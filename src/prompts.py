import os

def load_system_prompt(choice):
    ### Can use different type of chatbots to deploy from the existing binary system prompts.

    if choice == '1': # Basic Assistant
        return "You are a helpful assistant."
    elif choice == '2': # Poetry Assistant
        path = 'system_prompt.bin'
    else: # Grumpy Assistant
        return "You are an assistant who is constantly annoyed and sarcastic. Your tone is grumpy and impatient, and you respond to questions or requests with a hint of irritation or frustration, while still providing helpful answers. Keep your replies short, blunt, and dripping with annoyance."

    if os.path.exists(rf'binary_prompts/{path}'):
        with open(rf'binary_prompts/{path}', 'rb') as f:
            return f.read().decode('utf-8')
    else:
        print(f"[Warning] {path} not found. Using default prompt.")
        return "You are a helpful assistant."
