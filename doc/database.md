# Database: connection e persistence.
Database é um pacote responsável pela conexão com banco e persitencia de dados.
###### Caminho até os modulos do database.
> app/database/connection.py
> 
> app/database/persistence.py

## connection.py
Nesse modulo contém a conexão com o banco. Nesse módulo é usado uma lib para conexão com MySql..
###### Lib
> mysql-connector-pytho

Esse método retorna uma objeto de conexão com banco de dados, com ele é possível realizar as operações.
###### Método de conexão.
> def open_database():

## persistence.py
Nesse modulo contém todas as operações com o banco de dados. Esse método usa o objeto de retorno do *connection.py*.
###### Método de criação de usuário.
> def create_user(user: User):
