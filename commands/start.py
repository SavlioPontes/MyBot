from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome = update.effective_user.first_name

    mensagem = f"""Olá, {nome}! Vamos começar a trabalhar?
    Você pode usar o comando /help para ver a lista de comandos disponíveis.
    """
    await update.message.reply_text(mensagem)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    mensagem = f"""Aqui estão os comandos disponíveis:
    /links - Lista todos os links cadastrados.
    /addlink <nome> <url> - Adiciona um novo link com o nome e a URL fornecidos.
    /rmlink <nome> - Remove o link com o nome fornecido.
    /help - Mostra esta mensagem de ajuda.
    """
    await update.message.reply_text(mensagem)