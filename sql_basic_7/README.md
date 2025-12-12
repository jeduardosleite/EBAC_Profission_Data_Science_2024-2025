# **Module 21 - Introduction SQL**

## **Lesson 7**

In this module i used concepts of:
- **SUBQUERIES**
- **PARTITIONED**
- **VIEWS**

### **Creating tables**

transacoes
```sql
CREATE EXTERNAL TABLE transacoes(
    id_cliente BIGINT,
    id_transacao BIGINT,
    data_compra DATE,
    valor DOUBLE,
    id_loja VARCHAR(25)
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://mod7-jeduardo/transacao/';
```
<br>

cliente
```sql
CREATE EXTERNAL TABLE cliente(
    id_cliente BIGINT,
    nome VARCHAR(25),
    data_compra DATE,
    valor_compra FLOAT,
    loja_cadastrada VARCHAR(25)
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://mod7-jeduardo/cliente/';
```
---
#### **Creating partitioned**

Firstly, i created seven bucket with csv archives:
- id_loja = magalu
- id_loja = giraffas
- id_loja = postosshell
- id_loja = subway
- id_loja = seveneleven
- id_loja = extra
- id_loja = shopee

Now, i created a new table
```sql
CREATE EXTERNAL TABLE transacoes_part(
    id_cliente BIGINT,
    id_transacoes BIGINT,
    valor DOUBLE)
    PARTITIONED BY (id_loja STRING)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://transacoes-partition-jeduardo/';
```

After that, I taught Athena.

```sql
MSCK REPAIR TABLE transacoes_part;
```
---
### **Tables for view**
Creating a new table.
```sql
CREATE VIEW transacoesv100 AS
SELECT
  id_cliente AS cliente,
  valor AS valor_compra,
  id_loja AS nome_loja
FROM transacoes
WHERE valor > 100;
```

```sql
CREATE VIEW clientevalor AS
SELECT
  id_cliente AS cliente,
  valor AS valor_compra
FROM transacoes
ORDER BY valor DESC
LIMIT 2;
```
