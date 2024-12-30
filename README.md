# Estudo de arquitetura Hexagonal

Usando Python e FastAPI, tenho o objetivo de destrinchar essa arquitetura
chegando a um código teste focado em estudo, a princípio.

## Requisitos

1. Será necessário ter o python >3.12

1. Ter o docker instalado na maquina, pois será necessário executar um comando para subir o banco

    ```bash
    > docker-compose up -d
    ```

## Orientações

1. Após o banco ficar "em pé", executar o script para criar as tabelas no banco postgress

    ```bash
    > wefood-fastapi\app\domain\ports\repository\create_tables.py
    ```
