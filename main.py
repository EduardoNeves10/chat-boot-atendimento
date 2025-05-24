from comandos import mostrat_ajuda, horario_disponivel, contato_instagram, contato_delivery, resposta_padrao, lista_de_produtos
import pyfiglet

# ascii_art = pyfiglet.figlet_format('Seja bem vindo Saanta Adega')

def responder_comLogica(entrada: str) -> str:
        entrada = entrada.strip().lower()
# def principal(texto):
#     print(ascii_art)
#     print('Bot max Iniciado... Digite 0 para ver os comandos disponíveis.')
#     print(f'{texto}')
#     while True:
#         entrada = input('Usuário: ').strip().lower()

        # if entrada == 'sair':
        #     print('Chatbot max: Encerrando o programa.')
            # break
        if entrada == '0':
            return('\nBot max:\n ', mostrat_ajuda())
        elif entrada == '1':
            return('\nBot max:\n ', horario_disponivel())
        elif entrada == '2':
            return('\nBot max:\n ', lista_de_produtos())
        elif entrada == '3':
            return('\nBot max:\n ', contato_instagram())
        elif entrada == '4':
            return('\nBot max:\n ', resposta_padrao())
        elif entrada == '5':
            return('\nBot max:\n ', contato_delivery())
        elif entrada == '6':
            return('Bot max:  Encerrando o programa')
            # break
        else:
            return 'Comando não reconhecido. Digite 0 para ajuda.'
