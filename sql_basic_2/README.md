# **Module 21 - Introduction SQL**

I created a table using the code:
```sql
CREATE EXTERNAL TABLE clientes(
    id BIGINT,
    idade BIGINT,
    sexo STRING,
    dependentes BIGINT,
    escolaridade STRING,
    tipo_cartao STRING,
    limite_credito DOUBLE,
    valor_transacao_12m DOUBLE,
    qtd_transacao_12m BIGINT
)
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  'separatorChar' = ',',
  'quoteChar' = '"',
  'escapeChar' = '\\'
)
STORED AS TEXTFILE
LOCATION 's3://jeduardo-m2-exercicio/';
```

In this exercise i learned:
- condition *WHERE*
- insert new data
- work with partitioned
- add new columns
- drop a table
