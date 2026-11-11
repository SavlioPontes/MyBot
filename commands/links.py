from telegram import Update
from telegram.ext import ContextTypes
from services import add_link, list_links


async def addlink(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    add_link(context.args[0], context.args[1])
    await update.message.reply_text(f"'{context.args[0]}' adicionado com sucesso!")

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    links = list_links()
    if not links:
        await update.message.reply_text("Nenhum link encontrado.")
        return

    response = "Links cadastrados:\n"
    for link in links:
        response += f"{link[1]}: {link[2]}\n"

    await update.message.reply_text(response)