# Importando bibliotecas
import copy
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

#######################
# Configurações gerais da página
st.set_page_config(
    page_title="Melhores Filmes - IMBb",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded")

#######################
# Estilização CSS 
#with open('style.css') as fp:
#    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

#######################
# Carregamento de dados
df = pd.read_csv('data/imdb_top_1000.csv')


#######################
# Sidebar 
with st.sidebar:
    st.title('🎥 Melhores filmes IMDb')

    selected_years = st.slider('Selecione o período de tempo',1920,2020,(1920,2020))
    st.markdown("Autor: Vincenth Sabino - PDITA003")

#######################
# Formatação de números
def transform_string(text):
    try:
        text = ''.join(filter(lambda i: i if i.isdigit() else None,text))
    except TypeError: 
        return text if type(text) == float or type(text) == int else 0
    try:
        num = int(text)
    except ValueError:
        num = 0
    return num

def format_number(num):
    if abs(num) > 1000000000:
        if not num % 1000000000:
            return f'{num//1000000000} B'
        return f'U$ {round(num/1000000000,1)} B'
    if abs(num) > 1000000:
        if not num % 1000000:
            return f'U$ {num // 1000000} M'
        return f'U$ {round(num / 1000000, 1)} M'
    return f'U$ {num // 1000} K'

def remove_comma(text):
    text = str(text)
    text = ''.join(filter(lambda i: i if i.isdigit() else None,text))
    return text

#######################
# Controle de interatividade
def filter_df(input_df,input_years):
    df_filtered = copy.deepcopy(input_df)
    df_filtered['Released_Year'] = df_filtered['Released_Year'].apply(transform_string)

    mask = df_filtered['Released_Year'].isin(range(input_years[0],input_years[1]+1))
    df_filtered = df_filtered[mask]

    return df_filtered

######################
# Criando Plots

def genres_pizza(input_df, input_column, input_years):
    df_copy = filter_df(input_df,input_years)
    genre_counts = df_copy[input_column].value_counts()
    df_copy.loc[df_copy[input_column].isin(genre_counts[genre_counts< (len(df_copy)/40)].index),
                  input_column] = 'Outros gêneros'

    genre_counts = df_copy[input_column].value_counts()

    fig = px.pie(values=genre_counts,names=genre_counts.index)
    fig.update_layout(legend=dict(orientation='h'))
    return fig

def gross_metric(input_df,input_column,input_years):
    df_copy = filter_df(input_df,input_years)
    grosses = df_copy[input_column].apply(transform_string)
    
    total = grosses.sum()
    total = format_number(total)
    return total

def top10_table(input_df,input_years):
    df_copy = filter_df(input_df,input_years)
    filtered = df_copy.head(n=10)
    filtered['Released_Year'] = filtered['Released_Year'].apply(remove_comma)
    filtered = filtered.filter(items=['Series_Title','Released_Year','Genre','Director','Star1'])
    filtered.columns = ['Título','Ano','Gênero','Diretor','Ator principal']
    return filtered

def score_bar(input_df, input_label, input_column1, input_column2, input_years):
    df_copy = filter_df(input_df,input_years)
    top10 = df_copy.head(n=10)

    movies = top10[input_label]
    column1 = top10[input_column1]
    column2 = top10[input_column2]/10

    fig = go.Figure(data=[
        go.Bar(name='IMDb', x=movies, y=column1),
        go.Bar(name='MetaScore', x=movies, y=column2)
    ])
    return fig

def gross_bar(input_df, input_label, input_column1, input_years):
    df_copy = filter_df(input_df,input_years)
    top10 = df_copy.head(n=10)

    fig = px.bar(top10,x=input_label,y=input_column1,
                 labels={input_label:'',input_column1:'Lucro'})
    return fig


###########################
# Dashboard

# Primeira Linha
col = st.columns((1.5, 2.7), gap='small')

with col[0]:
    
    # Gráfico de pizza de gêneros
    with st.container():
        st.markdown('#### Gêneros presentes')
        p1 = genres_pizza(df,'Genre',selected_years)
        st.plotly_chart(p1, use_container_width=True)

    # Métrica do lucro total
    with st.container():
        metric = gross_metric(df,'Gross',selected_years)
        st.metric(label='#### Lucro total', value=metric)


with col[1]:

    # Tabela dos 10 melhores filmes
    with st.container():
        st.markdown('### Top 10 melhores filmes')
        table = top10_table(df,selected_years)
        st.dataframe(table, use_container_width=True, hide_index=True)


##################
# Segunda Linha
col = st.columns((2, 2), gap='medium')

with col[0]:
    
    # Histograma comparativo de pontuações
    with st.container():
        st.markdown('#### IMBb x Metascore')
        p1 = score_bar(df,'Series_Title','IMDB_Rating','Meta_score',selected_years)
        st.plotly_chart(p1, use_container_width=True)


with col[1]:

    # Lucro do top 10
    with st.container():
        st.markdown('#### Lucro do top 10')
        p2 = gross_bar(df,'Series_Title','Gross',selected_years)
        st.plotly_chart(p2, use_container_width=True)