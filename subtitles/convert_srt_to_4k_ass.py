"""
Conversor e Estilizador de Legendas para Resolução 4K (SRT -> ASS).

Objetivo:
  Converte legendas em formato SRT para o formato ASS estilizado para
  exibição em alta resolução (3840x2160 - 4K), com fonte grande, alto contraste
  e margens ajustadas para telas amplas e eventos/transmissões.

Uso:
  python3 subtitles/convert_srt_to_4k_ass.py [<caminho_entrada.srt> <caminho_saida.ass>]
"""

import sys


def srt_time_to_ass(time_str):
    time_str = time_str.replace(',', '.')
    parts = time_str.split(':')
    if len(parts) == 3:
        h, m, s = parts
        s, ms = s.split('.')
        h = int(h)
        return f"{h}:{m}:{s}.{ms[:2]}"
    return time_str


def convert_srt_to_ass(srt_file, ass_file):
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Fontsize alterado para 280.
    # Outline, Shadow e MarginV redimensionados proporcionalmente para 4K.
    ass_content = """[Script Info]
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

    with open(ass_file, 'w', encoding='utf-8') as f:
        f.write(ass_content)

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            if '-->' in line:
                start_time, end_time = line.split(' --> ')
                start_ass = srt_time_to_ass(start_time)
                end_ass = srt_time_to_ass(end_time)

                text = []
                i += 1
                while i < len(lines) and lines[i].strip():
                    text.append(lines[i].strip())
                    i += 1

                text_ass = "\\N".join(text)
                f.write(f"Dialogue: 0,{start_ass},{end_ass},Default,,0,0,0,,{text_ass}\n")
            else:
                i += 1


if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "/Users/mateusarce/Downloads/Igreja/Luzeirinhos_de_Tefe_Corrigido.srt"
        output_file = "/Users/mateusarce/Downloads/Igreja/Luzeirinhos_de_Tefe_Estilizado.ass"

    convert_srt_to_ass(input_file, output_file)