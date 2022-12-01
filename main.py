# Imports
from random import seed, randint

class Processo:
    def __init__(self, qtdPag):
        seed()
        self.id = randint(1000, 9999)
        self.qtdPag = qtdPag

def main():
    print("main")

if __name__ == "__main__":
    main()