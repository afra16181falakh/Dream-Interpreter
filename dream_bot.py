import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyC8g8ua5VJufl_kPGnHfMVm3lWsVavPua0")
genai.configure(api_key="AIzaSyCMIgg735oFJTXiHQ3gWFKh8aIcKedCaME")
genai.configure(api_key="AIzaSyDLoVVBhxm0NMf9UafHRFasC7TwOOycxXI")
genai.configure(api_key="AIzaSyB9PO9OUbWzYKnJCFv5jr283-mjGpPHyIU")

# Try to get available models first to debug any issues
try:
    models = genai.list_models()
    print(f"Available models: {[model.name for model in models]}")
except Exception as model_list_error:
    print(f"Could not list models: {model_list_error}")

# Set up the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    },
    safety_settings=[
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]
)

def main():
    print("\n✨ Gen Z Dream Bot ✨")
    print("Type 'quit' to exit\n")
   
    # Start chat session
    chat = model.start_chat(history=[])
   
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
               
            # Get response with Gen Z style prompt
            prompt = f"Respond to this as a Gen Z dream interpreter: {user_input}. Keep it casual, use emojis, and make it funny!"
            response = chat.send_message(prompt)
            print("Bot:", response.text)
           
        except KeyboardInterrupt:
            print("\nGoodbye! ✌️")
            break
        except Exception as e:
            print("Oops! Something went wrong:", str(e))

if __name__ == "__main__":
    main()
