import datetime
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor
import asyncio

# 14,9 segundos
# 13,42 segundos
# 2,61 segundos
# 14,83 segundos
# 17,87 segundos


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    print(f"Realizando o processamento matemático de forma assincrona")
    el = asyncio.get_event_loop()
    inicio = datetime.datetime.now()
    # el.run_until_complete(computar(inicio=1, fim=50_000_000))
    tarefa1 = el.create_task(computar(10_000_000, 1))
    tarefa2 = el.create_task(computar(20_000_000, 10_000_000))
    tarefa3 = el.create_task(computar(30_000_000, 20_000_000))
    tarefa4 = el.create_task(computar(40_000_000, 30_000_000))
    tarefa5 = el.create_task(computar(50_000_000, 30_000_000))
    tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas)
    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")


if __name__ == "__main__":
    main()
