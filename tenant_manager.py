import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

class TenantManager:
    def __init__(self):
        self.conn_params = {
            "host": os.getenv("DB_HOST"),
            "database": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASS")
        }

    def criar_novo_tenant(self, nome_exibicao, schema_nome):
        """
        Faz o onboarding completo de um novo cliente.
        """
        conn = psycopg2.connect(**self.conn_params)
        conn.autocommit = True 
        cursor = conn.cursor()

        try:
            print(f"Iniciando criação do tenant: {nome_exibicao}...")


            cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(
                sql.Identifier(schema_nome)
            ))

            tabelas = ['produtos', 'vendas']
            for tabela in tabelas:
                query = sql.SQL("""
                    CREATE TABLE IF NOT EXISTS {schema}.{table} (
                        LIKE farmacia_central.{table} INCLUDING ALL
                    ) TABLESPACE tb_fasters
                """).format(
                    schema=sql.Identifier(schema_nome),
                    table=sql.Identifier(tabela)
                )
                cursor.execute(query)

            cursor.execute("""
                INSERT INTO public.tenants (nome_exibicao, schema_alvo) 
                VALUES (%s, %s) ON CONFLICT DO NOTHING
            """, (nome_exibicao, schema_nome))

            print(f"\033[32mSucesso! {nome_exibicao} está pronto e no disco tb_fasters.\033[0m")

        except Exception as e:
            print(f"\033[31mErro ao criar tenant: {e}\033[0m")
        finally:
            cursor.close()
            conn.close()

manager = TenantManager()

manager.criar_novo_tenant("PetShop AuAu", "petshop_auau")
