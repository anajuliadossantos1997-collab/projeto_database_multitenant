CREATE SCHEMA IF NOT EXISTS farmacia_central;

CREATE TABLE farmacia_central.produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    stock INT DEFAULT 0,
    preco NUMERIC(10,2)
);

CREATE TABLE farmacia_central.vendas (
    id SERIAL PRIMARY KEY,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor_total NUMERIC(10,2)
);

CREATE TABLESPACE tb_fasters LOCATION 'C:\dados_postgres\faster_datas';

CREATE SCHEMA IF NOT EXISTS store_tech;

CREATE TABLE store_tech.produtos (
	LIKE farmacia_central.produtos
	INCLUDING ALL
);
CREATE TABLE store_tech.vendas (
LIKE farmacia_central.vendas
INCLUDING ALL
);

ALTER TABLE farmacia_central.vendas
SET TABLESPACE tb_fasters;

ALTER TABLE farmacia_central.produtos
SET TABLESPACE tb_fasters;

ALTER TABLE store_tech.vendas
SET TABLESPACE tb_fasters;

ALTER TABLE store_tech.produtos
SET TABLESPACE tb_fasters;

CREATE TABLE public.tenants (
    id SERIAL PRIMARY KEY,
    nome_exibicao VARCHAR(100),
    schema_alvo VARCHAR(63) UNIQUE NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO public.tenants (nome_exibicao, schema_alvo) 
VALUES ('Farmácia Central', 'farmacia_central'), ('Tech Store', 'store_tech');
