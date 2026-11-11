from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome = update.effective_user.first_name

    mensagem = f"""Olá, {nome}! Vamos começar a trabalhar?

Você pode utilizar os seguintes comandos:

/start - Iniciar o bot
/help - Listar os comandos disponíveis
/status - Verificar o servidor
/bots - Consultar os bots ativos
/links - Consultar seus links
/codigo - Consultar códigos salvos
"""

    await update.message.reply_text(mensagem)