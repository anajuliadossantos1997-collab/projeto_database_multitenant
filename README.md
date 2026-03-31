## projeto_database_multitenant
Implementação de gerenciamento físico e lógico de um Banco Multi_tenant utilizando PostgreSQL

#Sobre o Projeto
Este repositório contém a infraestrutura de dados para um sistema que suporta múltiplos clientes (tenants) de forma isolada e performática.

#Conceitos Aplicados:
* Isolamento Lógico:** Uso de `SCHEMAS` independentes para cada cliente (`farmacia_central`, `store_tech`).
* Isolamento Físico:** Configuração de `TABLESPACE` para direcionar os dados para discos de alta performance.
* Padronização:** Criação de tabelas utilizando `LIKE` para garantir consistência estrutural.

#Como utilizar:
1. Certifique-se de ter o PostgreSQL instalado.
2. Crie a pasta física em seu sistema para o Tablespace (ex: `C:\dados_postgres\faster_datas`).
3. Execute o arquivo 'setup_db.sql'.

## 🐍 Automação com Python
O script `tenant_manager.py` permite escalar o sistema criando novos clientes automaticamente.

# Como rodar:
1. Instale as bibliotecas: `pip install python-dotenv psycopg2`
2. Crie um arquivo `.env` baseado no `.env.example`.
3. Execute o script: `python tenant_manager.py`
