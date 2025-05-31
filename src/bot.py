from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
import requests

def create_bot(token, system_prompt, model_name="llama-2-7b-chat"):
    app = Application.builder().token(token).build()

    async def start_command(update, context):
        context.user_data["chat_history"] = [{"role": "system", "content": system_prompt}]
        await update.message.reply_text('''👋 Hey! I'm your chatbot.\n\nType /start to begin a new conversation.\n\nLet's go! 💬''')

    async def handle_message(update, context):
        user_message = update.message.text
        chat_history = context.user_data.get("chat_history", [{"role": "system", "content": system_prompt}])
        chat_history.append({"role": "user", "content": user_message})

        data = {
            "model": model_name,
            "messages": chat_history,
            "stream": False
        }

        try:
            response = requests.post("http://localhost:11434/api/chat", json=data)
            response.raise_for_status()
            reply = response.json()['message']['content']
        except Exception as e:
            reply = f"Error: {str(e)}"

        chat_history.append({"role": "assistant", "content": reply})
        context.user_data["chat_history"] = chat_history
        await update.message.reply_text(reply)

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    return app