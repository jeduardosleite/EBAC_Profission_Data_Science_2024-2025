[My Linkedin](https://www.linkedin.com/in/jos%C3%A9-eduardo-souza-leite/)
- pip install -r requirements.txt

# Exercise 1 - Module 38

<img width="1108" height="714" alt="image" src="https://github.com/user-attachments/assets/ca95b274-fc1e-4a3d-93af-bd5a177b578d" />

## Dataset
| Variável               | Tipo       | Nulos | Valores Únicos | Papel      |
|------------------------|------------|-------|----------------|-------------|
| sexo                   | object     | 0     | 2              | covariable |
| posse_de_veiculo       | object     | 0     | 2              | covariable |
| posse_de_imovel        | object     | 0     | 2              | covariable |
| qtd_filhos             | int64      | 0     | 8              | covariable |
| tipo_renda             | object     | 0     | 5              | covariable |
| educacao               | object     | 0     | 5              | covariable |
| estado_civil           | object     | 0     | 5              | covariable |
| tipo_residencia        | object     | 0     | 6              | covariable |
| idade                  | int64      | 0     | 47             | covariable |
| tempo_emprego          | float64    | 25082 | 3004           | covariable |
| qt_pessoas_residencia  | float64    | 0     | 9              | covariable |
| renda                  | float64    | 0     | 46077          | covariable |
| mau                    | bool       | 0     | 2              | target     |

---

## Data Treatment

### NaN

```python
dataset = df_3_meses.copy()   # 3 last months
dataset['tempo_emprego'] = dataset['tempo_emprego'].fillna(dataset['tempo_emprego'].median())   # applying median in the NaN
dataset.drop(['data_ref', 'index'], axis=1, inplace=True)

df_modelagem = dataset.sample(frac=0.95, random_state=42)  # DF used for modeling
df_validacao = dataset.drop(df_modelagem.index)            # DF used for validation

df_modelagem.reset_index(inplace=True,
                 drop=True)
df_validacao.reset_index(inplace=True, drop=True)
```
In this exercise, we were asked to separate the last three months.

Null values ​​in the **employment_time** category were treated with the median, as this works best with outliers and large data sets.

But, in PyCaret, we can treat NaN on the setup. Even so, I decided to treat it first.

```python
s = setup(data = df_modelagem,
          target = 'mau',
          imputation_type = 'simple',
          numeric_imputation = 'median')
```

### Outliers
I will apply the Isolation Forest method to identify outliers using a threshold of 0.05, meaning the cutoff will be 5%.

> It is a decision tree–based algorithm that isolates anomalous observations in a dataset. It automatically identifies which records differ from the rest.

```python
s = setup(
    data=df_modelagem,          
    target='mau',

    # Null treatment
    numeric_imputation='median',
    categorical_imputation='mode',

    # Outlier removal
    remove_outliers=True,
    outliers_method='iforest',
    outliers_threshold=0.05,

    # Normalization
    normalize=True,
    normalize_method='zscore',

    # PCA
    pca=True,
    pca_method='linear',
    pca_components=5,

    # Multicollinearity
    remove_multicollinearity=True,
    multicollinearity_threshold=0.95,

    # Balancing
    fix_imbalance=True,  # SMOTE automático

    # Reproducibility
    session_id=9221
)
```
| Step                               | Action                                                                        |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| **Imputation**                     | Filled missing values with the median (numerical) and mode (categorical).     |
| **Normalization**                  | Standardized the data using *z-score* (mean = 0, standard deviation = 1).     |
| **Outlier Removal**                | Used the `iforest` (Isolation Forest) method to exclude 5% of extreme values. |
| **Multicollinearity Removal**      | Eliminated highly correlated variables (r > 0.95).                            |
| **Target Variable Balancing**      | Applied **SMOTE** to balance the “mau” target classes.                        |
| **PCA (Dimensionality Reduction)** | Generated 10 linear principal components.                                     |
| **Cross-Validation**               | Used StratifiedKFold with 10 splits, ensuring class balance across samples.   |


<img width="247" height="776" alt="image" src="https://github.com/user-attachments/assets/6cddf80f-5d59-4af3-9e4a-902b7c6ba1cd" />

---

## Compare Models

Firstly, i transformed the variable ```qtd_filhos``` into numeric.

```python
df_modelagem['qtd_filhos'] = df_modelagem['qtd_filhos'].astype(float)
```

```python
melhor_modelo = compare_models(fold=10)
```

<img width="721" height="489" alt="image" src="https://github.com/user-attachments/assets/89d36f51-692b-49ba-89ec-05016a9e2c3b" />

Despite this result, the exercise requested that I use the ```lightgbm``` model.

---

## Create Model

```python
modelo_lightgbm = create_model('lightgbm')
```

---

## Tune Model

```python
params_grid = {
  'n_estimators': [2000], # Increase the number of trees
  'learning_rate': [0.01, 0.025], # Decrease the learning rate
  'num_leaves': [20, 31, 40],
  'min_child_samples': [30, 50, 70],
}

modelo_tunado = tune_model(
    modelo_lightgbm,
    search_library='scikit-optimize', # Bayesian optimization methods
    search_algorithm='bayesian',
    custom_grid = params_grid 
)
```

<img width="439" height="427" alt="image" src="https://github.com/user-attachments/assets/954eada0-def2-4675-9f68-5d3fc4deaaec" />

---

## Pipeline

In this stage, i was created a pipeline containing these functions:
- null replacement 
- outlier removal 
- PCA 
- Creation of a dummy with at least one variable 


```python
X = df_dummie.drop(columns=['mau'])
y = df_dummie['mau']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=10)

# Replacing null values
def valores_nulos(df):
    df_filled = df.copy()
    for col in df_filled.columns:
        if df_filled[col].dtype in ['float64', 'int64']:
            df_filled[col].fillna(df_filled[col].median(), inplace=True)
        else:
            df_filled[col].fillna(df_filled[col].mode()[0], inplace=True)
    return df_filled

# Outlier removal
def remove_outliers(df, numeric_only=True, threshold=1.5):
    df_clean = df.copy()
    
    # Seleciona colunas numéricas
    if numeric_only:
        cols = df_clean.select_dtypes(include=['number']).columns
    else:
        cols = df_clean.columns
    
    for col in cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = ~((df_clean[col] < (Q1 - threshold * IQR)) | 
                 (df_clean[col] > (Q3 + threshold * IQR)))
        df_clean = df_clean[mask]
    
    return df_clean

# PCA to Linear dimensionality reduction
pca = PCA(n_components=5)

# Standard Scaler to normalize inputs (extra step)
scaler_pipe = StandardScaler()

# Dummy creation
def criar_dummy(df):
    df_copy = df.copy()
    # Seleciona apenas colunas categóricas (object ou category)
    colunas_cat = df_copy.select_dtypes(include=['object', 'category']).columns
    # Aplica get_dummies em todas as colunas categóricas
    df_copy = pd.get_dummies(df_copy, columns=colunas_cat, drop_first=True, dtype=int)
    return df_copy
```

In the application, I passed these parameters:

```python
pipe = Pipeline(steps=[("valor_nulo", valores_nulos(df_dummie)), 
                       ("remove_outlier", remove_outliers(df_dummie)), 
                       ("PCA(5)", pca),
                       ("Scaler", scaler_pipe),
                       ("Cria_dummy", criar_dummy(df_dummie))])
```

And saved:

```python
save_model(pipe,'Lightgbm Model')
```
