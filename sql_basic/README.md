# Module 21 - Introduction SQL

First i performed a query indicated in the supporting material.

```sql
CREATE EXTERNAL TABLE clientes(
  id BIGINT,
  idade BIGINT,
  sexo STRING,
  dependentes BIGINT,
  escolaridade STRING,
  tipo_cartao STRING,
  limite_credito DOUBLE,
  valor_transacoes_12m DOUBLE,
  qtd_transacoes_12m BIGINT)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',', 'quoteChar' = '"', 'escapeChar' = '\\')
STORED AS TEXTFILE
LOCATION 's3://NAME/'
```

### Query 1
Select the entire table.
```sql
SELECT * FROM clientes;
```

### Query 2
The selected columns was *id*, *idade* and *limite_credito* to sort by male gender.
```sql
SELECT id, idade, limite_credito FROM clientes WHERE sexo = 'M' ORDER BY idade DESC;
```

### Query 3
Creating a new column called average_age_by_sex where I averaged the age by sex.
```sql
SELECT sexo, AVG(idade) AS "media_idade_por_sexo" FROM clientes GROUP BY sexo;
