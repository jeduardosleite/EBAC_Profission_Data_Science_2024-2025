# Module 21 - Exercise 4

Now i'll use concepts of:
- Selecting datas with ***AND***, ***OR***, ***IN*** and ***BETWEEN***
- Filter ***LIKE*** and ***WILDCARDS***
- Condition selection with ***CASE***, ***WHEN***, ***THEN***

----
But, firstly we need create a bucket in AWS S3 and make a table (*query_total*)
```sql
CREATE EXTERNAL TABLE transacoes(
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
LOCATION 's3://bucket-transacoes-jeduardo/';
```

After that I carried out 7 querys. The codes are described within the file.
