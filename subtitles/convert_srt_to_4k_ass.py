"""
Conversor e Estilizador de Legendas para Resolução 4K (SRT -> ASS).

Objetivo:
  Converte legendas em formato SRT para o formato ASS estilizado para
  exibição em alta resolução (3840x2160 - 4K), com fonte grande, alto contraste
  e margens ajustadas para telas amplas e eventos/transmissões.

Uso:
  python3 subtitles/convert_srt_to_4k_ass.py entrada.srt [saida.ass] [--force]
"""

import argparse
import re
import sys
from pathlib import Path

# Fontsize alterado para 280.
# Outline, Shadow e MarginV redimensionados proporcionalmente para 4K.
ASS_HEADER = """[Script Info]
Title: Legenda Estilizada 4K Grande
ScriptType: v4.00+
Collisions: Normal
PlayResX: 3840
PlayResY: 2160

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial Black,280,&H0000FFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,12,6,2,20,20,180,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

ASS_LINE_BREAK = "\\N"

_TIME = r"(\d{1,2}):(\d{2}):(\d{2})(?:[,.](\d{1,3}))?"
TIMING_RE = re.compile(rf"^\s*{_TIME}\s*-->\s*{_TIME}")
FORMAT_TAG_RE = re.compile(r"<(/?)([ibu])>", re.IGNORECASE)
OTHER_TAG_RE = re.compile(r"</?[a-z][^>]*>", re.IGNORECASE)


class SrtError(ValueError):
    pass


def srt_time_to_ass(hours, minutes, seconds, millis):
    """Converte partes de um timecode SRT para o formato ASS (centésimos)."""
    centis = int((millis or "0").ljust(3, "0")) // 10
    return f"{int(hours)}:{minutes}:{seconds}.{centis:02d}"


def _format_tag(match):
    closing, tag = match.groups()
    return "{\\" + tag.lower() + ("0" if closing else "1") + "}"


def srt_text_to_ass(text):
    """Escapa chaves e converte <i>/<b>/<u> em tags ASS; remove outras tags HTML."""
    text = text.replace("{", "\\{").replace("}", "\\}")
    text = FORMAT_TAG_RE.sub(_format_tag, text)
    return OTHER_TAG_RE.sub("", text)


def srt_to_ass(srt_content):
    """Converte o conteúdo de um SRT em conteúdo ASS completo."""
    lines = srt_content.splitlines()
    events = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if "-->" not in line:
            i += 1
            continue

        match = TIMING_RE.match(line)
        if not match:
            raise SrtError(f"linha {i + 1}: timecode inválido: {line!r}")
        start = srt_time_to_ass(*match.groups()[:4])
        end = srt_time_to_ass(*match.groups()[4:])

        text = []
        i += 1
        while i < len(lines) and lines[i].strip():
            text.append(srt_text_to_ass(lines[i].strip()))
            i += 1

        events.append(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{ASS_LINE_BREAK.join(text)}\n")

    if not events:
        raise SrtError("nenhuma legenda encontrada no arquivo")
    return ASS_HEADER + "".join(events)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Converte uma legenda SRT em ASS estilizado para 4K.")
    parser.add_argument("input", type=Path, help="arquivo .srt de entrada")
    parser.add_argument("output", type=Path, nargs="?", help="arquivo .ass de saída (padrão: mesmo nome com .ass)")
    parser.add_argument("--force", action="store_true", help="sobrescreve a saída se ela já existir")
    args = parser.parse_args(argv)

    output = args.output or args.input.with_suffix(".ass")
    if not args.input.is_file():
        parser.error(f"arquivo de entrada não encontrado: {args.input}")
    if output.exists() and not args.force:
        parser.error(f"saída já existe: {output} (use --force para sobrescrever)")

    try:
        content = srt_to_ass(args.input.read_text(encoding="utf-8-sig"))
    except (SrtError, UnicodeDecodeError) as e:
        print(f"erro: {args.input}: {e}", file=sys.stderr)
        return 1

    output.write_text(content, encoding="utf-8")
    print(f"gerado: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
