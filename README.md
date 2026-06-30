# PMSA API Servidores de Jogos

API REST desenvolvida para o Trabalho Final da disciplina de Cloud Computing, do curso de Sistemas de Informação da UNIDAVI.

O projeto tem como tema **servidores de jogos** e disponibiliza rotas para consultar o status da aplicação, listar servidores simulados e buscar um servidor específico pelo seu identificador.

A API foi desenvolvida com **Python** e **FastAPI**, utilizando dados simulados armazenados em um arquivo JSON externo. O projeto também possui testes unitários com **Pytest**, análise estática com **Ruff**, execução em container com **Docker** e pipeline de Integração Contínua com **GitHub Actions**.

---

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pytest
* HTTPX
* Ruff
* Docker
* GitHub Actions

---

## Estrutura do projeto

```text
pmsa-api/
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── data/
│   │   └── servidores.json
│   └── tests/
│       ├── __init__.py
│       └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Rotas disponíveis

### Verificar status da API

```http
GET /status
```

Exemplo de resposta:

```json
{
    "nome": "API de Servidores de Jogos",
    "versao": "1.0.0",
    "status": "online"
}
```

---

### Listar servidores

```http
GET /servidores
```

Exemplo de resposta:

```json
{
    "sucesso": true,
    "quantidade": 10,
    "dados": [
        {
            "id": 1,
            "nome": "Alpha PvP Brasil",
            "jogo": "Minecraft",
            "regiao": "Brasil",
            "status": "online",
            "jogadores_online": 82,
            "capacidade": 100,
            "modo": "PvP",
            "versao": "1.7.10",
            "ping_ms": 28
        }
    ]
}
```

---

### Buscar servidor por identificador

```http
GET /servidores/{id}
```

Exemplo:

```http
GET /servidores/1
```

Exemplo de resposta para servidor existente:

```json
{
    "sucesso": true,
    "dados": {
        "id": 1,
        "nome": "Alpha PvP Brasil",
        "jogo": "Minecraft",
        "regiao": "Brasil",
        "status": "online",
        "jogadores_online": 82,
        "capacidade": 100,
        "modo": "PvP",
        "versao": "1.7.10",
        "ping_ms": 28
    }
}
```

Exemplo de resposta para servidor inexistente:

```json
{
    "sucesso": false,
    "erro": "Servidor não encontrado."
}
```

Nesse caso, a API retorna o código HTTP `404`.

---

## Dados simulados

Os dados utilizados pela API estão armazenados no arquivo:

```text
api/data/servidores.json
```

Esse arquivo contém 10 registros simulados de servidores de jogos, com informações como:

* identificador;
* nome do servidor;
* jogo;
* região;
* status;
* quantidade de jogadores online;
* capacidade máxima;
* modo de jogo;
* versão;
* ping em milissegundos.

Os dados não estão embutidos diretamente no código-fonte da aplicação.

---

# Execução local sem Docker

## Pré-requisitos

Antes de executar o projeto localmente, é necessário ter instalado:

* Python 3.13 ou superior;
* Git;
* terminal PowerShell, CMD ou equivalente.

---

## 1. Clonar o repositório

```powershell
git clone https://github.com/PedroMuci/pmsa-api.git
```

Acesse a pasta do projeto:

```powershell
cd pmsa-api
```

---

## 2. Criar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
.\venv\Scripts\activate
```

Se o ambiente virtual foi ativado corretamente, o terminal deverá exibir algo parecido com:

```powershell
(venv) PS C:\caminho\pmsa-api>
```

---

## 3. Instalar as dependências

Com o ambiente virtual ativado, execute:

```powershell
pip install -r requirements.txt
```

Esse comando instala as bibliotecas necessárias para executar a API, os testes e a análise estática de código.

---

## 4. Executar a API localmente

Na raiz do projeto, execute:

```powershell
uvicorn api.app:app --reload
```

Se a aplicação iniciar corretamente, o terminal exibirá uma mensagem parecida com:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## 5. Acessar a API no navegador

Com a API em execução, acesse:

```text
http://127.0.0.1:8000/status
```

Para listar os servidores:

```text
http://127.0.0.1:8000/servidores
```

Para buscar um servidor específico:

```text
http://127.0.0.1:8000/servidores/1
```

Para acessar a documentação automática do FastAPI:

```text
http://127.0.0.1:8000/docs
```

---

## 6. Encerrar a execução local

Para parar o servidor local, volte ao terminal em que o Uvicorn está rodando e pressione:

```text
CTRL + C
```

---

# Execução com Docker

## Pré-requisitos

Para executar a aplicação com Docker, é necessário ter instalado:

* Docker;
* Docker Desktop, no caso do Windows;
* Git, caso deseje clonar o repositório.

---

## 1. Clonar o repositório

```powershell
git clone https://github.com/PedroMuci/pmsa-api.git
```

Acesse a pasta do projeto:

```powershell
cd pmsa-api
```

---

## 2. Construir a imagem Docker

Na raiz do projeto, execute:

```powershell
docker build -t pmsa-api .
```

Esse comando cria uma imagem Docker local chamada `pmsa-api`, utilizando as instruções definidas no arquivo `Dockerfile`.

---

## 3. Executar o container

Após construir a imagem, execute:

```powershell
docker run --name pmsa-api-container -p 8000:8000 pmsa-api
```

Esse comando cria e executa um container chamado `pmsa-api-container`, mapeando a porta `8000` do container para a porta `8000` da máquina local.

---

## 4. Acessar a API pelo navegador

Com o container em execução, acesse:

```text
http://127.0.0.1:8000/status
```

Para listar os servidores:

```text
http://127.0.0.1:8000/servidores
```

Para buscar um servidor específico:

```text
http://127.0.0.1:8000/servidores/1
```

Para acessar a documentação automática:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Parar o container

No terminal em que o container está rodando, pressione:

```text
CTRL + C
```

---

## 6. Remover o container

Caso queira remover o container criado, execute:

```powershell
docker rm pmsa-api-container
```

Se o container ainda estiver em execução, use:

```powershell
docker rm -f pmsa-api-container
```

---

## 7. Executar novamente após remover o container

Caso o container tenha sido removido, é possível executá-lo novamente com:

```powershell
docker run --name pmsa-api-container -p 8000:8000 pmsa-api
```

---

# Testes unitários

O projeto possui testes unitários implementados com Pytest.

Os testes estão localizados em:

```text
api/tests/test_api.py
```

Foram implementados quatro testes principais:

1. Verificação de retorno HTTP 200 na rota `GET /servidores`;
2. Validação da estrutura JSON retornada pela rota `GET /servidores`;
3. Verificação de retorno HTTP 404 para servidor inexistente em `GET /servidores/{id}`;
4. Validação da rota `GET /status`.

---

## Executar os testes

Com o ambiente virtual ativado, execute:

```powershell
pytest
```

Resultado esperado:

```text
4 passed
```

---

# Análise estática com Ruff

O projeto utiliza Ruff para análise estática do código Python.

Para executar a verificação localmente, use:

```powershell
python -m ruff check api
```

Resultado esperado:

```text
All checks passed!
```

---

# Integração Contínua com GitHub Actions

O projeto possui um pipeline de Integração Contínua configurado com GitHub Actions.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

O pipeline é executado automaticamente em eventos de `push` e `pull_request` na branch `main`.

As etapas configuradas no pipeline são:

1. Checkout do código;
2. Configuração do Python;
3. Instalação das dependências;
4. Verificação de qualidade do código com Ruff;
5. Execução dos testes unitários com Pytest.

A etapa com Ruff foi incluída como verificação adicional além dos testes unitários.

---

# Possíveis problemas e soluções

## Porta 8000 já está em uso

Se a porta `8000` já estiver sendo usada por outro processo, a API pode não iniciar corretamente.

Uma solução é encerrar o processo que está usando a porta ou executar a API em outra porta.

Exemplo com Uvicorn em outra porta:

```powershell
uvicorn api.app:app --reload --port 8001
```

Nesse caso, acesse:

```text
http://127.0.0.1:8001/status
```

---

## Container com nome já existente

Se aparecer erro informando que o container `pmsa-api-container` já existe, remova o container antigo:

```powershell
docker rm -f pmsa-api-container
```

Depois execute novamente:

```powershell
docker run --name pmsa-api-container -p 8000:8000 pmsa-api
```

---

## Docker não está em execução

Se aparecer erro de conexão com o Docker, verifique se o Docker Desktop está aberto e em execução.

Depois tente novamente:

```powershell
docker build -t pmsa-api .
```

---

# Versionamento

O projeto foi versionado com Git e publicado no GitHub.

O desenvolvimento foi dividido em commits incrementais, registrando a evolução da aplicação em etapas, como:

* criação da estrutura inicial;
* criação dos dados simulados;
* implementação das rotas;
* criação dos testes unitários;
* configuração do pipeline CI;
* configuração do Docker.

---

# Autor

Pedro Muci

Curso de Sistemas de Informação UNIDAVI
Disciplina: Cloud Computing
Tema: Servidor de jogos
