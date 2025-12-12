## **Module 21 - Introduction SQL**

### **Lesson 5**
Using functions:
- COUNT
- GROUP BY
- MIN
- MAX
- SUM
- AVG
- HAVING
----
After create a bucket in AWS S3, i wrote this code for make a table.
```sql
CREATE EXTERNAL TABLE heartattack (
  age INT,
  sex INT,
  cp INT,
  trtbps INT,
  chol INT,
  fbs INT,
  restecg INT,
  thatach INT,
  exng INT,
  oldpeak DOUBLE,
  slp INT,
  caa INT,
  thall INT,
  output INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://mod5-bucket-jeduardo/';
```
---
In this table there is null data, so I used this code in some queries.
```sql
WHERE "output" IS NOT NULL AND "output" IN (0,1)
```
