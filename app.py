from flask import Flask

# Erstellt eine Flask-Instanz
app = Flask(__name__)

# Definiert die Route für die Startseite ("/")
@app.route('/')
def hello_world():
    # Gibt den Text zurück, der im Browser angezeigt werden soll
    return '<h1>Hello, World!</h1><p>Das ist Ihre erste Flask-Seite.</p>'

# Startet den Entwicklungsserver, wenn die Datei direkt ausgeführt wird
if __name__ == '__main__':
    app.run(debug=True)
