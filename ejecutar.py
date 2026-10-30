
import webbrowser
import os

# Ruta del archivo HTML
archivo = os.path.abspath("page.html")

# Abrir en el navegador predeterminado
webbrowser.open("file:///" + archivo.replace("\\", "/"))

print("Página web ejecutada correctamente.")
