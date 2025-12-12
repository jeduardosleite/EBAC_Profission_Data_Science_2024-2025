[My Linkedin](https://www.linkedin.com/in/jos%C3%A9-eduardo-souza-leite/)
- pip install -r requirements.txt

# Exercise 2 - Module 36

<img width="630" height="449" alt="image" src="https://github.com/user-attachments/assets/71c2128c-0185-42d9-a2b1-5d024b583c93" />


## Dataset

This database comes from the **AMABiliDados** project and contains data from São Paulo tax receipts registered for automatic donation to AMA, the Association of Friends of Autistic People.

*Nota Fiscal Paulista* is a consumer incentive program from the São Paulo state government, which returns a portion of the ICMS tax whenever you request that your CPF be included on the receipt. 
Under this program, taxpayers can direct their credits to an NGO, and when they do so, whenever the registered consumer makes a purchase, the credits from receipts issued by the same unidentified establishment (receipts without a CPF) are "dragged" to the NGO in the form of a donation.

- [Click here](https://www.ama.org.br/site/) if you want to learn more about AMA.
- [Click here](https://doacao1.ama.org.br/sitenfp) if you want to learn how you can become an NFP donor.

This database contains data on tax invoices that have allocated their credits to AMA. Its fields are described below:

|Field|Description|
|:-|:-|
|CNPJ emit.| CNPJ of the invoice issuer|
|Emitente| Business name of the invoice issuer|
|No.| Invoice Number|
|Data Emissão| Invoice issuance data|
|Valor NF| Invoice Amount|
|Data Registro| Registration data in the NFP system|
|Créditos| Credit Amount (donation)|
|Situação do Crédito| Whether the credit has already been paid, is being processed, etc.|
|Ano| Year of invoice issuance|
|Semestre| Semester of invoice issuance|
|Retorno| Credit amount divided by the invoice amount|
|flag_credito| Indicates whether the invoice has positive credit|
|categoria| Note categorization |

---

## Objective

Continuation of the previous exercise, where i explored IV and woe concepts. But this time, I'll do a more in-depth analysis.
First, I'll create time variables for:
- day of the week,
- weekend dummy,
- day of the month,
- quarter,
- year.

```python
# Criando colunas com os respectivos dias da semana
df['Dia_da_semana'] = df['Data Registro'].dt.dayofweek

# Referente a semana do ano, sendo de 1 até 53
df['semana'] = df['Data Registro'].dt.isocalendar().week

# Referente ao nome do mês, de 1 a 12
df['mes'] = df['Data Registro'].dt.month

# Referente ao trimestre do respectivo mês, sendo de 1 até 4
df['trimestre'] = df['Data Registro'].dt.quarter

#Referente ao ano, de 2017 até 2022
df['ano'] = df['Data Registro'].dt.year
```

Then I created quantiles for 'Valor NF' at 5, 10, 20 and 50.

```python
# Criar as variáveis por quantís de 5, 10, 20 e 50
for q in [5, 10, 20, 50]:
    df[f'ValorNF_q{q}'] = pd.qcut(df['Valor NF'], q, duplicates='drop')
```

---

## Metadado

I created a metadata file to facilitate the calculation of IV and WOE.
1) I excluded the variables that did not explain the results;
2) I made a copy of the original df;
3) I dropped the unwanted columns;
4) I converted the "categoria" variable to dummies;
5) I converted the quartiles to midpoints, since qcut does not recognize strings;
6) I created the metadata with the column dtypes;
7) I assigned roles to each variable, as follows:
- Explanatory: explanatory variables;
- Response: target variable;
8) I added a quantity column with the unique value of each variable.

```python
# Selecionei as colunas que, para esta análise, não trarão informações relevantes.
colunas_deletadas = ['CNPJ emit.', 'Emitente', 'No.', 'Data Registro', 'Data Emissão', 'Situação do Crédito']
                     
# Cópia do df original
new_df = df.copy()

# Função drop para excluir as colunas
new_df.drop(columns=colunas_deletadas, inplace=True)

# Transformando a categoria em dummies para analisar posteriormente
new_df = pd.get_dummies(new_df, columns=['categoria', ], dtype=int)

# Convertendo os quartis de NF para ponto médio, evita erros no loop do "popular metadados", visto que o qcut não identifica strings.
for col in ['ValorNF_q5', 'ValorNF_q10', 'ValorNF_q20', 'ValorNF_q50']:
    new_df[col] = new_df[col].apply(lambda x: x.mid if isinstance(x, pd.Interval) else np.nan)

# Criação do metadados através do new_df, pegando apenas o dtypes de cada coluna
metadados = pd.DataFrame({'dtypes':new_df.dtypes})

# Atribuindo papéis, ou seja, rótulos a cada variável. Resposta e Explicativas
metadados['papel'] = 'Explicativa'
metadados.loc['flag_credito', 'papel'] = 'Resposta'

# Atribuindo a quantidade de cada valor a cada
metadados['quantidade'] = new_df.nunique()
```

<img width="386" height="761" alt="image" src="https://github.com/user-attachments/assets/c8fabac6-83e2-49b5-bf71-c53d40bed688" />

## Problems with infinite values

While performing the activity, I encountered problems with infinite values ​​resulting from dividing an explanatory variable by zero. To resolve this discrepancy, I used the concept of ```epsilon```.

```epsilon``` is often used to avoid division-by-zero errors or logarithms of zero. The idea is to replace the assumed zero value with an *extremely small*, practically insignificant number.

$$
1 \times 10^{-6}
$$

```Python
tab['woe'] = np.log((tab['pct_evento'] + eps) / (tab['pct_n_evento'] + eps))
```

```epsilon``` was used in the WOE calculation precisely to avoid log(0) or 1/0. This ensures that if in some group (or range) the number of events is 0, the calculation does not break and the logarithm is not infinite.

```python
for var in metadados[metadados['papel'] == 'Explicativa'].index:
    try:
        serie = new_df[var]
        if pd.api.types.is_numeric_dtype(serie):
            if metadados.loc[var, 'quantidade'] > 5:
                metadados.loc[var, 'iv'] = IV(pd.qcut(serie, 5, duplicates='drop'),
                                              new_df['flag_credito'])
            else:
                metadados.loc[var, 'iv'] = IV(serie, new_df['flag_credito'])
        elif isinstance(serie.dtype, pd.CategoricalDtype):
            metadados.loc[var, 'iv'] = IV(serie, new_df['flag_credito'])
        else:
            print(f"Coluna ignorada (tipo não tratado): {var}")
            metadados.loc[var, 'iv'] = np.nan
    except Exception as e:
        print(f"Erro em {var}: {e}")
        metadados.loc[var, 'iv'] = np.nan

metadados
```

<img width="460" height="757" alt="image" src="https://github.com/user-attachments/assets/6a64cb65-4639-45f2-98f6-368e8e59ebf0" />

---

## Conclusion

### Which variables seem to show greater discriminative power according to IV?

|Range|Predictive Power|
|:-|:-|
|0 to 0.02| Useless |
|0.02 to 0.1| Weak |
|0.1 to 0.3| Medium |
|0.3 to 0.5| Strong |
|0.5 or more| Suspiciously high |

The variables ```Retorno``` and ```Créditos``` show **extremely high** values, which are considered suspicious according to Siddiqi’s table.  
This may indicate two situations:  
1) Data leakage  
2) The target variable is embedded within the feature  

The variable ```categoria_Alimentos``` has a *moderately high* predictive power, reaching almost *0.3*.

The categorized variables ```ValorNF_50```, ```ValorNF_20```, and ```ValorNF_10``` have **medium** power, ranging between *0.15* and *0.10*.

---

### When continuous variables are categorized, is there any relationship between the number of categories and IV?

As the number of categories for ```ValorNF``` increases, the **IV grows**.  
This happens because finer partitioning increases the granularity of the information — in other words, the model becomes better at capturing differences between groups.

---

## Number of Notes per Quarter

<img width="717" height="691" alt="image" src="https://github.com/user-attachments/assets/8c01dd71-3358-4100-960d-2ebff2216d1e" />

We noticed that 2018 had the highest number of notes. Events that occurred this year may have influenced this, such as the Venezuelan migration crisis, economic instability, the return of measles, etc.
We can also conclude that, due to seasonality, holidays, and other factors, the last two quarters have a higher number.

---

## Category and Quarter

<img width="453" height="554" alt="image" src="https://github.com/user-attachments/assets/be39f25c-b491-46e1-ab1b-37fcd9ffc04e" />

To evaluate the WOE and IV of the categories over time, I created another metadata (using the same logic as the previous one), but filtering for the year 2020 onward.

With this, I was able to answer:

#### Which categories appear to have the highest proportion of notes with returns greater than zero
Among the categories, I highlight ```Varejo``` with an average predictive power, value of *0.111*, ```Alimentos``` and ```Restaurantes``` with weak predictive power with, respectively, *0.0664* and *0.0457*. The other categories have a smaller impact, making them useless in this context.

#### Are these differences stable over time?
There are no significant variations by quarter or year, demonstrating that the behavior of ```flag_credito``` is stable over time for the 2020-2022 period.
The **IV** remains very low throughout the period, which explains the temporal stability in the proportion of notes with positive credit (1).
Specifically for 2022, I noticed a steep decline, but I assume this is due to a lack of data or a smaller volume.
