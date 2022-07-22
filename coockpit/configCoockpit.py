import os


SEP_DIR ="\\"

DIRETORIO_BASE = os.path.dirname(os.path.dirname(__file__))

DIRETORIO_ARQUIVOS = SEP_DIR.join([DIRETORIO_BASE, "arquivos"])

DIRETORIO_ARQUIVOS_TEMP = SEP_DIR.join([DIRETORIO_BASE, "temp"])


CREDENCIAIS = [
    {
        "usuario": "xxxxxxx",
        "senha": "xxxxxxx"
    }
]




