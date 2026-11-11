import os

from telegram.ext import ApplicationBuilder, CommandHandler
from commands import start

from data import inicializar_banco

token = os.environ["TELEGRAM_BOT_TOKEN"]


def main() -> None:
    inicializar_banco()
    

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("links", links))
    app.add_handler(CommandHandler("addlink", addlink))
    app.add_handler(CommandHandler("projects", start))


    app.run_polling()


if __name__ == "__main__":
    main()