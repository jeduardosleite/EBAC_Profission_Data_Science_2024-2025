[Linkedin](https://www.linkedin.com/in/jos%C3%A9-eduardo-souza-leite/)
---
<h1 align="center">Final Project – Explaining the code</h1>

<div align="center">
  <img width="1028" height="666" alt="image" src="https://github.com/user-attachments/assets/62b5e43b-a1e2-44f3-b46c-a348f5d0d9a8" />
</div>

---

Remembering that this project is a continuation of the last exercise. You can see in this link: https://github.com/ebac-data-science/Basic_Pycaret

---

## Before the setup

Before building *setup()*, I will treat the target imbalance with ```SMOTE```.

```python
X = df_dummie.drop(columns=['mau'])
y = df_dummie['mau']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=10)

smote = SMOTE(random_state=9221)  # here i used SMOTE
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
```

---

## PyCaret

### Setup

Criei um dataset concatenando o *X_train* e *y_train* balanceados na etapa anterior.

```python
s = setup(
    data=pd.concat([X_train_res, y_train_res], axis=1),  # new df
    target='mau',

    normalize=True,
    normalize_method='zscore',

    pca=False,

    remove_multicollinearity=True,
    multicollinearity_threshold=0.95,

    fix_imbalance=False,

    session_id=9221
)
```

<img width="325" height="725" alt="image" src="https://github.com/user-attachments/assets/e12e6074-a7ef-4c41-bf65-d52b7fd30a10" />

### Create Model

You have been asked to use a specific model, the *lightgbm*.

```
modelo_lightgbm = create_model('lightgbm')
```
<img width="454" height="42" alt="image" src="https://github.com/user-attachments/assets/81a0c0a9-3921-438c-bd03-e8446c5407c6" />


### Tune Model

First, I tested several parameters to find a suitable model. Then, I tuned this model with the *tune_model* function.

```
params_grid = {
    'n_estimators': (800, 4000),
    'learning_rate': (0.001, 0.03),
    'num_leaves': (15, 60),
    'min_child_samples': (10, 150),
    'max_depth': (-1, 20),
    'subsample': (0.6, 1.0),
    'colsample_bytree': (0.6, 1.0),
    'reg_alpha': (0.0, 1.0),
    'reg_lambda': (0.0, 1.0),
    'scale_pos_weight': (0.8, 1.2),
}

modelo_tunado = tune_model(
    modelo_lightgbm,
    search_library='scikit-optimize',
    search_algorithm='bayesian',
    custom_grid=params_grid,
    optimize='AUC',
    n_iter=10,
    fold=5,
    choose_better=True
)
```
<img width="442" height="42" alt="image" src="https://github.com/user-attachments/assets/8d83b93d-58d8-4560-983d-a06c57ca33b2" />

### Evaluate Model

See some graphs that, through evaluate_model, we can visualize with PyCaret.

#### ROC AUC
<img width="708" height="509" alt="image" src="https://github.com/user-attachments/assets/ed234b3b-6a7b-4b97-887d-7a8fb9c155d3" />

#### Confusion Matrix
<img width="782" height="520" alt="image" src="https://github.com/user-attachments/assets/4544578b-2871-42d8-8706-96fa0e296fe6" />

#### Feature Importance
<img width="842" height="471" alt="image" src="https://github.com/user-attachments/assets/2796071d-8501-4794-8211-3f8e476a2256" />

You can see more statistics and graphs:
<img width="1078" height="95" alt="image" src="https://github.com/user-attachments/assets/bf34d9c8-06de-4797-a322-703e9fe91995" />

---

## Pipeline

```python
pipe = Pipeline(steps=[
    ("valores_nulos", ValoresNulosTransformer()),
    ("padronizar_nomes", padroniza_nomes),
    ("padronizar_categoricas", padroniza_categoricas),
    ("cria_dummy", CriarDummyTransformer()),
    ("pca", PCA(n_components=5)),
    ("modelo", parametros_lightgbm)
])
```



```python
# valores_nulos
class ValoresNulosTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        return df

# cria_dummy
class CriarDummyTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True, dtype=int)
        return df
# pca
pca = PCA(n_components=5)

# padroniza_nomes
padroniza_nomes = FunctionTransformer(padronizar_nomes)

# padroniza_categoricas
padroniza_categoricas = FunctionTransformer(padronizar_categoricas)

# modelo
parametros_lightgbm = LGBMClassifier(
    boosting_type='gbdt',
    class_weight=None,
    colsample_bytree=1.0,
    importance_type='split',
    learning_rate=0.03,
    max_depth=-1,
    min_child_samples=10,
    min_child_weight=0.001,
    min_split_gain=0.0,
    n_estimators=4000,
    n_jobs=-1,
    num_leaves=60,
    objective=None,
    random_state=9221,
    reg_alpha=0.0,
    reg_lambda=0.0,
    subsample=1.0,
    subsample_for_bin=200000,
    subsample_freq=0,
    scale_pos_weight=0.8
)

```

<img width="245" height="317" alt="image" src="https://github.com/user-attachments/assets/53a96305-d009-4e56-bbbd-5be5ef3dea85" />

---

## Streamlit

I created an application in streamlit, where I tested this model. You can see my creation process on repository: 

[https://github.com/ebac-data-science/Final_project_streamlit/tree/main](https://github.com/ebac-data-science/Final_Project_EBAC)

And check my app:

https://ebac-jeduardo.streamlit.app/








