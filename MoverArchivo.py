import getpass
from PIL import Image # python3 -m pip install pillow
import shutil
import os
import platform

sistema = platform.system()
if sistema.upper() == 'WINDOWS':
    p = input('punto de guardado (c, d, e): ')
    user = getpass.getuser() #nombre usuario
    carpetaImagenes = f"{p}:/{user}/Pictures/"
    carpetaMusica = f"{p}:/{user}/Music/"
    carpetaVideos = f"{p}:/{user}/Videos/"
    carpetaDocumentos = f"{p}:/{user}/Documents/"

elif sistema.upper() == 'LINUX' or sistema.upper() == 'DARWIN':
    carpetaImagenes = "~/Pictures/"
    carpetaMusica = "~/Music/"
    carpetaVideos = "~/Videos/"
    carpetaDocumentos = "~/Documents/"
def pwd() ->str:
    """retorna la ubicacion del archivo como el 'pwd' de linux"""
    ubicacion = os.path.abspath(os.getcwd())+"/"
    return ubicacion

def MoverArchivo(Direccion= pwd() ) ->None:
    if __name__ == "__main__":
        for archivo in os.listdir(Direccion):
            nombre, extension = os.path.splitext(Direccion + archivo)

            if extension in [".jpg", ".jpeg", ".png",".jfif"]:
                pintura = Image.open(Direccion + archivo)
                pintura.save(carpetaImagenes + "compressed_"+ archivo, optimize = True, quality = 60)
                os.remove(Direccion + archivo) #Borra imagen despues de que se guardara su forma compressed_
            # mueve archivos
            elif extension in [".mp3"]:
                shutil.move(Direccion + archivo, carpetaMusica + archivo)

            elif extension in [".mp4"]:
                shutil.move(Direccion + archivo, carpetaVideos + archivo)

            elif extension in [".pdf", ".docx", ".txt"]:
                shutil.move(Direccion + archivo, carpetaDocumentos + archivo)

            elif extension in [".iso",".exe"]:
                shutil.move(Direccion + archivo, carpetaDocumentos + archivo)

MoverArchivo()