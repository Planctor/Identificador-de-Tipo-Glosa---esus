from classes.AnaliseDeGlosas import AnaliseDeGlosas as ag
from classes.StartPrograma import StartPrograma as st
import time as tm

#start do programa
if __name__ == "__main__":
    start_time = tm.time()
    inicio = st()
    programa = ag('teste_relatorio.xlsx','Validações de Regras Negócio', 'Validações de Campos Obrigatórios')

    inicio.tela_inicio_simples()
    programa.start()
    print(f"Tempo de execução: {tm.time() - start_time:.2f} segundos")
    print("\n\nPrograma finalizado, com sucesso!\n")
