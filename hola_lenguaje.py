import os


def main():
    nombre = os.getenv("USERNAME")
    lenguage = os.getenv("LANGUAGE")
    print(f"¡Hola, {nombre} desde GitHub!")
    print(f"¡lenguage, {lenguage} favorito!")

if __name__ == "__main__":
    main()
