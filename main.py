import streamlit as st
import pandas as pd
import altair as alt


def gerar_pdf():
    file_path = "Preços semestrais_AUTOMOTIVOS_2023.01.csv"

    # Carregue os dados do arquivo CSV usando pd.read_csv
    chart_data = pd.read_csv(file_path, delimiter=';')

    return chart_data  # Retorna o DataFrame lido do arquivo CSV

pf = gerar_pdf()


Colunas = ['Data da Coleta', 'Revenda', 'Estado - Sigla', 'Venda']

pf = pf[Colunas]


with st.sidebar:
    st.subheader('Revenda dos Combustível')
    st.subheader('Senção filtro')

    FRevenda = st.selectbox('Selecione Revenda', pf['Revenda'].unique())
    fEstado = st.selectbox('Selecionar Estados', pf['Estado - Sigla'].unique())

    # Filtrar o DataFrame com base nas seleções do usuário
    FdadosUsuario = pf[(pf['Revenda'] == FRevenda) & (pf['Estado - Sigla'] == fEstado)].reset_index(drop=True)


st.header("Preço dos Combustíveis")
st.markdown("Selecionou a Revenda: " + FRevenda)
st.markdown("Selecionou o Estado: " + fEstado)

chart = alt.Chart(FdadosUsuario).mark_line(point=True).encode(
    x='Data da Coleta',
    y='Venda',

)

st.altair_chart(chart, use_container_width=True)

