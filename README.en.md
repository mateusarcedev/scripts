# 🛠️ Scripts & Automations

Centralized repository for Python utilities and automations focused on file organization, media processing, and everyday operational tasks.

[ 🇧🇷 Versão em Português (README.md)](file:///Users/mateusarce/projetos/scripts/README.md)

---

## 📁 Repository Structure

```text
scripts/
├── google_drive/                 # Cloud storage asset management & organization
│   └── organize_drive_ebooks.py  # Technical book categorization & directory cleanup
│
├── subtitles/                    # Video subtitle processing & styling
│   └── convert_srt_to_4k_ass.py  # SRT to 4K-styled ASS subtitle converter
│
├── README.md                     # Bilingual documentation (PT-BR / EN)
└── README.en.md                  # Dedicated English README
```

---

## 🎯 Modules & Business Objectives

### 1. Video Subtitle Processing & Styling (`subtitles/`)

#### 📄 [`convert_srt_to_4k_ass.py`](file:///Users/mateusarce/projetos/scripts/subtitles/convert_srt_to_4k_ass.py)
* **Business Objective**: 
  Standard `.srt` subtitles lack styling metadata, leading to small, generic text and poor readability when rendered on large displays or high-resolution (4K) videos.
  
  This script converts basic `.srt` files into `.ass` (*Advanced SubStation Alpha*) format with tailored high-contrast styling designed specifically for 4K Ultra HD (3840x2160) video presentations, church services/events, and broadcast screens.

* **Business Rules & Transformations**:
  - **4K Canvas Resolution**: Sets native display dimensions to 3840x2160 (`PlayResX: 3840`, `PlayResY: 2160`).
  - **High-Contrast Typography**: Applies `Arial Black` at font size 280 in high-visibility yellow, with a thick black outline (12px) and shadow (6px) to guarantee readability over any background footage.
  - **Safe Margins**: Defines a 180px vertical bottom margin to prevent occlusion by media player controls or interface overlays.
  - **Timecode Precision Conversion**: Translates SRT millisecond timecodes (comma format) to the ASS standard (centisecond format).

---

### 2. Google Drive Storage Management (`google_drive/`)

#### 📄 [`organize_drive_ebooks.py`](file:///Users/mateusarce/projetos/scripts/google_drive/organize_drive_ebooks.py)
* **Business Objective**: 
  Following large migrations or bulk downloads, digital libraries often become cluttered across root and temporary folders. Searching manually for study references becomes slow and cumbersome.
  
  This script automates the classification and restructuring of digital technical books on Google Drive, routing each item to its dedicated domain track while trashing duplicate copies and empty leftover folders.

* **Business Rules & Categorization**:
  - **Subject Track Routing**:
    - **Algorithms & Data Structures**: Books on algorithmic theory, graphs, problem-solving, and compilers.
    - **Machine Learning & Mathematics**: Works on machine learning, probability theory, foundations of computing, and Apache Spark.
    - **Databases**: Relational databases, SQL optimization, NoSQL (Redis), and graph databases (Neo4j).
    - **General / Other**: Engineering handbooks, legal codes, and general reference documents.
  - **Safe In-Place Relocation**: Modifies parent folder hierarchy directly via the Google Drive API (`addParents`/`removeParents`), eliminating the need to re-download or re-upload large files.
  - **Duplicate & Directory Hygiene**: Locates duplicate file copies and moves them to trash, expurgating empty folders from legacy backup structures.

---

## 🚀 Guidelines for Adding New Scripts

When contributing new scripts to this repository:
1. **Domain-Driven Modularization**: Group scripts into designated subfolders based on their business domain (e.g., `finance/`, `media_processing/`, `backup/`).
2. **Semantic Naming**: Use descriptive action verbs for filenames (e.g., `generate_monthly_report.py`, `compress_video_files.py`).
3. **Documentation**: Keep documentation updated with business purpose, input/output requirements, and operational rules in both Portuguese and English.
