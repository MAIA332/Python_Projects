import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import colorsys
import time
from sklearn.datasets import load_iris
import os

def distribuicao_idade(df):
    df.Age.hist(bins = 60)
    plt.xlabel("Idade")
    plt.ylabel("Número de Profissionais")
    plt.title("Distribuição de Idade")
    plt.show()

def pref_trb_idd(df):
    df_ageranges = df.copy()
    bins=[0, 20, 30, 40, 50, 60, 100]

    df_ageranges['AgeRanges'] = pd.cut(df_ageranges['Age'], bins, labels=["< 20", "20-30", "30-40", "40-50", "50-60", "< 60"]) 

    df2 = pd.crosstab(df_ageranges.AgeRanges, df_ageranges.JobPref).apply(lambda r: r/r.sum(), axis=1)

    # Definindo a quantidade
    num = len(df_ageranges.AgeRanges.value_counts().index)

    # Criando a lista de cores
    listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
    listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

    # Gráfico de Barras (Stacked)
    ax1 = df2.plot(kind = "bar", stacked = True, color = listaRGB, title = "Preferência de Trabalho por Idade")
    lines, labels = ax1.get_legend_handles_labels()
    ax1.legend(lines, labels, bbox_to_anchor = (1.51, 1))
    plt.show()

def exercicio_anl_explt():
    os.system('cls')
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df_clone = df
    print(len(df_clone))
    print(df_clone.head())
    print("=====================")
    print(list(df_clone))
    print("=====================")
    print(iris.target_names) #imprime o nome das variaveis target do datasset
    print(iris.target) #imprime as variaveis target como 0,1,2
    print("=====================")
    df_clone['spceie'] = pd.Categorical.from_codes(iris.target,iris.target_names)
    print(df_clone.head())# adiciona uma nova coluna no clone do meu dataframe, chamado especie, cujo valor é a funcao pd.Categorical.from_codes com os parametros iris.target e iris.target_names
    print("=====================")
    df_clone['target'] = iris.target
    print(df_clone.head())# adciona uma nova coluna no clone do dataframe, chamada target, cujo valor é iris.target
    features = df_clone.columns[:4]
    print(features)
    print(df_clone.groupby('target').mean().T)

exercicio_anl_explt()