import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# Tu token (NO lo compartas públicamente en el futuro)
TOKEN = "7741456689:AAEReltV6xcKmuvmOy1U8NJtkBvcpGR2o6U"

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Ver tips de hoy", callback_data="tips")],
        [InlineKeyboardButton("📘 Ver comandos", callback_data="comandos")]
    ]
    await update.message.reply_text(
        "👋 ¡Bienvenido a FUTBOLBET!\n\nAquí recibirás tips diarios basados en estadísticas reales y análisis profesionales.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Comando /tips
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽️ Tip del día:\n\n🔹 Gana Inter Miami\n🔹 +2.5 goles en Flamengo\n🔹 Ambos marcan en LA Galaxy vs Austin FC")

# Comando /comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📘 Comandos disponibles:\n\n"
        "/start - Iniciar el bot y ver menú\n"
        "/tips - Ver los tips de fútbol del día\n"
        "/comandos - Mostrar esta ayuda\n"
    )

# Mensaje de bienvenida para nuevos miembros
async def bienvenida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"👋 ¡Bienvenido, {member.full_name}! ⚽️ Este es el canal de TIPS de fútbol profesional.")

# Manejar botones
async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "tips":
        await tips(update, context)
    elif query.data == "comandos":
        await comandos(update, context)

# Main
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CallbackQueryHandler(botones))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, bienvenida))

    app.run_polling()

if __name__ == '__main__':
    main()
    app.run_polling()
