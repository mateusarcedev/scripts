<div align="center">

# 🛠️ Scripts & Automações / Automations

**[ 🇧🇷 Versão em Português ](#-português-pt-br)** &nbsp;&nbsp;|&nbsp;&nbsp; **[ 🇺🇸 English Version ](#-english-en)**

</div>

---

<a name="português-pt-br"></a>
## 🇧🇷 Português (PT-BR)

Repositório central de utilitários e automações em Python para organização de arquivos, processamento de mídias e tarefas operacionais do dia a dia.

### 📁 Estrutura do Repositório

```text
scripts/
├── google_drive/                 # Gestão e organização de acervos na nuvem
│   └── organize_drive_ebooks.py  # Categorização de livros técnicos e limpeza de pastas
│
├── subtitles/                    # Processamento e estilização de legendas de vídeo
│   └── convert_srt_to_4k_ass.py  # Conversor SRT para ASS formatado em 4K
│
├── README.md                     # Documentação bilíngue (PT-BR / EN)
└── README.en.md                  # Dedicated English README
```

---

### 🎯 Módulos e Objetivos de Negócio

#### 1. Processamento e Estilização de Legendas (`subtitles/`)

##### 📄 [`convert_srt_to_4k_ass.py`](file:///Users/mateusarce/projetos/scripts/subtitles/convert_srt_to_4k_ass.py)
* **Objetivo de Negócio**: 
  Legendas no formato padrão `.srt` não possuem informações de estilo visual, resultando em textos pequenos, fontes genéricas e legibilidade prejudicada quando exibidas em telas grandes ou vídeos de alta resolução (4K). 
  
  Este script tem a finalidade de converter arquivos `.srt` em `.ass` (*Advanced SubStation Alpha*) com configurações visuais de alto contraste e legibilidade, projetadas especificamente para transmissões, exibições em igrejas/eventos e vídeos em resolução Ultra HD (3840x2160).

* **Regras de Negócio & Transformações**:
  - **Calibração de Resolução 4K**: Configura a área de exibição nativa para 3840x2160 (`PlayResX: 3840`, `PlayResY: 2160`).
  - **Tipografia e Contraste**: Aplica fonte `Arial Black` em tamanho 280 com cor amarela de destaque, contorno escuro espesso (12px) e sombra (6px) para garantir leitura clara sobre qualquer fundo de imagem.
  - **Posicionamento Seguro**: Define margens inferiores de 180px para evitar cortes por barras de reprodução ou sobreposição com elementos de interface.
  - **Conversão de Timecodes**: Converte a precisão de tempo do padrão SRT (milissegundos separados por vírgula) para o padrão ASS (centésimos de segundo).

---

#### 2. Gestão do Google Drive (`google_drive/`)

##### 📄 [`organize_drive_ebooks.py`](file:///Users/mateusarce/projetos/scripts/google_drive/organize_drive_ebooks.py)
* **Objetivo de Negócio**: 
  Após migrações ou downloads em lote, documentos e livros técnicos acumulam-se desordenados na nuvem. A busca manual por referências de estudo torna-se lenta e ineficiente.
  
  Este script automatiza a catalogação e organização do acervo digital no Google Drive, alocando cada livro técnico em sua respectiva trilha de conhecimento, além de higienizar o drive descartando arquivos duplicados e pastas esvaziadas.

* **Regras de Negócio & Categorização**:
  - **Classificação por Trilha Temática**:
    - **Algoritmos e Estruturas de Dados**: Livros e materiais de teoria de algoritmos, grafos, resolução de problemas e compiladores.
    - **Machine Learning e Matemática**: Obras sobre aprendizado de máquina, probabilidade, teoria da computação e Spark.
    - **Banco de Dados**: Referências de bancos relacionais, otimização de consultas SQL, NoSQL (Redis) e grafos (Neo4j).
    - **Outros / Geral**: Manuais de engenharia, livros institucionais/legais e materiais complementares.
  - **Movimentação Segura**: Altera a hierarquia de pastas diretamente na API do Google Drive (`addParents`/`removeParents`) sem necessidade de download/upload dos arquivos.
  - **Higienização de Duplicatas e Diretórios**: Identifica arquivos repetidos e envia para a lixeira, removendo também diretórios residuais de migrações anteriores (ex: pastas vazias de backups antigos).

---

### 🚀 Boas Práticas para Novos Scripts

Ao adicionar novos scripts ao repositório:
1. **Modularização por Domínio**: Crie uma pasta específica para o assunto ou contexto de negócio do script (ex: `finance/`, `media_processing/`, `backup/`).
2. **Nomenclatura Semântica**: Nomeie os arquivos com verbos de ação e objetivos claros (ex: `generate_monthly_report.py`, `compress_video_files.py`).
3. **Documentação**: Atualize este `README.md` destacando a necessidade que o script resolve e suas regras de funcionamento.

---
---

<a name="english-en"></a>
## 🇺🇸 English (EN)

Centralized repository for Python utilities and automations focused on file organization, media processing, and everyday operational tasks.

### 📁 Repository Structure

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

### 🎯 Modules & Business Objectives

#### 1. Video Subtitle Processing & Styling (`subtitles/`)

##### 📄 [`convert_srt_to_4k_ass.py`](file:///Users/mateusarce/projetos/scripts/subtitles/convert_srt_to_4k_ass.py)
* **Business Objective**: 
  Standard `.srt` subtitles lack styling metadata, leading to small, generic text and poor readability when rendered on large displays or high-resolution (4K) videos.
  
  This script converts basic `.srt` files into `.ass` (*Advanced SubStation Alpha*) format with tailored high-contrast styling designed specifically for 4K Ultra HD (3840x2160) video presentations, church services/events, and broadcast screens.

* **Business Rules & Transformations**:
  - **4K Canvas Resolution**: Sets native display dimensions to 3840x2160 (`PlayResX: 3840`, `PlayResY: 2160`).
  - **High-Contrast Typography**: Applies `Arial Black` at font size 280 in high-visibility yellow, with a thick black outline (12px) and shadow (6px) to guarantee readability over any background footage.
  - **Safe Margins**: Defines a 180px vertical bottom margin to prevent occlusion by media player controls or interface overlays.
  - **Timecode Precision Conversion**: Translates SRT millisecond timecodes (comma format) to the ASS standard (centisecond format).

---

#### 2. Google Drive Storage Management (`google_drive/`)

##### 📄 [`organize_drive_ebooks.py`](file:///Users/mateusarce/projetos/scripts/google_drive/organize_drive_ebooks.py)
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

### 🚀 Guidelines for Adding New Scripts

When contributing new scripts to this repository:
1. **Domain-Driven Modularization**: Group scripts into designated subfolders based on their business domain (e.g., `finance/`, `media_processing/`, `backup/`).
2. **Semantic Naming**: Use descriptive action verbs for filenames (e.g., `generate_monthly_report.py`, `compress_video_files.py`).
3. **Documentation**: Keep the `README.md` updated with business purpose, input/output requirements, and operational rules in both Portuguese and English.
