from telegram import Update
from telegram.ext import ContextTypes
from .links import contextValidation
from services import add_event, list_events, remove_event, edit_event

async def addevent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not contextValidation(context, 3):
        await update.message.reply_text("Uso: /addevent <nome do evento> <data do evento> <hora do evento>")
        return
    
    add_event(context.args[0], context.args[1], context.args[2])

async def listevent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    events = list_events()
    if not events:
        await update.message.reply_text("Nenhum evento encontrado.")
        return

    response = "Eventos cadastrados:\n"
    for event in events:
        response += f"{event[1]}: {event[2]} às {event[3]}\n"

    await update.message.reply_text(response)

async def rmevent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not contextValidation(context, 1):
        await update.message.reply_text("Uso: /rmevent <id do evento>")
        return

    event_id = context.args[0]
    remove_event(event_id)
    await update.message.reply_text(f"Evento com ID {event_id} removido.")

async def editevent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not contextValidation(context, 4):
        await update.message.reply_text("Uso: /editevent <id do evento> <novo nome> <nova data> <nova hora>")
        return

    event_id = context.args[0]
    new_name = context.args[1]
    new_date = context.args[2]
    new_time = context.args[3]

    edit_event(event_id, new_name, new_date, new_time)
    await update.message.reply_text(f"Evento com ID {event_id} atualizado.")

