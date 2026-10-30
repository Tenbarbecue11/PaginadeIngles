
import webbrowser
import os

# Ruta del archivo HTML
archivo = os.path.abspath("index.html")

# Abrir en el navegador predeterminado
webbrowser.open("file:///" + archivo.replace("\\", "/"))

print("Página web ejecutada correctamente.")
