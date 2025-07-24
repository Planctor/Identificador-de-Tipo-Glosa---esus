import os
import time

class StartPrograma:
    def __init__(self):
        pass

    def tela_inicio_simples(self):
        print("\n" + "="*100)
        print(" "*15 + "IDENTIFICADOR DE TIPO DE GLOSA")
        print("\n" + "="*100)
        print(" "*15 + "Tutorial:")
        print(" "*15 + " - Instale o Python no site - https://www.python.org/downloads/")
        print(" "*15 + " - Verifique se o pip está instalado corretamente")
        print(" "*15 + " - Para instalar as dependencias(Pandas e NumPY), use o comando pip install -r requirements.txt")
        print("="*100 + "\n")
        
        print("Carregando...")
        for i in range(101):
            print(f"\rProgresso: [{'#'*(i//2)}{' '*(50-(i//2))}] {i}%", end='')
            time.sleep(0.003)

        print("\n")
        input("Pressione enter para continuar")