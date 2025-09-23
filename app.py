from flask import Flask
import csv
import os
from flask import request

app = Flask(__name__)
# Nome do arquivo
ARQUIVO_CSV = 'estudante.csv'
#Função para salvar problema com dados etnico-racial
def salvar_estudante(nome, escola, bairro, etnia):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow(['nome', 'escola', 'bairro', 'etniapt'])
        escritor.writerow([nome, escola, bairro, etnia])

def ler_problemas():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados


@app.route("/")
def home():
    return "Bem-vindo ao sistema de cidades colaborativas!"

@app.route("/sobre")
def sobre():
    return "sobre"

@app.route("/cadastrar")
def cadastrar():
    salvar_estudante("Joana", "pública", "Xique-Xique", "Albina")
    return "Problema cadastrado com sucesso!"

@app.route("/cadastrar_form")
def cadastrar_form():
    nome = request.args.get("nome")
    problema = request.args.get("problema")
    bairro = request.args.get("bairro")
    etnia = request.args.get("etnia")

    salvar_estudante(nome, problema, bairro, etnia)
    return f"Problema cadastrado com sucesso: {nome} ({etnia}) {problema} ({bairro})"


if __name__ == "__main__":
    app.run(debug=True)
