from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome = update.effective_user.first_name

    mensagem = (
        f"Olá {nome}! Vamos começar a trabalhar?\n\n"
        "Você pode utilizar os seguintes comandos:\n"
        "/start - Iniciar o bot\n"
        "/status - Verificar o servidor\n"
        "/cpu - Consultar o processador\n"
        "/ram - Consultar a memória RAM\n"
        "/help - Mostrar os comandos"
    )

    await update.message.reply_text(mensagem)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    nome = update.effective_user.first_name

    mensagem = (
        f"Olá {nome}! Vamos começar a trabalhar?\n\n"
        "Você pode utilizar os seguintes comandos:\n"
        "/start - Iniciar o bot\n"
        "/status - Verificar o servidor\n"
        "/cpu - Consultar o processador\n"
        "/ram - Consultar a memória RAM\n"
        "/help - Mostrar os comandos"
    )

    await update.message.reply_text(mensagem)

app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("start", start)) # responde um /hello com a funcao hello()
app.add_handler(CommandHandler("status", status)) 
app.add_handler(CommandHandler("cpu", cpu)) 
app.add_handler(CommandHandler("ram", ram)) 
app.add_handler(CommandHandler("help", help)) 





app.run_polling()