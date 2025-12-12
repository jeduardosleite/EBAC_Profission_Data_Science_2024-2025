# Module 21 - Exercise 3

Now i'll use concepts of:
- selection of unique values with ***SELECT DISTINCT***,
- ordenation with ***ORDER BY***,
- renaming columns in visualization with ***AS***,
- limitation of preview with ***LIMIT***
---
Firstly, i created a bucket and make a table.
```sql
CREATE TABLE EXTERNAL transacoes(
  id_cliente BIGINT,
  id_transacao BIGINT,
  valor FLOAT,
  id_loja STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  'separatorChar' = ',',
  'quoteChar' = '"',
  'escapeChar' = '\\'
)
STORED AS TEXTFILE
LOCATION 's3://mod3-jeduardo/';
```

After that I carried out 4 querys. The codes are described within the file.
