# <p align="center">Manipulando objetos no AWS S3<br>Explorando Botocore</p>

<p align="center">
<img src="http://img.shields.io/static/v1?label=LICENCA&message=...&color=GREEN&style=for-the-badge"/>     
<img src="http://img.shields.io/static/v1?label=STATUS&message=N/A&color=GREEN&style=for-the-badge"/>
</p>

Este projeto consiste na criação de uma solução em Python para gerenciar objetos no Amazon S3, utilizando a biblioteca Botocore. A solução foi projetada para baixar objetos do S3 para a máquina local e, em seguida, remover esses objetos do S3. Antes de realizar o download, o sistema verifica se o objeto já existe em uma pasta de objetos processados, como parte de um processo separado de ETL. Se o objeto já tiver sido processado, não será baixado novamente e será removido do S3. Caso contrário, o objeto será baixado e, em seguida, removido do S3, oferecendo um gerenciamento eficiente e simplificado.

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
- Substitua o <code>acess_key</code> e o <code>secret_access_key</code> pelos IDs existentes no arquivo de <code>Acess Keys</code> baixado anteriormente.
- Configure as variáveis: <pre><code>bucket_name=nome_do_bucket
path_to_search=caminho_do_objeto/nomeclatura_do_objeto
local_base_path=pasta_local</code></pre>

### Conclusão

Após seguir esses passos, você estará pronto para automatizar o download e remoção dos objetos no S3.

## Considerações Finais

- A documentação pode não estar tão detalhada; talvez seja necessário um certo nível de conhecimento para adaptar o código.
- Este projeto representa uma refatoração de um script que desenvolvi na empresa onde trabalho atualmente, o MagaluBank. Enfrentamos "desafios" ao tentar baixar vários objetos usando o boto3, o que me levou a optar pelo botocore. 

<hr>

![Image](https://i.imgur.com/p4vnGAN.gif)