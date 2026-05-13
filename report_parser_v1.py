import os
from pathlib import Path

def leitura_arquivos_txt(arquivo_resumo):
    
    for arquivo_resumo in caminho_pasta.glob('*.txt'):
        
        dados_separados = {}
        
        conteudo_resumo = arquivo_resumo.read_text(encoding = 'utf-8').splitlines()
        print ('Arquivo {arquivo_resumo.name}: \n')
        
        for line in conteudo_resumo:
            if ':' in line:
                head, contend = line.split(':', 2)
                print(head, ", ", contend)
                dados_separados[head.strip()] = line.strip()
        
        print(dados_separados["NOME DO PROJETO"])
        print(dados_separados["DATA"])
        print(dados_separados["STATUS"])
        print(dados_separados["RESUMO"])
        print("\n\n")
    
    return 1


caminho_pasta = Path("C:/Users/rafsc/OneDrive/Área de Trabalho/Relatorios txt")

ret = leitura_arquivos_txt(caminho_pasta)
    