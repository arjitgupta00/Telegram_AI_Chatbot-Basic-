import subprocess
from config.config import ENV_MODEL_NAME

MODEL_NAME = ENV_MODEL_NAME

if MODEL_NAME == None:
    MODEL_NAME = 'dolphin-mistral'
else:
    pass

def ensure_ollama_model():
    """
    Check if Ollama has MODEL_NAME installed.
    If not, import it using ollama CLI.
    """
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        installed_models = result.stdout.lower()

        if MODEL_NAME.lower() in installed_models:
            print(f"[INFO] Model '{MODEL_NAME}' is already installed in Ollama.")
            return True
        else:
            print(f"[INFO] Model '{MODEL_NAME}' not found. Importing now...")
            subprocess.run(["ollama", "pull", MODEL_NAME], check=True)
            print(f"[INFO] Model '{MODEL_NAME}' successfully imported.")
            return True
    except FileNotFoundError:
        print("[ERROR] 'ollama' CLI not found. Please install Ollama and add it to your PATH.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Ollama command failed: {e}")
        return False