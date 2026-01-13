
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)  # cria o app primeiro

from rotas.rotas import *  # importa as rotas depois

if __name__ == '__main__':
    app.run(debug=True)
