
# ---------------------------
# Día 3 - Flask
# ---------------------------

# 📌 Requisitos:
# 1. Instalar virtualenv: pip install virtualenv​
# 2. Crear entorno virtual: python -m venv venv​   virtual enviroment
# 3. Activar entorno:​
#    - Mac source  venv\bin\activate
#    - Windows: venv\Scripts\activate 
# 4. Instalar Flask: pip install flask​
# 5. mkdir flask_crud_usuarios​
# 6. cd flask_crud_usuarios​
# 5. Ejecutar app: flask run


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Bienvenidos esta es mi primera aplicación con Flask!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    