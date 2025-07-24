import os
import time
import pandas as pd
import numpy as np
from datetime import date as dt

class AnaliseDeGlosas:
    def __init__(self, xlsx, RegraNegocio, CamposObrigatorios):
        self.xlsx = pd.read_excel(xlsx)
        self.ColunaRegraNegocio = RegraNegocio
        self.ColunaCamposObrigatorios = CamposObrigatorios
        self.arquivo = f"{os.getcwd()}/glosas/"
        #Regras de Negocio
        self.ListaRegrasValidacaoNegocio = []
        self.glosasRegras = []
        #Campos Obrigatorios
        self.ListaCamposObrigatorios = []
        self.glosasCampos = []
        self.dataExtracao = dt.fromtimestamp(time.time())

    #pega os valores do txt e joga nas listas, pendente refatorar
    def PegarTXTparaLista(self):
        with open(self.arquivo + "ListaValidacaoDeNegocios.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            self.ListaRegrasValidacaoNegocio = [valor.strip() for valor in conteudo.split('\n')]

    def PegarTXTparaLista2(self):
        with open(self.arquivo + "glosasRegras.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            self.glosasRegras = [valor.strip() for valor in conteudo.split('\n')]

    def PegarTXTparaLista3(self):
        with open(self.arquivo + "ListaCamposObrigatorios.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            self.ListaCamposObrigatorios = [valor.strip() for valor in conteudo.split('\n')]

    def PegarTXTparaLista4(self):
        with open(self.arquivo + "glosasCampos.txt", 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            self.glosasCampos = [valor.strip() for valor in conteudo.split('\n')]

    # Verifica se existe a coluna de validação regras de negocio
    def VerificacaoRegraNegocio(self):
        # Analisa os tipos de glosas contidos em Validações de Regras Negócio
        try:
            #cria uma nova lista a partir de ListaRegrasValidacaoNegoci
            #retorna true se o texto for encontrada na coluna ColunaRegraNegocio
            regrasTipoGlosa = list(map(lambda glosa : self.xlsx[self.ColunaRegraNegocio].str.contains(glosa, na= False), self.ListaRegrasValidacaoNegocio))
            #faz a comparação entre as listas, a ordem importa
            return np.select(regrasTipoGlosa, self.glosasRegras, default = 'Glosa Não encontrada')
        except Exception as ex:
            print(f"\n                  ATENÇÃO - Verifique sua planilha.\n {ex} Ocorreu um erro inesperado:verifique se a coluna existe.\n")

    # Verifica se existe a coluna de validação de campo obrigatorio
    def verificacaoCampoObrigatorio(self):
        # Analisa os tipos de glosas contidos em Validações de Campos Obrigatorios
        try:
            #cria uma nova lista a partir de ListaRegrasValidacaoNegoci
            #retorna true se o texto for encontrada na coluna ColunaCamposObrigatorios
            regrasTipoGlosa = list(map(lambda glosa : self.xlsx[self.ColunaCamposObrigatorios].str.contains(glosa, na= False), self.ListaCamposObrigatorios))
            #faz a comparação entre as listas, a ordem importa
            return np.select(regrasTipoGlosa, self.glosasCampos, default = 'Glosa Não encontrada')
        except Exception as ex:
            print(f"\n                  ATENÇÃO - Verifique sua planilha.\n {ex} Ocorreu um erro inesperado:verifique se a coluna existe.\n")


    def analiseRetorno(self):
        total_linhas = len(self.xlsx)
        linhas_com_glosa = (self.xlsx['Tipo Glosa'] != 'Glosa Não encontrada').sum()
        linhas_sem_glosa = total_linhas - linhas_com_glosa

        print("\n" + "="*50 + " RESUMO DA ANÁLISE " + "="*50)
        print(f"\n✅ Total de linhas processadas: {total_linhas}")
        print(f"🔍 Linhas com glosa identificada: {linhas_com_glosa}")
        print(f"⚪ Linhas com glosas não identificada: {linhas_sem_glosa}\n")
        print("📊 Distribuição dos tipos de glosa:")
        print("\n" + "="*120 + "\n")
    
    def start(self):
        self.PegarTXTparaLista()
        self.PegarTXTparaLista2()
        self.PegarTXTparaLista3()
        self.PegarTXTparaLista4()
        time.sleep(1)

        self.xlsx['Tipo Glosa'] = np.where(
            self.xlsx['Validações de Regras Negócio'].str.fullmatch('-', na=False),
            self.verificacaoCampoObrigatorio(),
            self.VerificacaoRegraNegocio()
        )

        #Cria a pasta com a planilha
        os.makedirs(f"{os.getcwd()}/planilha/", exist_ok=True)
        os.chdir(f"{os.getcwd()}/planilha/")
        self.analiseRetorno()
        return self.xlsx.to_excel(f"Análise_Esus_{self.dataExtracao}.xlsx", engine='openpyxl', index=False, sheet_name='Principal')
        