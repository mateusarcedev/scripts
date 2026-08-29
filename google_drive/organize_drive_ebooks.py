"""
Organizador de Ebooks e Limpeza de Pastas no Google Drive.

Objetivo:
  Categoriza livros técnicos e documentos acadêmicos em pastas temáticas
  no Google Drive (Algoritmos, ML/Matemática, Banco de Dados, Outros),
  move os arquivos via API sem necessidade de re-upload, descarta
  duplicatas e higieniza pastas vazias.

Uso:
  python3 google_drive/organize_drive_ebooks.py
"""

import os
import sys
import requests

# Carrega o token OAuth da variável de ambiente GDRIVE_TOKEN ou GOOGLE_DRIVE_TOKEN
TOKEN = os.getenv("GDRIVE_TOKEN") or os.getenv("GOOGLE_DRIVE_TOKEN", "")
BASE  = "https://www.googleapis.com/drive/v3"

def h():
    if not TOKEN:
        print("[ERRO] Token do Google Drive não configurado.")
        print("Defina a variável de ambiente antes de executar:")
        print("  export GDRIVE_TOKEN='seu_token_oauth'")
        sys.exit(1)
    return {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def move(file_id, new_parent, old_parent, label=""):
    r = requests.patch(
        f"{BASE}/files/{file_id}",
        params={"addParents": new_parent, "removeParents": old_parent, "fields": "id,name"},
        headers=h(),
    )
    status = "v" if r.ok else f"X [{r.status_code}]"
    print(f"  {status} {label}")

def trash(file_id, label=""):
    r = requests.patch(f"{BASE}/files/{file_id}", json={"trashed": True}, headers=h())
    status = "~" if r.ok else f"X [{r.status_code}]"
    print(f"  {status} Lixeira: {label}")

# ── IDs das pastas Ebooks
EBOOKS   = "1esS4FFPjbdYT3xik2EyImQpDRdW9Jlw0"
ALGO     = "1iF_g4sGL__2E3YwuThFIbUrIfZKRo0I4"   # Algoritmos e Estruturas de Dados
ML_MAT   = "1cNCR0Vl5BGbOdTYTa2_FQ_4NhIEdl6mr"   # Machine Learning e Matemática
DB       = "10iwBqIuf-qgtCsiYNFLEZHIkV8lS8u14"   # Banco de Dados
OUTROS_E = "1lNhfD8jqwrf3ycv8lECt8-wG4GWdYd6q"   # Outros (Ebooks)

# ── IDs de pastas a deletar (vazias)
PASTA_OUTROS_DOCS = "1Bk9ubB1XfKYW5FCIO1GqZUA0I4yWPSLJ"  # Outros (raiz Documentos)
PASTA_MATEUS      = "1PDUgAA8Xw9EWAQKrRIJdyavD-WuWj3AW"  # Mateus/
ONEDRIVE_PASTA    = "1o_fR5YCkTfX1kdjmQD1J14x1MGkyadDK"  # OneDrive_2026-04-26/
MATEUS_ARCE_SUB   = "1AsmMAX74Qpg8ZVnKkDabx7-NTgjXcV_0"  # __Mateus Arce/ dentro do OneDrive

# ── Algoritmos e Estruturas de Dados
print("\n[Algoritmos e Estruturas de Dados]")
algo_ids = [
    ("1grisRm9Drln0XBdXdpDdeewNMx2ABOQj", "Algorithms-JeffE.pdf"),
    ("1gtxsP4NYV8UnfZtsC1gCPKDH1J0ofk7W", "Algorithms in C.pdf"),
    ("1h4jICp37RLz8lD3AUfBo8bu6RdlZx8Rk", "Algorithm Design.pdf"),
    ("1h6Fbz-Fj9S1ZjlkVQ0ZkYaJWl62GfnIT", "Advanced Problem Solving.pdf"),
    ("1h6lXOCMHWLAV0TbrUg1XxCZTlHhN5guY", "Advanced Algorithms.pdf"),
    ("1geceXE3fl9ty62fV09ENAQOjYlxjIAfe", "An-Open-Guide-to-Data-Structures-and-Algorithms.pdf"),
    ("1gGwv8xNRji2dB0IUSaoVgS-d3cad12vb", "Anu's Prep List.pdf"),
    ("1g4Nj_6kaueBJKHkDhDcwrEboVXWiAGFF", "Data Structures and Algorithm.pdf"),
    ("1fppHZowRJbcJCiy7Ora8y1GvrUilHzz8", "Dsa.pdf"),
    ("1flXF6q_lRX6erKCHNnepgbmWhNmsxi3O", "Entendendo Algoritmos.pdf"),
    ("1fdD_R-vbZ0OmXT6SpCPZpTQf3wR6bONP", "Estruturas de Dados Abertas (C++).pdf"),
    ("1fQulEjtxuHOjrO2dme7r8y74vBY8lMwY", "GraphAlgorithms.pdf"),
    ("1gEs5gNyuto-a6io2z_24c2qS3XeS0k6x", "Competitive Programmer's Handbook.pdf"),
    ("1gDV-DjET5RvPZUEuoMS7tJ0zMGnytXuF", "cp2.pdf"),
    ("1hDCR8BGwxj-MePmtULOSotZzAnmBVJYx", "The Little Book of Algorithms 2.0.pdf"),
    ("1h8T90LeYPkGNWFoy2FcHPX3ZVI13NGU5", "Think Data Structures.pdf"),
    ("1hcRrWxmkE92d3UDhP1EC9smZ8wLjKy_U", "Open Data Structures.pdf"),
    ("1hIkfXhouNpbF-ayWEp0lWIO-c_O31IB_", "Writing a C Compiler - 2024.pdf"),
    ("1fveY0c6LflTWiMgSbR0ev_pPZFZrODky", "Design and Implementation of an Interpreter.pdf"),
]
for fid, nome in algo_ids:
    move(fid, ALGO, EBOOKS, nome)

# ── Machine Learning e Matemática
print("\n[Machine Learning e Matematica]")
ml_ids = [
    ("1f3DdxzxQZlLkNZvZsvCxl3ATN5hJrZNF", "Machine Learning using Python.pdf"),
    ("1fGrtxRlWhmI72saUOmqQySyVU2RgAL6o", "Learning Theory from First Principles.pdf"),
    ("1f7qwutaIxUcML3R1QGaWdg4zeSPdWi72", "LearningSpark2.0.pdf"),
    ("1f-MuLpfuJsFqIHkOd3pg62yOj7n3nO2J", "Mathematical Foundations of Computing.pdf"),
    ("1hS9-kTUD07pwXJwZa7IYFYq8z1lK1FeN", "ProbabilityforComputerScientists.pdf"),
    ("1-3V-ZayCaTTtlr8YE-HFj0HfVx3ox5dt", "lista_de_probabilidade.pdf"),
]
for fid, nome in ml_ids:
    move(fid, ML_MAT, EBOOKS, nome)

# ── Banco de Dados
print("\n[Banco de Dados]")
db_ids = [
    ("1hQd8bZzthOwMyOSn_OHyiyoNGF8AZ1UP", "Redis-For-Dummies.pdf"),
    ("1fVioswNGmpNFaeBdM3VJmyQtsMF54JIU", "Graph_Databases_2e_Neo4j.pdf"),
    ("1ex5dSKJ53ei6YKoU8Wh58lzntaORLHoP", "sql_query_optimization_techniques.pdf"),
    ("1hcfoIXwz5KR_doEyashqhrY9YRICmWOD", "next-level-database-techniques-for-developers.pdf"),
]
for fid, nome in db_ids:
    move(fid, DB, EBOOKS, nome)

# ── Outros (Ebooks)
print("\n[Outros Ebooks]")
outros_ids = [
    ("1jd7uPceDyam3TaLuYqj16kVEy5nRs1tt", "Livro Beer - Mecanica dos Materiais.pdf"),
    ("1jnaMoaGEHSFLWamuWDJRlTii8avaP8_l", "7Fundamentos-2.pdf"),
    ("1fmp_tW00xTa7CBBE5UTZwEDYsQ9Vi36N", "Engineer's Mini-Notebook - IC Applications.pdf"),
    ("1fpuwJ_2fkOKTo6rMWnHSHK0To4Qz9ETz", "Docker For Beginners.pdf"),
    ("1t1H4Ii8BI0uH6EIVIKWufQilbhuyB4XE", "Codigo Civil 2 ed.pdf"),
]
for fid, nome in outros_ids:
    move(fid, OUTROS_E, EBOOKS, nome)

# ── Duplicata Código Civil
print("\n[Limpeza duplicatas]")
trash("1ihMY4Ky_M1uwsZsLZqOA-Xe9U-D23aiS", "Codigo Civil 2 ed_copia.pdf (duplicata)")

# ── Pastas vazias -> lixeira
print("\n[Pastas vazias -> Lixeira]")
trash(PASTA_OUTROS_DOCS, "Outros/ (raiz Documentos - vazia)")
trash(MATEUS_ARCE_SUB,   "__Mateus Arce/ (OneDrive - esvaziada)")
trash(ONEDRIVE_PASTA,    "OneDrive_2026-04-26/ (esvaziada)")
# Pasta Mateus/ - verificar se ainda tem Horas complementares antes de apagar
# trash(PASTA_MATEUS, "Mateus/ (verificar se vazia)")

print("\nFase 2 concluida!")
print("Verifique a pasta 'Mateus/' manualmente - pode ainda ter 'Horas complementares'.")