import os

DATA_INICIAR = '22-03-2022'

SEP_DIR ="\\"

DIRETORIO_BASE = os.path.dirname(os.path.dirname(__file__))

DIRETORIO_ARQUIVOS = SEP_DIR.join([DIRETORIO_BASE, "arquivos"])

DIRETORIO_ARQUIVOS_TEMP = SEP_DIR.join([DIRETORIO_BASE, "temp"])

DIRETORIO_ARQUIVOS_DE_PARA = SEP_DIR.join([DIRETORIO_BASE, "DE_PARA"])

CREDENCIAIS = [
    {
        "usuario": "etl@jumaconsultoria.com",
        "senha": "2022"
    }
]

URL_SISTEMA = "https://app.tecnofit.com.br/"


