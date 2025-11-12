from flask import Flask

app = Flask(__name__)

# --- Rota Principal ---
@app.route("/")
def index():
    # Vamos adicionar um pouco de HTML!
    return """
    <h1>Bem-vindo ao Meu Mini-Site!</h1>
    <p>Use a barra de endereços para navegar:</p>
    <ul>
      <li>/sobre</li>
      <li>/contato</li>
    </ul>
    """

# --- ROTA NOVA: Sobre ---
@app.route("/sobre")
def sobre():
    return "<h1>Sobre Nós</h1><p>Esta é a página sobre... nós!</p>"

# --- ROTA NOVA: Contato ---
@app.route("/contato")
def contato():
    return "<h1>Contato</h1><p>Nosso email é professor@escola.com</p>"

if __name__ == "__main__":
    app.run(debug=True)# --- ROTA NOVA: Contato ---
@app.route("/contato")
def contato():
    return "<h1>Contato</h1><p>Nosso email é professor@escola.com</p>"

# --- ROTA DINÂMICA: Perfil ---
# O que estiver em <nome> será passado como argumento para a função perfil()
@app.route("/perfil/<nome>")
def perfil(nome):
    # Usamos um f-string para formatar o HTML com a variável
    return f"<h1>Olá, {nome}!</h1><p>Este é o seu perfil.</p>"


if __name__ == "__main__":
    app.run(debug=True)