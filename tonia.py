from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import time
import os
import requests
from PIL import Image
import uuid
import numpy as np
import json


cabecario = '''
████████╗ ██████╗ ███╗   ██╗      ██╗ █████╗ 
╚══██╔══╝██╔═══██╗████╗  ██║      ██║██╔══██╗
   ██║   ██║   ██║██╔██╗ ██║█████╗██║███████║
   ██║   ██║   ██║██║╚██╗██║╚════╝██║██╔══██║
   ██║   ╚██████╔╝██║ ╚████║      ██║██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝      ╚═╝╚═╝  ╚═╝

      Módulo: API TONIA + MANUAL DE ERROS
                                             
'''


print(cabecario)
dialogos = []

app = Flask(__name__)
CORS(app)

def pesquisa(erro):
    erro = int(erro)
    
    f = open("json/transacao.json",)
    data = json.load(f)
    
    buscar = list(filter(lambda x:x["cod"]==erro,data))

    if(len(buscar)!= 0):
        print(buscar[0])
        response = {
            "statusCode":200,
            "resposta":buscar[0]["resposta"],
            "pergunta":buscar[0]["pergunta"]
        }
        
        
    else:
        print("não achei")
        response = {
            "statusCode":400,
            "resposta":""
        }
    
    return response

    
@app.route('/oraculo', methods=['GET', 'POST'])
def scan_file():
    if request.method == 'GET':
        erro = str(request.headers.get('erro'))
        search = pesquisa(erro)
        
        return search

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)