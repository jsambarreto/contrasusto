#!.\.env python3

import tabula
from os import chdir, getcwd, listdir
import pandas as pd

from calculos.calcula_hora import calcula_hora
from calculos.calcula_salario import calcula_salario
from selecao_pasta.seleciona_pasta import seleciona_pasta

def carrega_base():
    caminho_pdf = seleciona_pasta()
    salarios=[] 
    arquivos=[]
    meses=[] 
    anos=[] 
    horas=[]

    #chdir('/content/drive/MyDrive/CONTRASUSTOS/PDF/')
    chdir(caminho_pdf)
    for c in listdir():
        if(c.endswith('13_1.PDF') or c.endswith('13_2.PDF')):
            continue
        else:
            arquivos.append(c)
    k=0
    for i in arquivos:
        print('Analisando o arquivo: %s'% i)
        print('Faltam %i de %i' % (len(arquivos)-k, len(arquivos)))
        k+=1
        dfs = tabula.read_pdf(i, stream=True, pages='1')
        mes, ano = dfs[0]['Unnamed: 0'][17].split('/')
        splitado = dfs[0]['Demonstrativo de Pagamento Mensal'][17].split(' ')
        meses.append(int(mes))
        anos.append(int(ano))
        try:
            try:
                horas.append(int(splitado[2]))
            
            except Exception as e:
                dfs3 = dfs[1]
                colunas = dfs3.columns
                aux = colunas[2].split(' ')
                horas.append(int(aux[1]))
        except Exception as e:
            dfs3 = dfs[2]
            colunas = dfs3.columns
            aux = colunas[2].split(' ')
            horas.append(int(aux[1]))
        for j in range(3,13):
            try:
                dfs2=dfs[j]
                salarios.append(float((dfs2['Base para FGTS'][0]).replace('.','').replace(',','.')))
            except: 
                continue
        base_salario = pd.DataFrame(list(zip(anos, meses, salarios, horas)), columns=['Ano','Mes','Salario', 'Hora'])
        base_salario_ordenada = base_salario.sort_values(['Ano','Mes'],ascending=True)
        base_salario_ordenada['horas_aulas'] = base_salario_ordenada[['Ano','Mes']].apply(lambda x: calcula_hora(x.Mes, x.Ano), axis=1)
        base_salario_ordenada['horas_calculadas'] = base_salario_ordenada[['Hora', 'horas_aulas']].apply(lambda x: calcula_salario(x.Hora, x.horas_aulas), axis=1)
        base_salario_ordenada['Diferenca']= round(base_salario_ordenada['horas_calculadas']-base_salario_ordenada['Salario'],2)
        salario_ano= base_salario_ordenada[['Ano','Diferenca']].groupby('Ano').sum('Diferenca')

    return salario_ano