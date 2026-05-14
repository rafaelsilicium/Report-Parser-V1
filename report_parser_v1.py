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
def leitura_arquivos_txt():
    
    dados_juntos = [] #Variável que receberá o conteúdo dos arquivos .txt unidos
    print("\nIniciando a leitura dos arquivos .txt\n")
    
    #Analisa todos os arquivos da pasta indicada
    for arquivo_resumo in caminho_pasta.glob('*.txt'):
        
        dados_separados = {} #Variável que recebe os conteúdos do arquivo atual
        conteudo_resumo = arquivo_resumo.read_text(encoding = 'utf-8-sig').splitlines()
        print (f"\nLendo o arquivo {arquivo_resumo.name}")
        
        #Separa na variável os cabeçalhos dos conteúdos, apresentando-os aos pares
        if arquivo_resumo.stat().st_size != 0:
            
            #variável para indicação de atualização do arquivo .txt no caso de haver algum campo faltando 
            atualiza_leitura_txt = False
            #Remove espaços e tabulações de cada uma das linhas do conteudo do arquivo .txt 
            conteudo_resumo_strip = [linha.strip() for linha in conteudo_resumo]
            
            #Procura cada uma das palavras-chave (headers) no arquivo .txt atual, indicando se falta algum
            for h in headers:    
                h_strip = h.strip()
                header_presente = any(h_strip in linha for linha in conteudo_resumo_strip)
                
                #caso falte algum header, apresenta no terminal o header faltando e modifica o arquivo .txt
                #adicionando "NÃO INFORMADO" ao campo ausente
                if not (header_presente):
                    print(f"Header {h} faltando!\n")
                    atualiza_leitura_txt = True
                
                    with open(arquivo_resumo,'a', encoding='utf-8-sig') as txt_edit:
                        txt_edit.write(f"\n{h}: NÃO INFORMADO")
            
            #Caso o arquivo .txt tenha sido atualizado pela busca dos headers, refaz a leitura do conteúdo
            if atualiza_leitura_txt:
                conteudo_resumo = arquivo_resumo.read_text(encoding = 'utf-8-sig').splitlines()    
           
           #Separa as palavras chave dos conteúdos, a partir do caractere ":"
            for line in conteudo_resumo:
                if ':' in line:
                    head, contend = line.split(':')
                    dados_separados[head.strip()] = line.strip(head).strip(': ')

            #Adiciona na variável geral o conteúdo da variável parcial
            dados_juntos.append(dados_separados)      
        
        else:
            print("Arquivo ignorado! .txt vazio!" )
        
    return dados_juntos #Retorna a variável com todos os conteúdos unidos


def main():

    print("\n--------Report Parser V1--------\n")
    #Abre o arquivo .csv para escrita
    with open(caminho_arquivo_csv, 'a', newline='', encoding = 'utf-8-sig') as planilha_csv:
        
        #Caso o arquivo esteja vazio, escreve na primeira linha o título 
        # de cada coluna
        if os.path.getsize(caminho_arquivo_csv) == 0:
            print("Arquivo .csv criado!")
            adicionar_headers = csv.writer(planilha_csv, delimiter = ';')
            adicionar_headers.writerow(headers)
            print("Cabeçalho do arquivo .csv adicionado!")
        
        #Escreve no .csv o conteúdo recebido da análise dos arquivos .txt 
        #retornada pela funcao leitura_arquivos_txt   
        adicionar_linha = csv.DictWriter(planilha_csv, fieldnames=headers, delimiter=';')
        adicionar_linha.writerows(leitura_arquivos_txt())
        print("\nEdição do arquivo .csv finalizada!")
        
    print("Fim da execução...")
        

if __name__ == "__main__":
    main()
    