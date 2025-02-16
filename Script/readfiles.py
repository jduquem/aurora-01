import os

def menu():
    print("="*32 + "\n" + "=       MENÚ PRINCIPAL         =" + "\n" + "="*32)
    print("=" + " Este menú fue creado para    =")
    print("=" + " facilitarte la manera de     =")
    print("=" + " como utilizar la aplicación  =")
    print("="*32)
    print("=" + "   1. Opción 1" + "                =")
    print("=" + "   2. Opción 2" + "                =")
    print("=" + "   3. Opción 3" + "                =")
    print("=" + "   4. Salir" + "                   =")
    print("="*32)
    opcion = input("Seleccione una opción: ")
    return opcion

def listar_archivos_csv(ruta):
    for raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".csv"):
                print(archivo)

def main():
    ruta_carpeta = r"C:\Users\jose.duque\OneDrive - arus.com.co\Documentos\readFile"
    opcion = 100
    while opcion > 0:
        opcion = menu()
        if opcion == "1":
            listar_archivos_csv(ruta_carpeta)
        elif opcion == "2":
            print("Opción 2")
        elif opcion == "3":
            print("Opción 3")
        elif opcion == "4":
            print("Salir")
        else:
            print("Opción no válida") 

if __name__ == '__main__':
    main()