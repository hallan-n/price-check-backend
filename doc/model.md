# Model User
O princial modelo de dados da API trata-se de uma classe.
###### Caminho até o modelo.
> app/models/user.py

Essa classe herda de BaseModel da lib pydantic.
###### Classe modelo.
> class User(BaseModel):

Para construir essa classe é necessário passar um dict.
###### Exemplo da classe construída.
> user = User(**user_dict):
