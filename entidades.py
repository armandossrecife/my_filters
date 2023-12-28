from PIL import Image
import requests
import os

class Download:
    def __init__(self, url, path_arquivo):
        self.url = url
        self.path_arquivo = path_arquivo

    def executa(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Verifica se houve algum erro na requisição
            with open(self.path_arquivo, 'wb') as file:
                file.write(response.content)
            print(f"Download completo. Arquivo salvo em: {self.path_arquivo}")
        except requests.exceptions.MissingSchema:
            print("URL inválida. Certifique-se de fornecer uma URL válida.")
            raise Exception('URL inválida. Certifique-se de fornecer uma URL válida.')
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")
            raise Exception(f"Erro na conexão: {e}")

class Imagem: 
    minha_imagem = None

    def __init__(self, id, nome_arquivo, path_arquivo):
        self.id = id
        self.nome_arquivo = nome_arquivo
        self.local_referencia = path_arquivo
        try:
            self.minha_imagem = Image.open(path_arquivo)
        except Exception as ex:
            print(f'Erro ao criar a imagem com o arquivo {nome_arquivo} na referência {path_arquivo}: {str(ex)}')

    def dimensoes(self):
        return self.minha_imagem.size

    def tamanho(self):
        return os.path.getsize(self.local_referencia)

    def formato(self):
        return self.minha_imagem.format

    def conteudo(self):
        return self.minha_imagem

    def __str__(self):
        return f'Nome: {self.nome_arquivo}, Dimensoes:{self.dimensoes()}, Formato: {self.formato()}, Tamanho: {self.tamanho()}'