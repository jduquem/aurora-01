import os

def listar_archivos_csv(ruta):
    for raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".csv"):
                print(archivo)

ruta_carpeta = r"C:\Users\jose.duque\OneDrive - arus.com.co\Documentos\readFile"
listar_archivos_csv(ruta_carpeta)
