import os
from pathlib import Path
import csv

#Configuração do caminho da pasta com os relatórios em .txt
caminho_pasta = Path("C:/Users/rafsc/OneDrive/Área de Trabalho/Relatorios txt")

#Configuração do caminho e nome do arquivo .csv a ser criado
caminho_arquivo_csv = 'C:/Users/rafsc/OneDrive/Área de Trabalho/Relatorios txt/projetos.csv'

#Indicação do título das separações dentro dos arquivos .txt
headers = ['NOME DO PROJETO', 'DATA', 'STATUS', 'RESUMO']


#Função para ler os arquivos .txt e juntar os conteúdos em uma única variável
def leitura_arquivos_txt(arquivo_resumo):
    
    dados_juntos = [] #Variável que receberá o conteúdo dos arquivos .txt unidos
    
    #Analisa todos os arquivos da pasta indicada
    for arquivo_resumo in caminho_pasta.glob('*.txt'):
        
        dados_separados = {} #Variável que recebe os conteúdos do arquivo atual
        
        conteudo_resumo = arquivo_resumo.read_text(encoding = 'utf-8').splitlines()
        print ('Arquivo',arquivo_resumo.name,': \n')
        
        #Separa na variável os cabeçalhos dos conteúdos, apresentando-os aos pares
        for line in conteudo_resumo:
            if ':' in line:
                head, contend = line.split(':')
                dados_separados[head.strip()] = line.strip(head).strip(': ')
        
        #Print do conteúdo do arquivo .txt atual
        print(dados_separados, "\n\n")
        #Adiciona na variável geral o conteúdo da variável parcial
        dados_juntos.append(dados_separados)      
        
    return dados_juntos #Retorna a variável com todos os conteúdos unidos


def main():

    #Abre o arquivo .csv para escrita
    with open(caminho_arquivo_csv, 'a', newline='', encoding = 'utf-8-sig') as planilha_csv:
        
        #Caso o arquivo esteja vazio, escreve na primeira linha o título de cada coluna
        if os.path.getsize(caminho_arquivo_csv) == 0:
            adicionar_headers = csv.writer(planilha_csv, delimiter = ';')
            adicionar_headers.writerow(headers)
        
        #Escreve no .csv o conteúdo recebido da análise dos arquivos .txt    
        adicionar_linha = csv.DictWriter(planilha_csv, fieldnames=headers, delimiter=';')
        adicionar_linha.writerows(leitura_arquivos_txt(caminho_pasta))
        
    

if __name__ == "__main__":
    main()
    