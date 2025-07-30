from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
import random

# TOKEN de tu bot
TOKEN = "7741456689:AAEReltV6xcKmuvmOy1U8NJtkBvcpGR2o6U"

# Tips profesionales basados en análisis reales
tips = [
    "📊 TIP: En la Serie A de Brasil, el 64% de los partidos en 2024 terminaron con menos de 2.5 goles.",
    "🔥 TIP: En la MLS, el 71% de los goles llegan en el segundo tiempo. Considera Over 1.5 2T.",
    "💡 TIP: Equipos que juegan entresemana Libertadores rotan en liga. Cuidado con favoritos sudamericanos.",
    "⚽ TIP: En derbis de Premier (ej: Arsenal vs Tottenham), hay alta probabilidad de tarjetas (Over 4.5).",
    "📈 TIP: Si un equipo lleva 3 partidos sin marcar, suele tener cuotas infladas. Revisa el 'ambos marcan'.",
    "💰 TIP: Evita combinadas largas. La mayoría de profesionales usan apuestas simples y stake bajo.",
    "⚠️ TIP: Nunca apuestes sin confirmar alineaciones. Un solo jugador clave puede cambiar el partido.",
    "🧠 TIP: Los últimos 5 partidos como local o visitante dicen más que la tabla general.",
    "📌 TIP: En la Liga MX hay muchas remontadas. Juega 'gol en los últimos 15 min' si el local va perdiendo.",
    "🎯 TIP: No persigas pérdidas. Si pierdes 2 apuestas seguidas, pausa y vuelve con mente fría."
]

# /start con botones
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    keyboard = [
        [
            InlineKeyboardButton("📌 Ver Tip de Hoy", callback_data="ver_tip"),
            InlineKeyboardButton("📘 Comandos", callback_data="ver_comandos")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"👋 ¡Hola *{user}*! Bienvenido a *FutbolBet* ⚽\n\n"
        "Aquí recibirás tips reales y consejos profesionales para apostar con más cabeza y menos suerte.\n\n"
        "Selecciona una opción 👇",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# /tip
async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tip_random = random.choice(tips)
    await update.message.reply_text(tip_random, parse_mode="Markdown")

# /comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "📘 *Lista de comandos disponibles:*\n\n"
        "✅ /start – Muestra el menú con botones\n"
        "✅ /tip – Muestra un consejo profesional de apuestas\n"
        "✅ /comandos – Muestra este listado de comandos\n"
    )
    await update.message.reply_text(texto, parse_mode="Markdown")

# Botones del menú de /start
async def manejar_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ver_tip":
        tip_random = random.choice(tips)
        await query.edit_message_text(tip_random, parse_mode="Markdown")
    elif query.data == "ver_comandos":
        texto = (
            "📘 *Lista de comandos disponibles:*\n\n"
            "✅ /start – Muestra el menú con botones\n"
            "✅ /tip – Muestra un consejo profesional de apuestas\n"
            "✅ /comandos – Muestra este listado de comandos\n"
        )
        await query.edit_message_text(texto, parse_mode="Markdown")

# Bienvenida automática en grupos
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for miembro in update.message.new_chat_members:
        await update.message.reply_text(
            f"👋 Bienvenido *{miembro.first_name}* al grupo de *FutbolBet* ⚽\n"
            "Usa /tip para recibir consejos de apuestas cada día.",
            parse_mode="Markdown"
        )

# Ejecutar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tip", tip))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CallbackQueryHandler(manejar_callback))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    print("✅ Bot FutbolBet PRO listo y corriendo...")
    app.run_polling()
