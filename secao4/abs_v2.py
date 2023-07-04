import multiprocessing
import time


def processar():
    print("[", end="", flush=True)
    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)
    print("]", end="", flush=True)


def main():
    ex = multiprocessing.Process(target=processar)

    ex.start()
    ex.join()


if __name__ == "__main__":
    main()
