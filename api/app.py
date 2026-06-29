from fastapi import FastAPI

app = FastAPI(
    title="API de Servidores de Jogos",
    version="1.0.0",
    description="API REST para consulta de servidores de jogos simulados."
)


@app.get("/status")
def obter_status():
    return {
        "nome": "API de Servidores de Jogos",
        "versao": "1.0.0",
        "status": "online"
    }