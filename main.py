from warnings import catch_warnings
import streamlit as st
import numpy as np
from PIL import Image
from pickle import load
import pandas as pd

import load_model as lm

# Carregando os modelos pelo módulo
X_scaler, minmax_scaler, X_scaler_names, model = lm.load_dados()

# Gerando a interface com streamlit
image = Image.open('imagem/churn.jpeg')

# Interface
st.title('Predição de Churn')
st.write('Aplicativo personalizado para predição de Churn da empresa de telecomunições.')
st.image(image)

st.sidebar.header('Informe os dados do cliente abaixo.')

sexo = st.sidebar.selectbox('Sexo', ('Female', 'Male'), help='Sexo do cliente')
senior_citizen = st.sidebar.selectbox('Senior Citizen', ('No', 'Yes'), help='Cliente tem mais de 65 anos?')
partner = st.sidebar.selectbox('Partner', ('No', 'Yes'), help='Cliente possui parceiro?')
dependents = st.sidebar.selectbox('Dependents', ('No', 'Yes'), help='Cliente possui dependentes?')
phone_service = st.sidebar.selectbox('Phone Service', ('No', 'Yes', 'No phone service'), help='Cliente possui serviço telefônico?')
multiple_lines = st.sidebar.selectbox('Multiple Lines', ('No', 'Yes'), help='Cliente possui múltiplas linhas telefônicas?')
internet_service = st.sidebar.selectbox('Internet Service', ('No', 'DSL', 'Fiber optic'), help='Tipo de serviço de internet')
online_security = st.sidebar.selectbox('Online Security', ('No', 'No internet service', 'Yes'), help='Cliente possui pacote de segurança oline?')
online_backup = st.sidebar.selectbox('Online Backup', ('No', 'No internet service', 'Yes'), help='Cliente possui pacote de backup online?')
device_protection = st.sidebar.selectbox('Device Protection', ('No', 'No internet service', 'Yes'), help='Cliente possui pacote de preoteção de dispositivo?')
tech_support = st.sidebar.selectbox('Tech Support', ('No', 'No internet service', 'Yes'), help='Cliente possui pacote de suporte técnico?')
streaming_TV = st.sidebar.selectbox('Streaming TV', ('No', 'No internet service', 'Yes'), help='Cliente possui serviço de streaming de TV?')
streaming_movies = st.sidebar.selectbox('Streaming Movies', ('No', 'No internet service', 'Yes'), help='Cliente possui serviço de streaming de filmes?')
contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'), help='Tipo de contrato')
paperless_billing = st.sidebar.selectbox('Paperless Billing', ('No', 'Yes'), help='Cliente possui pagamento por meio impresso?')
payment_method = st.sidebar.selectbox('Payment Method', ('Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'), help='Método de pagamento')
tenure = st.sidebar.number_input(label='Tenure', step=0.01, min_value=0.0, help='Tempo de contrato do cliente')
charges_monthly = st.sidebar.number_input(label='Charges Monthly', step=0.01, min_value=0.0, help='Gasto mensal do cliente')
charges_total = st.sidebar.number_input(label='Charges_Total', step=0.01, min_value=0.0, help='Gasto total do cliente')

# Tentativa de ler os dados
try:
    # Ler parte categórica de entrada
    X = pd.DataFrame({'Gender':sexo, 'SeniorCitizen':senior_citizen, 'Partner':partner, 'Dependents':dependents, 'PhoneService':phone_service, 'MultipleLines':multiple_lines,
            'InternetService':internet_service, 'OnlineSecurity':online_security, 'OnlineBackup':online_backup, 'DeviceProtection':device_protection, 'TechSupport':tech_support,
            'StreamingTV':streaming_TV, 'StreamingMovies':streaming_movies, 'Contract':contract, 'PaperlessBilling':paperless_billing, 'PaymentMethod':payment_method}, index=[0])

    # Transformar parte categórica da entrada
    X = pd.DataFrame(X_scaler.transform(X), columns=X_scaler_names[0:-3])

    # Concatenar dados numéricos
    X['Tenure'] = tenure
    X['ChargesMonthly'] = charges_monthly
    X['ChargesTotal'] = charges_total

    # Transformar os dados com o transformador do mínimo-máximo
    X = pd.DataFrame(minmax_scaler.transform(X), columns=X_scaler_names)
except:
    st.write('Algo aconteceu na leitura dos dados. Tente novamente!')

# Tentativa de realizar a predição
try:
    # Botão de predição
    if st.button('Realizar predição'):
        pred = model.predict(X)
        pred_proba = model.predict_proba(X)
        if (pred[0] == 0):
            st.write('O cliente não deixará o plano. :sunglasses:')
        else:
            st.write(f'Atenção. O cliente deixará o plano com {pred_proba[0][1]*100:.2f}% de certeza.')
    else:
        st.write('Aguardando predição')
except:
    st.write('Algo aconteceu na predição. Tente novamente!')
