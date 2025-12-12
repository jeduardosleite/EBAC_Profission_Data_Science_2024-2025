# Module 22 - Exercise 1

### Plotly and Melt

This practice refers to choosing 3 financial assets from Yahoo Finance to analyze and create a graph with plotly.

- Packs for work
```python
import plotly.express as px
from plotly import graph_objects
from IPython.display import FileLink, display
import yfinance as yf
import pandas as pd
import numpy as np
```
---
- Downloading the financial data
- Creating the amplitude
- Applying the melt function to transform wide large in long df 

```python
%%time

asset = ['AAPL', 'META', 'NVDA']
date_time = '2023-07-30'

asset_finance = yf.download(asset, start=date_time).reset_index()

amplitude = asset_finance['High'] - asset_finance['Low']
amplitude['Date'] = asset_finance['Date']
ampli = amplitude.reset_index()

df_to_melt = amplitude[['Date', 'META', 'AAPL', 'NVDA']]
df_long = df_to_melt.melt(
    id_vars='Date',          
    var_name='Company',       
    value_name='Amplitude'   
)
```
---

- Making the graphs plotly

```python
fig = px.line(
    df_long,
    x='Date',
    y='Amplitude',
    color='Company',
    template='plotly_white',
    title='Daily amplitude per asset'
)

fig.update_layout(
    title={
        'text': 'Daily amplitude per asset',
        'x': 0.5,              
        'xanchor': 'center'    
    }
)

fig.write_image("amplitude_por_ativo.jpg")
display(FileLink('amplitude_por_ativo.jpg', result_html_prefix="📥 Click here to download: "))

fig.show()
```

<img width="1088" height="242" alt="image" src="https://github.com/user-attachments/assets/6967d62c-cf2a-4340-a9a5-c663f1c48e02" />

---

- Archives to download
```python
std_company = (df_long.groupby('Company')['Amplitude']
               .std()
               .sort_values(ascending=False))

mean_company = (df_long.groupby('Company')['Amplitude']
                .mean()
                .sort_values(ascending=False))

std_company.to_csv('standard_deviation.csv', index=False)
mean_company.to_csv('average_deviation.csv', index=False)

display(FileLink('standard_deviation.csv', result_html_prefix="📥 Click here to download: "))
display(FileLink('average_deviation.csv', result_html_prefix="📥 Click here to download: "))
```

## Insights

**META** shares showed the highest volatility in the period analyzed, with *standard* and *average* deviations significantly higher than other assets.

This indicates that their prices fluctuated more intensely over the days, which may represent greater risk — and also greater potential return.
