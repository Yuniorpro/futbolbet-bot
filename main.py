from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters

# TOKEN DEL BOT
TOKEN = "7741456689:AAEReltV6xcKmuvmOy1U8NJtkBvcpGR2o6U"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 ¡Bienvenido al bot de apuestas!\nUsa /tips para recibir recomendaciones."
    )

# Comando /tips
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ Aquí van los tips del día:\n1. Gana Flamengo\n2. Over 2.5 goles en Palmeiras\n3. Empate Fluminense"
    )

# Comando /comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Tips", callback_data='tips')],
        [InlineKeyboardButton("Contacto", callback_data='contacto')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('📋 Elige una opción:', reply_markup=reply_markup)

# Manejador de botones
async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'tips':
        await query.edit_message_text("🎯 Tips rápidos:\n- Gana Inter Miami\n- Menos de 2.5 goles en São Paulo")
    elif query.data == 'contacto':
        await query.edit_message_text("📩 Contáctanos en @TuCanalTelegram")

# Mensaje de bienvenida a nuevos usuarios
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for miembro in update.message.new_chat_members:
        await update.message.reply_text(f"🎉 ¡Bienvenido {miembro.full_name} al canal!")

# Función principal
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CallbackQueryHandler(botones))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))

    print("🤖 Bot iniciado correctamente...")
    app.run_polling()

if __name__ == '__main__':
    main()
