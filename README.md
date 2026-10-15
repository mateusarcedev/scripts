# 🛠️ Scripts & Automações

Utilitários e automações em Python para organização de arquivos, processamento de mídias e tarefas operacionais do dia a dia.

[🇺🇸 English version](README.en.md)

---

### 📁 Estrutura

```text
scripts/
├── google_drive/
│   └── organize_drive_ebooks.py  # Migração única do acervo de ebooks no Google Drive
├── subtitles/
│   └── convert_srt_to_4k_ass.py  # Conversor SRT para ASS formatado em 4K
├── tests/                        # Testes (unittest, biblioteca padrão)
└── requirements.txt              # Dependências do script do Google Drive
```

### ⚙️ Requisitos

- Python 3.10+
- `subtitles/` usa apenas a biblioteca padrão.
- `google_drive/` precisa de `requests`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

### 1. Legendas — [`subtitles/convert_srt_to_4k_ass.py`](subtitles/convert_srt_to_4k_ass.py)

Converte `.srt` em `.ass` (*Advanced SubStation Alpha*) com estilo de alto contraste para vídeos 4K (3840x2160), exibições em telões, igrejas e eventos.

```bash
python3 subtitles/convert_srt_to_4k_ass.py legenda.srt                 # gera legenda.ass
python3 subtitles/convert_srt_to_4k_ass.py legenda.srt saida.ass --force
```

- **Resolução**: `PlayResX: 3840`, `PlayResY: 2160`.
- **Tipografia**: `Arial Black` tamanho 280, amarelo, contorno 12px e sombra 6px. No Linux a fonte normalmente não vem instalada e o player usa uma substituta.
- **Margem inferior**: 180px.
- **Timecodes**: converte milissegundos do SRT (`,` ou `.`, com ou sem espaços em `-->`) para centésimos do ASS.
- **Texto**: `<i>`, `<b>` e `<u>` viram tags ASS; outras tags HTML são removidas; `{` e `}` são escapadas.
- **Segurança**: não sobrescreve a saída sem `--force`; em caso de SRT inválido, termina com erro e não grava arquivo parcial.

### 2. Google Drive — [`google_drive/organize_drive_ebooks.py`](google_drive/organize_drive_ebooks.py)

Script de **uso único** que reorganizou um acervo específico de ebooks: os IDs de arquivos e pastas estão fixos no código, então ele não funciona em outro Drive sem edição.

> ⚠️ Executa imediatamente ao rodar, sem modo de simulação: move arquivos, envia uma duplicata conhecida e pastas para a lixeira (pastas enviadas para a lixeira levam o conteúdo junto). Revise os IDs antes de executar.

```bash
export GDRIVE_TOKEN='token_oauth_com_escopo_drive'   # token de acesso; expira em ~1h
python3 google_drive/organize_drive_ebooks.py
```

---

### 🧪 Testes

```bash
python3 -m unittest discover -s tests -v
```

O CI executa os testes em Ubuntu e Windows (Python 3.10 e 3.13).

### 🚀 Boas práticas para novos scripts

1. **Pasta por domínio** (ex.: `finance/`, `media_processing/`, `backup/`) e nomes com verbo de ação (ex.: `compress_video_files.py`).
2. **Sem caminhos, IDs ou tokens fixos no código**: receba entradas por argumentos (`argparse`) e segredos por variável de ambiente.
3. **Ações destrutivas** (apagar, mover, sobrescrever) exigem confirmação explícita, como `--force` ou `--apply`.
4. **Documente** o uso aqui e em `README.en.md`, e adicione testes para a lógica que não depende de serviços externos.
