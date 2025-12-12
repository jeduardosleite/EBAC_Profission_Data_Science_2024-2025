# Module 22 - Exercise 2

### Candlestick

Academic activity to answer the questions:

1. Take a 90-day moving average of the adjusted closing values of the assets you chose
2. Using the ```rolling()``` function, calculate the standard deviation of these assets over time, using the same moving window as the item above
2. Create a line chart for the moving averages of your base assets
4. Create a line chart for standard deviations in a sliding window
5. Compare the two graphs you made with the one in the previous task. See if they point to similar conclusions regarding periods of greater asset volatility (variation).
---

Packs for work:
```python
from plotly import graph_objects
from IPython.display import FileLink, display
from plotly import graph_objects

import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
import numpy as np
```
---
I created two functions to automate both graphs.
```python
def plot_rolling(df, func, window=90, title='Rolling Média'):
    rolling_result = func(df.rolling(window))
    df_result = rolling_result.stack().reset_index()
    df_result.columns = ['Data', 'Ativo', 'Valor']

    fig = px.line(df_result,
                 x = 'Data',
                 y = 'Valor',
                 color = 'Ativo',
                 title = title)
    fig.show()
```

```python
def grafico_candlestick(database, sigla = 'sigla', titulo = 'título'):
    indicadores = ['Close', 'High', 'Low', 'Open', 'Volume']
    ativo = [sigla]*len(indicadores)
    
    colunas = list(zip(indicadores, ativo))
    
    df = database.loc['2025-06-01':,colunas]
    df.columns = indicadores
    
    candlestick = go.Candlestick(
        x = df.index,
        open = df['Open'],
        high = df['High'],
        low = df['Low'],
        close = df['Close'],
        name = sigla,
        showlegend = True)
    
    layout = go.Layout(
        title=dict(text=titulo, x=0.5),
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)')
    
    grafico = go.Figure(data=[candlestick], layout=layout)
    
    grafico.update_xaxes(showgrid = True,
                         gridwidth = 1,
                         gridcolor = 'LightGrey')
    grafico.update_yaxes(showgrid = True,
                         gridwidth = 1,
                         gridcolor = 'LightGrey')
    
    return grafico
```
