Integrantes del proyecto: Juan Pedro Suñer 

# Instalación de Python 3.11 

Este archivo README proporciona instrucciones para instalar Python 3.11 y configurar streamlit en tu sistema.

## Instalación de Python 3.11

### Windows

1. Visita el [sitio web oficial de Python](https://www.python.org/downloads/) y descarga el instalador de Python 3.11 para Windows.
2. Ejecuta el instalador descargado y asegúrate de marcar la opción "Add Python 3.11 to PATH" durante la instalación.
3. Sigue las instrucciones en pantalla para completar la instalación.

### macOS

1. Puedes instalar Python 3.11 usando Homebrew ejecutando el siguiente comando en la terminal:
   ```bash
   brew install python@3.11

### Linux (Ubuntu)
    
1. Abre una terminal y ejecuta los siguientes comandos para instalar Python 3.11:
      sudo apt update
      sudo apt install python3.11
 
# Instalación y ejecución de streamlit 

1. Abre una terminal y ejecuta los siguientes comandos dentro del directorio del proyecto:
    python3 -m venv env 

# comdandos en diferentes S.O

### Windows

    env\Scripts\activate
    pip install -r requirements.txt
    streamlit run "app\main.py"

### macOs o Linux(Ubuntu)

    env\bin\activate    
    pip install -r requirements.txt
    streamlit run "app\main.py"



