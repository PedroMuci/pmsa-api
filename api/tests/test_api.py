from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_listar_servidores_retorna_status_200():
    resposta = client.get("/servidores")

    assert resposta.status_code == 200


def test_listar_servidores_retorna_estrutura_json_esperada():
    resposta = client.get("/servidores")
    corpo = resposta.json()

    assert "sucesso" in corpo
    assert "quantidade" in corpo
    assert "dados" in corpo

    assert corpo["sucesso"] is True
    assert corpo["quantidade"] == 10
    assert isinstance(corpo["dados"], list)

    primeiro_servidor = corpo["dados"][0]

    campos_obrigatorios = [
        "id",
        "nome",
        "jogo",
        "regiao",
        "status",
        "jogadores_online",
        "capacidade",
        "modo",
        "versao",
        "ping_ms",
    ]

    for campo in campos_obrigatorios:
        assert campo in primeiro_servidor


def test_buscar_servidor_inexistente_retorna_status_404():
    resposta = client.get("/servidores/999")
    corpo = resposta.json()

    assert resposta.status_code == 404
    assert corpo["sucesso"] is False
    assert corpo["erro"] == "Servidor não encontrado."


def test_rota_status_retorna_dados_da_api():
    resposta = client.get("/status")
    corpo = resposta.json()

    assert resposta.status_code == 200
    assert corpo["nome"] == "API de Servidores de Jogos"
    assert corpo["versao"] == "1.0.0"
    assert corpo["status"] == "online"