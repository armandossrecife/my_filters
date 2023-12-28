import os
import time
from urllib.parse import urlparse
from entidades import Download, Imagem
from filtros import BlackAndWhiteFilter, GrayscaleFilter, EdgesFilter

class Util:
  def extrair_nome_extensao_url(self,url):
    # Faz o parse da URL
    parsed_url = urlparse(url)
    # Obtém o caminho do arquivo
    caminho_arquivo = parsed_url.path
    # Extrai o nome do arquivo e a extensão
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    return nome_arquivo, extensao

  def wait_for_file(self,file_path, interval=1):
      print('Aguarde...')
      while not os.path.exists(file_path):
        time.sleep(interval)
        interval = interval + 1
        print(".", end=" ")

class ManipulaImagem:
  def __init__(self, utilidades):
    self.utilidades = utilidades

  def cria_imagem(self, minha_url):
    imagem_teste = None
    try:
      print(f'URL: {minha_url}')
      nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
      arquivo = nome_arquivo + extensao_arquivo
      print(f'Arquivo: {arquivo}')
      meu_download = Download(url=minha_url, path_arquivo=arquivo)
      print(f'Inicia download...')
      meu_download.executa()
      print(f'Download concluído!')
      self.utilidades.wait_for_file(arquivo)
      imagem_teste = Imagem(id=1, nome_arquivo=arquivo, path_arquivo=arquivo)
      print(imagem_teste)
    except Exception as ex: 
      print(f'Erro: {str(ex)}')
      raise Exception('Erro no Download')
    return imagem_teste.conteudo()

  def aplica_filtro_grayscale(self,minha_imagem, nome):
    print('Aplicando filtro grayscale...')
    # Create an instance of the GrayscaleFilter
    grayscale_filter = GrayscaleFilter()
    # Apply the filter to the image
    filtered_image_grayscale = grayscale_filter.apply_filter(minha_imagem)
    # Save the filtered image
    nome = nome + '_greyscale.jpg'
    filtered_image_grayscale.save(nome)
    print(f'Filtro grayscale aplicado com sucesso! Arquivo salvo em {nome}')

  def aplica_filtro_black_and_white(self,minha_imagem, nome):
    print('Aplicando filtro BlackAndWhite...')
    # Create an instance of the BlackAndWhiteFilter
    black_and_white_filter = BlackAndWhiteFilter()
    # Apply the filter to the image
    filtered_image_black_and_white = black_and_white_filter.apply_filter(minha_imagem)
    # Save the filtered image
    nome = nome + '_black_and_white.jpg'
    filtered_image_black_and_white.save(nome)
    print(f'Filtro black_and_white aplicado com sucesso! Arquivo salvo em {nome}')

  def aplica_filtro_edges(self,minha_imagem, nome):
    print('Aplicando filtro EdgesFilter...')
    # Create an instance of the EdgesFilter
    edges_filter = EdgesFilter()
    # Apply the filter to the image
    filtered_image_edges_filter = edges_filter.apply_filter(minha_imagem)
    # Save the filtered image
    nome = nome + '_edges.jpg'
    filtered_image_edges_filter.save(nome)
    print(f'Filtro edges aplicado com sucesso! Arquivo salvo em {nome}')