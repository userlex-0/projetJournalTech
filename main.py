# voir notes.txt
from flask import Flask, render_template, url_for

app = Flask(__name__)    # on créer une instance de l'application web 'app'

@app.route('/')    # le serveur nous renvoie la page index.html lorsque nous sommes à l'url "/" ("https://projetjournaltech.userlex0.repl.co/") = page par défaut
def welcomePage():
  return render_template('welcome.html')

@app.route('/home') # decorateur nous permettant d'indiquer ce que le serveur doit faire lorsque nous entrons l'url indiqué (ici '/home')
def homePage():
  return render_template('home.html')

@app.route('/chat-gpt')
def chatGPT():
  return render_template('chatGPT.html')

@app.route('/pixel-war')
def pixelWar():
  return render_template('pixelWar.html')

@app.route('/cyber')
def cybersecurite():
  return render_template('cyber.html')

@app.route('/credits')
def credits():
  return render_template('credits.html')
  
if __name__ == '__main__':    # si ce fichier est le fichier principale (il n'est pas importé par un autre fichier) alors on lance le serveur
  app.run(debug=True, port=5555, host="0.0.0.0")