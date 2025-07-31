from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Token fijo (puedes luego moverlo a una variable de entorno por seguridad)
TOKEN = "7741456689:AAEReltV6xcKmuvmOy1U8NJtkBvcpGR2o6U"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Bienvenido al bot.")

# Comando /tips
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aquí van algunos tips útiles...")

# Comando /comandos con botones
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = [
        [InlineKeyboardButton("Tip 1", callback_data="tip1")],
        [InlineKeyboardButton("Tip 2", callback_data="tip2")],
    ]
    reply_markup = InlineKeyboardMarkup(botones)
    await update.message.reply_text("Selecciona una opción:", reply_markup=reply_markup)

# Al pulsar un botón
async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Seleccionaste: {query.data}")

# Bienvenida a nuevos miembros
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for miembro in update.message.new_chat_members:
        await update.message.reply_text(f"¡Bienvenido {miembro.full_name} al grupo!")

# MAIN
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CallbackQueryHandler(botones))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))
    app.run_polling()

if __name__ == "__main__":
    main()
