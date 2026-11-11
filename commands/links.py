from telegram import Update
from telegram.ext import ContextTypes
from services import add_link, list_links, remove_link, edit_link


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

async def rmlink(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link_name = context.args[0]
    remove_link(link_name)
    await update.message.reply_text(f"'{link_name}' removido com sucesso!")

def context_Validation(context: ContextTypes.DEFAULT_TYPE, min_args: int) -> bool:
    return len(context.args) >= min_args

async def editlink(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    mensagem_uso = (
        "Uso:\n"
        "/editlink nome nome novo_nome\n"
        "/editlink nome url nova_url\n"
        "/editlink nome ambos novo_nome nova_url"
    )

    if not context_Validation(context, 3):
        await update.message.reply_text(mensagem_uso)
        return

    link_name = context.args[0]
    action = context.args[1].lower()

    if action == "nome" and len(context.args) == 3:
        new_name = context.args[2]
        resultado = edit_link(link_name, novo_nome=new_name)

    elif action == "url" and len(context.args) == 3:
        new_url = context.args[2]
        resultado = edit_link(link_name, nova_url=new_url)

    elif action == "ambos" and len(context.args) == 4:
        new_name = context.args[2]
        new_url = context.args[3]
        resultado = edit_link(
            link_name,
            novo_nome=new_name,
            nova_url=new_url
        )

    else:
        await update.message.reply_text(mensagem_uso)
        return

    if resultado:
        await update.message.reply_text(
            f"'{link_name}' atualizado com sucesso!"
        )
    else:
        await update.message.reply_text(
            f"Link '{link_name}' não encontrado."
        )