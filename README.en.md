# 🛠️ Scripts & Automations

Python utilities and automations for file organization, media processing and everyday operational tasks.

[🇧🇷 Versão em português](README.md)

---

### 📁 Structure

```text
scripts/
├── google_drive/
│   └── organize_drive_ebooks.py  # One-off migration of an ebook library on Google Drive
├── subtitles/
│   └── convert_srt_to_4k_ass.py  # SRT to 4K-styled ASS subtitle converter
├── tests/                        # Tests (unittest, standard library)
└── requirements.txt              # Dependencies for the Google Drive script
```

### ⚙️ Requirements

- Python 3.10+
- `subtitles/` uses only the standard library.
- `google_drive/` needs `requests`:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

### 1. Subtitles — [`subtitles/convert_srt_to_4k_ass.py`](subtitles/convert_srt_to_4k_ass.py)

Converts `.srt` into `.ass` (*Advanced SubStation Alpha*) with high-contrast styling for 4K (3840x2160) video, large screens, church services and events.

```bash
python3 subtitles/convert_srt_to_4k_ass.py subtitle.srt                 # writes subtitle.ass
python3 subtitles/convert_srt_to_4k_ass.py subtitle.srt output.ass --force
```

- **Resolution**: `PlayResX: 3840`, `PlayResY: 2160`.
- **Typography**: `Arial Black` size 280, yellow, 12px outline and 6px shadow. Linux usually lacks the font, so the player falls back to a substitute.
- **Bottom margin**: 180px.
- **Timecodes**: converts SRT milliseconds (`,` or `.`, with or without spaces around `-->`) to ASS centiseconds.
- **Text**: `<i>`, `<b>` and `<u>` become ASS tags; other HTML tags are stripped; `{` and `}` are escaped.
- **Safety**: never overwrites the output without `--force`; an invalid SRT exits with an error and writes no partial file.

### 2. Google Drive — [`google_drive/organize_drive_ebooks.py`](google_drive/organize_drive_ebooks.py)

**One-off** script that reorganized a specific ebook library: file and folder IDs are hardcoded, so it does not work on another Drive without editing.

> ⚠️ Runs immediately with no dry-run mode: it moves files and trashes a known duplicate and folders (trashing a folder also trashes its contents). Review the IDs before running.

```bash
export GDRIVE_TOKEN='oauth_access_token_with_drive_scope'   # access token; expires in ~1h
python3 google_drive/organize_drive_ebooks.py
```

---

### 🧪 Tests

```bash
python3 -m unittest discover -s tests -v
```

CI runs the tests on Ubuntu and Windows (Python 3.10 and 3.13).

### 🚀 Guidelines for new scripts

1. **One folder per domain** (e.g. `finance/`, `media_processing/`, `backup/`) and action-verb file names (e.g. `compress_video_files.py`).
2. **No hardcoded paths, IDs or tokens**: take inputs as arguments (`argparse`) and secrets from environment variables.
3. **Destructive actions** (delete, move, overwrite) require explicit opt-in such as `--force` or `--apply`.
4. **Document** usage here and in `README.md`, and add tests for logic that does not depend on external services.
