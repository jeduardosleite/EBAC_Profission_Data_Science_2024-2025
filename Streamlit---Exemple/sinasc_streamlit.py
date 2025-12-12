import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set()  

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    st.pyplot(fig=plt)
    return None


st.set_page_config(page_title = 'Sinasc RO - 2019', 
                   page_icon = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ__uwtZnbxNRdhFe5UctTZc8ruHFiFTkVgrw&s',
                   layout='wide')


st.markdown("<h1 style='text-align: center; color: red;'> Análise Sinasc 2019 </h1>", unsafe_allow_html=True)

sinasc = pd.read_csv('SINASC_RO_2019.csv')

sinasc.DTNASC = pd.to_datetime(sinasc.DTNASC)

min_data = sinasc.DTNASC.min()
max_data = sinasc.DTNASC.max()

st.write(sinasc.DTNASC.max())
st.write(sinasc.DTNASC.min())

datas = pd.DataFrame(sinasc.DTNASC.unique(), columns=['DTNASC'])
datas.sort_values(by='DTNASC', inplace=True, ignore_index=True)
st.write(datas)

data_inicial = st.sidebar.date_input("Data inicial",
                           value = min_data,
                           min_value = min_data,
                           max_value = max_data)
data_final = st.sidebar.date_input("Data final",
                           value = max_data,
                           min_value = min_data,
                           max_value = max_data)

st.sidebar.write("Data inicial é: ", data_inicial)
st.sidebar.write("Data final é: ", data_final)


sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) &
                (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]

plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')
plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
