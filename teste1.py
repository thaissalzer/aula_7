import streamlit as st
import pandas as pd

st.write("Sou servidor público!")


st.write("Ola,mundo!")

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


numero = st.slider('Selecione um número', min_value = 0, max_value = 100)
st.text("Seu número é " + str(numero))

servidores = {
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
}

df = pd.DataFrame(servidores)

st.write("Criando uma tabela!")

#tabelas interativas
st.write(df)

#inserindo um selectbox
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

#LEMBRETE: O formato de print é diferente do fstring de Python
st.write(f'Você selecionou:  {opcao}')

dfFiltrado = df.loc[df['nomeServidor'] == opcao]
st.write(dfFiltrado)


