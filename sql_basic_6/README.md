# **Module 21 - Introduction SQL**

### **Lesson 6**

In this module i practiced basic functions of tables junctions.
- ***UNION***
- Junctions ***INNER*** and ***CROSS***
- Junctions ***LEFT*** and ***RIGHT***
----

#### **Tables**

##### transacoes
```sql
CREATE EXTERNAL TABLE transacoes (
    id_cliente BIGINT,
    id_transacao BIGINT,
    valor_compra DOUBLE,
    loja_cadastro STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://mod6-jeduardo/transacoes/';
```

##### cliente
```sql
CREATE EXTERNAL TABLE cliente (
    id_cliente BIGINT,
    nome STRING,
    valor_compra DOUBLE,
    loja_cadastro STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://mod6-jeduardo/cliente/';
```
---
