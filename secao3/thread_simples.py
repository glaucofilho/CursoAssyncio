import threading
import time


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f"{n} {o_que}(s)...")
        time.sleep(1)
    pass


def main():
    th = threading.Thread(target=contar, args=("elefante", 10))
    th.start()
    print("Podemos fazer outras coisas no programa enquanto o thread vai executando...")
    print("Glauco " * 2)
    th.join()  # Avisa pra aguardar aqui a thread terminar de executar
    print("Pronto")


if __name__ == "__main__":
    main()
