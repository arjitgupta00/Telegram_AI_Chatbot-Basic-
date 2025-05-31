import ctypes
import argparse
from config.config import TELEGRAM_BOT_TOKEN
from src.prompts import load_system_prompt
from src.bot import create_bot
from src.model_manager import ensure_ollama_model, MODEL_NAME

# Prevent Windows system sleep
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001 | 0x00000040)

def main():
    parser = argparse.ArgumentParser(description="Run Telegram LLaMA chatbot")
    parser.add_argument(
        '-m', '--model',
        choices=['1', '2'],
        default='0',
        help="Select the system prompt model (1=default, 2=poetry bot). Default is 1."
    )
    args = parser.parse_args()

    system_prompt = load_system_prompt(args.model)
    print(system_prompt[:100])
    print(f"[INFO] System prompt loaded (model {args.model}):\n{system_prompt[:100]}...\n")

    # Ensure Ollama model is installed before starting the bot
    if not ensure_ollama_model():
        print("[ERROR] Could not ensure Ollama model is installed. Exiting.")
        return

    print(f"[INFO] Starting Telegram bot with model '{MODEL_NAME}'...")
    app = create_bot(TELEGRAM_BOT_TOKEN, system_prompt, model_name=MODEL_NAME)
    app.run_polling()

if __name__ == "__main__":
    main()