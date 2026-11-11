import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from commands import start, links, addlink, rmlink, editlink, helpme, addevent, listevent, rmevent, editevent, newqrcode
from data import inicializar_banco

def main() -> None:

    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("O token do bot não foi encontrado no arquivo .env.")    
    app = ApplicationBuilder().token(token).build()

    inicializar_banco()

    #Default commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", helpme))
    #Links
    app.add_handler(CommandHandler("links", links))
    app.add_handler(CommandHandler("addlink", addlink))
    app.add_handler(CommandHandler("rmlink", rmlink))
    app.add_handler(CommandHandler("editlink", editlink))
    #Reminder
    app.add_handler(CommandHandler("addevent", addevent))
    app.add_handler(CommandHandler("listevent", listevent))
    app.add_handler(CommandHandler("rmevent", rmevent))
    app.add_handler(CommandHandler("editevent", editevent))
    #QR code generation
    app.add_handler(CommandHandler("newqrcode", newqrcode))
    #Bots
    # app.add_handler(CommandHandler("bots", bots))
    # app.add_handler(CommandHandler("botstatus", botstatus))
    # app.add_handler(CommandHandler("botlogs", botlogs))
    # app.add_handler(CommandHandler("restartbot", restartbot))   


    app.run_polling()

if __name__ == "__main__":
    main()