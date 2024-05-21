# simple-dynamodb-api
API to manage a DynamoDB Table

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mvm-sp/simple-dynamodb-api.git
   cd simple-dynamodb-api
   
### Optional: Adding Tests
You can add test scripts for each API function in the `tests` directory
# API Python para DynamoDB

Este projeto fornece uma API em Python para gerenciar uma tabela DynamoDB usando a biblioteca `boto3`. A API suporta a criação, leitura, atualização, exclusão e listagem de tutoriais.

## Estrutura do Projeto
````
simple-dynamodb-api/
├── api/
│ ├── init.py
│ ├── create_tutorial.py
│ ├── get_tutorial.py
│ ├── update_tutorial.py
│ ├── delete_tutorial.py
│ ├── list_tutorials.py
├── tests/
│ ├── init.py
│ ├── test_create_tutorial.py
│ ├── test_get_tutorial.py
│ ├── test_update_tutorial.py
│ ├── test_delete_tutorial.py
│ ├── test_list_tutorials.py
├── main.py
├── requirements.txt
└── README.md
````
Crie um ambiente virtual (opcional, mas recomendado):

````bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
````

Instale os pacotes necessários:

````bash
pip install -r requirements.txt

````

Configure as credenciais da AWS:

````bash
aws configure
````
Isso solicitará sua AWS Access Key, AWS Secret Key, região padrão e formato de saída.

Uso
Execute o script main.py para ver exemplos de uso da API:

````bash
python main.py
````

Isso executará os seguintes passos:

* Criar um novo tutorial.
* Buscar o tutorial criado por ID.
* Atualizar o tutorial.
* Listar todos os tutoriais.
* Excluir o tutorial.

# API

Endpoints da API
------------------------

* `create_tutorial(title, description, published`): Cria um novo tutorial.
* `get_tutorial(id)`: Recupera um tutorial pelo ID.
* `update_tutorial(id, title=None, description=None, published=None)`: Atualiza um tutorial pelo ID.
* `delete_tutorial(id)`: Exclui um tutorial pelo ID.
* `list_tutorials()`: Lista todos os tutoriais.


# Testes
----------------------
Para executar os testes, você pode criar scripts de teste no diretório tests. Os testes utilizam o framework unittest.

#### Executar Testes

Para executar todos os testes de uma vez:

````bash
python -m unittest discover -s tests
````

Ou para executar um teste específico:

````bash
python tests/test_create_tutorial.py
````