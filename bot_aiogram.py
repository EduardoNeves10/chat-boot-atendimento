import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from comandos import mostrat_ajuda, horario_disponivel, contato_instagram, contato_delivery, resposta_padrao, lista_de_produtos

BOT_TOKEN = "7220407737:AAE5Qq2xEqwWevuTta4l1nEhOBc2bILNl2Q"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


teclado = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Carrinho de produtos"), KeyboardButton(text="📝 Lista de compras")],
        [KeyboardButton(text="Sim"), KeyboardButton(text="Não")],
        [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6")],
        [KeyboardButton(text="7")]
    ],
    resize_keyboard=True
)

def responder_com_logica_local(entrada: str) -> str: # parametro chamado entrada, que é uma string, -> str: retorna como resposta uma string
    entrada = entrada.strip().lower() #formata o texto de entrada em minuscula e retira os espaços

    if entrada == '1':
        return mostrat_ajuda()
    elif entrada == '2':
        return horario_disponivel()
    elif entrada == '3':
        return lista_de_produtos()
    elif entrada == '4':
        return contato_instagram()
    elif entrada == '5':
        return contato_delivery()
    elif entrada == '6':
        return resposta_padrao  ()
    elif entrada == '7':
        return "Pedido concluido. Obrigado!"
    else:
        return ""

aguardando_confirmacao = {}  # guarda se o usuário está esperando confirmação de finalização

historico_respostas ={}

@dp.message()
async def responder_mensagem(message: Message):
    texto = message.text.strip().lower()
    user_id = message.from_user.id

    # Inicializa estruturas se necessário
    if user_id not in historico_respostas:
        historico_respostas[user_id] = []
    if user_id not in aguardando_confirmacao:
        aguardando_confirmacao[user_id] = False

    # Saudação só na primeira mensagem (exceto se for "7")
    if not historico_respostas[user_id] and texto != "7":
        await message.answer("Seja bem-vindo à sua nova bebida favorita. \nDigite 1 para ver o cardápio.", reply_markup=teclado)

    # Se o bot está esperando confirmação de finalização
    if aguardando_confirmacao[user_id]:
        if texto == "sim":
            await message.answer("Pedido concluído. Obrigado!")
            historico_respostas[user_id] = []
            aguardando_confirmacao[user_id] = False
        elif texto == "não":
            await message.answer("Ok, continue escolhendo.")
            aguardando_confirmacao[user_id] = False
        else:
            await message.answer("Responda apenas com 'sim' ou 'não'.")
        return

    # Armazena a entrada no histórico
    historico_respostas[user_id].append(texto)

    # Se usuário digitou "7", mostrar resumo e perguntar
    if texto == "7":
        respostas = historico_respostas.get(user_id, [])
        respostas_filtradas = [r for r in respostas if r not in ["1", "2", "3", "4", "5", "6", "7"]]

        if respostas_filtradas:
            resumo = "Resumo do seu pedido:\n- " + "\n- ".join(respostas_filtradas)
        else:
            resumo = "Você ainda não escreveu nenhuma mensagem personalizada."

        await message.answer(resumo)
        await message.answer("Deseja finalizar o pedido? (sim / não)")
        aguardando_confirmacao[user_id] = True
        return

    # Gera resposta normal do menu
    resposta = responder_com_logica_local(texto)
    await message.answer(f"Bebida favorita:\n{resposta}")




async def main(): # define função assíncrona main, a palavra async indica que pode conte operações assíncronas usando await
    print("Bot Telegram iniciado...") # apenas exibe a mensagem no terminal
    await dp.start_polling(bot) # dp -> Dispatcher funções que respondem a mensagem, e coordenar as ações do bot. Ele fica escultando o que acontece (mensagens, comandos) e chama a função certa.
    # .start_polling(bot) Esse método diz ao bot para começar a verifica o servidor do Telegram constantemente (em loop) procurando por novas mensagens
    # await significa: espere aqui enquanto isso roda, mas sem trava o restante do sistema



if __name__ == "__main__":
    asyncio.run(main())
