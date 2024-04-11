# <p align="center">Manipulando objetos no AWS S3<br>Explorando Botocore</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>     
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto consiste na criação de uma solução em Python para gerenciar objetos no Amazon S3, utilizando a biblioteca Botocore. Ele permite extrair e deletar objetos de forma automatizada na nuvem da AWS, oferecendo uma gestão eficiente e simplificada.

## Diagrama de Fluxo

![Diagram](https://github.com/tonsatomicos/dpp-duckdb-processing-persistence/blob/main/assets/diagram_pipeline.png?raw=true)

Sinta-se à vontade para clonar, adaptar e ajustar o projeto conforme necessário. Consulte as instruções abaixo, se precisar. :alien:

## Dependências do Projeto

Este projeto foi desenvolvido utilizando o Poetry para gerenciamento de ambientes virtuais e bibliotecas.

### Bibliotecas Utilizadas

- botocore (v1.34.78)
- python-dotenv (v1.0.1)

### Instalação das Dependências

Você pode instalar as dependências manualmente, ou, utilizando o Poetry ou o Pip com os seguintes comandos:

#### Utilizando Poetry

```bash
poetry config virtualenvs.in-project true
poetry env use 3.12.1
poetry install

```

#### Utilizando Pip

```bash
pip install botocore python-dotenv

```

## Configurações do Projeto - Parte 1

- Necessário conta na AWS.
- Baixe o <code>Acess Keys</code> no Security Credentials.
- Crie um arquivo <code>.env</code> na pasta <code>config</code> e salve nele a seguinte linha: <pre><code>aws_access_key_id=acess_key 
aws_secret_access_key=secret_access_key</code></pre>
- Substitua o <code>acess_key e o secret_access_key</code> pelos IDs existentes no arquivo de Acess Keys baixado anteriormente.
- Configure as variáveis: <pre><code>bucket_name=nome_do_bucket
path_to_search=caminho_do_objeto/nomeclatura
local_base_path=pasta_local_data</code></pre>