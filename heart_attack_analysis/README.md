# DATA ANALYSIS: HEART ATTACK


###**Objective 1:**
Understand the distribution of the variable 'sex' with the chance of heart attack.

- ***sex 0*** = female
- ***sex 1*** = male
- ***output 0*** = small chance of heart attack
- ***output 1*** = high chance of heart attack

This is exposed in query 1.

###**Objective 2:**
Analyze the maximum, minimum and average age in the 'sex - output' relationship.

This is exposed in query 2.

----

First I wrote the following code:
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
LOCATION 's3://mod5-bucket-heartattack/';
```
----

### **Query 1**
```sql
SELECT 
    COUNT(sex) AS Amount, 
    sex AS "Sex", 
    "output" AS heart_attack_chance,
    CASE 
       WHEN sex = 0 AND "output" = 0 THEN 'Female with less chance'
       WHEN sex = 1 AND "output" = 0 THEN 'Male with less chance'
       WHEN sex = 0 AND "output" = 1 THEN 'Female with more chance'
       WHEN sex = 1 AND "output" = 1 THEN 'Male with more chance'
    END AS sexo_describe
FROM heartattack
GROUP BY "output", sex
ORDER BY Amount DESC;
```
----
### Query 2

```sql
SELECT 
    MAX(age) AS max_age, 
    MIN(age) AS min_age, 
    ROUND(AVG(age)) AS median_age,
    CASE 
        WHEN "output" = 1 THEN 'More chance'
        ELSE 'Less chance'
    END AS heart_attack_chance,
    CASE 
        WHEN sex = 1 THEN 'Male'
        ELSE 'Female'
    END AS Sex
FROM heartattack
GROUP BY sex, "output";
```
