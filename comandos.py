from datetime import datetime
import pandas as pd
import gdown
import pyfiglet



def mostrat_ajuda():
    return (
        '\nComandos Disponíveis:\n'
        '1 - Está pagina!\n'
        '2 - Horário de atendimento presencial.\n'
        '3 - Lista de Produtos.\n'
        '4 - Instagram.\n'
        '5 - Iniciar um Delivery.\n'
        '6 - Dados de Compra.\n'
        '7 - Finaliza pedido Pedido.\n'
    )

def horario_disponivel():
    agora = datetime.now()
    return(
    '\nSegunda-feira: Fechado\n'
    'Terça-feira: 12:00 - 18:00\n'
    'Quarta-feira: 12:00 - 18:00\n'
    'Quinta-feira: 12:00 - 18:00\n'
    'Sexta-feira: 12:00 - 21:00\n'
    'Sábado: 12:00 - 22:00\n'
    'Domingo: 12:00 - 18:00\n'
    f'\nHorário atual {agora.strftime("%H:%M")}'
    )
   
def lista_de_produtos():
    # df = pd.read_excel('texte.xlsx')
    # return(df[['produto','valor']])

    url ='https://docs.google.com/spreadsheets/d/1F_zbq7eA8isZ-_uN6f6PuAFp8RAr4IaX/edit?usp=drive_link&ouid=113855903916372490284&rtpof=true&sd=true'

    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    output = 'texte.xlsx'
    # Baixa o arquivo
    gdown.download(download_url, output, quiet=False)

    df = pd.read_excel(output)

    lista = ""
    for index, row in df.iterrows():
        numero = row['item']
        produto = row['produto']
        valor = row['valor']
        lista += f" {numero} - {produto}: R$ {valor:.2f}\n"

    return lista

def contato_instagram():
    return 'Link: https://www.instagram.com/saantaadega/'

def contato_whattsapp():
    return 'Link: WhattsApp'

def contato_delivery():
    return(
    '\nOlá, gostaria de fazer um pedido. Segue meus dados.\n'
    '\nSelecione o número do item da lista: '
    '\nSelecione a quantidade: ' 
    '\nDigite a observação:\n ' 
    '\nApós enviar os dados, digite o número 6\n ' 
    )
    

def resposta_padrao():
    return(
    '\nSegue a confirmação dos meus dados.\n'
    '\nNome: '
    '\nEndereço: '
    '\nPagamento: '
    '\nObservações: ' 
    '\n Digite 7 logo após envia todas opções. \n' 
    )

