import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from commands import start, links, addlink, rmlink, editlink
from data import inicializar_banco

def main() -> None:

    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("O token do bot não foi encontrado no arquivo .env.")    
    app = ApplicationBuilder().token(token).build()

    inicializar_banco()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("links", links))
    app.add_handler(CommandHandler("addlink", addlink))
    app.add_handler(CommandHandler("rmlink", rmlink))
    app.add_handler(CommandHandler("editlink", editlink))
    

    app.run_polling()

if __name__ == "__main__":
    main()