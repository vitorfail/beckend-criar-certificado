from base64 import encodebytes
from statistics import mode
from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageFont, ImageDraw
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def criar():
  if request.json == None or request.json == False:
    return 'Não há nehum parâmetro. Por favor envie a descriçaõ da imagem'
  else:
    tipo1 = {
      "font_nome": r"font/cac_champagne.ttf",
      "font_size_nome": 276,
      "font_assinaturas": r"font/BODONI BK BT BOOK.TTF",
      "font_size_assinaturas": 110,
      "font_conteudo": r"font/BauerBodoniStd-Roman.ttf",
      "font_size_conteudo": 49,
      "coord_nome": (873, 1160),
      "coord_diretor": (950, 1850),
      "coord_reitor": (2350, 1850),
      "coor_data": (2350, 1850),
      "coor_conteudo": (880, 1400),
      "imagem": r'certificado1.jpg'
    }
    tipo2 = {
      "font_nome": r"font/cac_champagne.ttf",
      "font_size_nome": 276,
      "font_assinaturas": r"font/BODONI BK BT BOOK.TTF",
      "font_size_assinaturas": 110,
      "font_conteudo": r"font/BauerBodoniStd-Roman.ttf",
      "font_size_conteudo": 49,
      "coord_nome": (873, 1110),
      "coord_diretor": (920, 1850),
      "coord_reitor": (2350, 1850),
      "coor_data": (2361, 1850),
      "coor_conteudo": (880, 1400),
      "imagem": r'certificado2.jpg'
    }
    tipo3 = {
      "font_nome": r"font/cac_champagne.ttf",
      "font_size_nome": 276,
      "font_assinaturas": r"font/BODONI BK BT BOOK.TTF",
      "font_size_assinaturas": 110,
      "font_conteudo": r"font/BauerBodoniStd-Roman.ttf",
      "font_size_conteudo": 49,
      "coord_nome": (873, 1110),
      "coord_diretor": (1100, 1850),
      "coord_reitor": (2350, 1850),
      "coor_data": (1673, 1850),
      "coor_conteudo": (880, 1400),
      "imagem": r'certificado3.jpg'
    }
    tipo4 = {
        "font_nome": r"font/cac_champagne.ttf",
        "font_size_nome": 276,
        "font_assinaturas": r"font/BODONI BK BT BOOK.TTF",
        "font_size_assinaturas": 110,
        "font_conteudo": r"font/Rubik.ttf",
        "font_size_conteudo": 49,
        "coord_nome": (873, 1110),
        "coord_diretor": (1049, 2120),
        "coord_reitor": (2350, 1850),
        "coor_data": (2280, 2120),
        "coor_conteudo": (1013, 1570),
        "imagem": r'certificado4.jpg'
      }
    def tipo(t):
      if t == 'tipo1':
        return tipo1
      if t == 'tipo2':
        return tipo2
      if t == 'tipo3':
        return tipo3
      if t == 'tipo4':
        return tipo4
    dados = request.json
    result = tipo(dados['tipo'])
    coord_nome = result["coord_nome"]
    coord_diretor = result["coord_diretor"]
    coord_reitor = result["coord_reitor"]
    coor_data = result["coor_data"]
    coor_conteudo = result["coor_conteudo"]
    imagem = Image.open(result["imagem"])
    font_nome = ImageFont.truetype(result["font_nome"], result["font_size_nome"])
    font_assinatura = ImageFont.truetype(result["font_assinaturas"], result["font_size_assinaturas"])
    font_conteudo = ImageFont.truetype(result["font_conteudo"], result["font_size_conteudo"])

    nome = dados['nome']
    diretor = dados['diretor']
    reitor = " "
    data = dados['data']
    conteudo = dados['conteudo']

    rgb_azul = (dados['rgb'][0], dados['rgb'][1], dados['rgb'][2])
    desenho = ImageDraw.Draw(imagem)
    w1, h1 = font_nome.getsize(nome)
    W1, H1 = coord_nome
    W2, H2 = font_assinatura.getsize(dados['diretor'])
    w2, h2 = coord_diretor
    w3, h3 = coord_reitor
    w4, h4 = coor_data
    W4, H4 = font_assinatura.getsize(dados['data'])
    w5, h5 = coor_conteudo
    w, h = desenho.textsize(nome)
    desenho.text(((imagem.width-w1)/2, H1), nome, font=font_nome, fill=rgb_azul)
    desenho.text((w2 - (W2/2), h2 - h), diretor, font=font_assinatura, fill=rgb_azul)
    desenho.text((w3 - w, h3 - h), reitor, font=font_assinatura, fill=rgb_azul)
    desenho.text((w4, h4 - h), data, font=font_assinatura, fill=rgb_azul)
    desenho.text((w5 - w, h5 - h), conteudo, font=font_conteudo, fill=rgb_azul)

    imagem.save(f'{nome}.jpg')
    filename = nome + '.jpg'
    @app.after_request
    def delete(response):
      os.remove('./'+filename)
      return response   
    return send_file(filename, mimetype='image/jpg')      
     

@app.route('/', methods=['GET'])
def responder():
  return 'Não usamos esse método'

if __name__ == '__main__': 
  app.run()
