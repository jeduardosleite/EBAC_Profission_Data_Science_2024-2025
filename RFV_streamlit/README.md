# Exercise 1 - Module 31

## RFV - Recency, Frequency, Value
#### Customer segmentation

<img width="1017" height="578" alt="image" src="https://github.com/user-attachments/assets/25f82bad-8c6d-4375-90a5-ad5105cd3029" />

RFV stands for "**recency"**," ""**frequency"**," and ""**value"**" and is used to segment customers based on their purchasing behavior
and group them into similar groups. Using this type of grouping, we can conduct better-targeted marketing and CRM campaigns, aiding in content personalization and even customer retention.

For each customer, each of the following components should be calculated:

- ```Recency``` (R): Number of days since the last purchase
- ```Frequency``` (F): Total number of purchases in the period
- ```Value``` (V): Total amount spent on purchases in the period

## How to run locally

### 1) Clone the repository
Open **Anaconda Prompt** (or any terminal with conda available) and run:

```bash
git clone https://github.com/jeduardosleite/RFV_streamlit.git
cd RFV_streamlit
```

### 2) Create and activate a conda environment
```bash
conda create -n rfv_streamlit python=3.10 -y
conda activate rfv_streamlit
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the Streamlit app
```bash
streamlit run app_RFV.py
```

## Link to deploy
https://exercisemodule31.streamlit.app/


