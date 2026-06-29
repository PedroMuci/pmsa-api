import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="API de Servidores de Jogos",
    version="1.0.0",
    description="API REST para consulta de servidores de jogos simulados.",
)

CAMINHO_DADOS = Path(__file__).parent / "data" / "servidores.json"


def carregar_servidores():
    with CAMINHO_DADOS.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


@app.get("/status")
def obter_status():
    return {
        "nome": "API de Servidores de Jogos",
        "versao": "1.0.0",
        "status": "online",
    }


@app.get("/servidores")
def listar_servidores():
    try:
        servidores = carregar_servidores()

        return {
            "sucesso": True,
            "quantidade": len(servidores),
            "dados": servidores,
        }

    except (FileNotFoundError, json.JSONDecodeError):
        return JSONResponse(
            status_code=500,
            content={
                "sucesso": False,
                "erro": "Erro ao carregar os dados dos servidores.",
            },
        )


@app.get("/servidores/{servidor_id}")
def buscar_servidor_por_id(servidor_id: int):
    try:
        servidores = carregar_servidores()

        for servidor in servidores:
            if servidor["id"] == servidor_id:
                return {
                    "sucesso": True,
                    "dados": servidor,
                }

        return JSONResponse(
            status_code=404,
            content={
                "sucesso": False,
                "erro": "Servidor não encontrado.",
            },
        )

    except (FileNotFoundError, json.JSONDecodeError):
        return JSONResponse(
            status_code=500,
            content={
                "sucesso": False,
                "erro": "Erro ao carregar os dados dos servidores.",
            },
        )