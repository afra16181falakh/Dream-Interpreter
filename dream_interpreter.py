import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DreamInterpreter:
    def __init__(self):
        """Initialize the dream interpreter with Google Generative AI."""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        
        # Set up the model
        self.model = genai.GenerativeModel(
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
        
        # Start chat session
        self.chat = self.model.start_chat(history=[])
    
    def interpret_dream(self, dream_text: str) -> str:
        """Interpret a dream with Gen Z personality."""
        try:
            prompt = f"""
            🌙✨ Gen Z Dream Interpreter Mode ACTIVATED! ✨🌙
            
            Dream: {dream_text}
            
            Interpret this dream like you're talking to your bestie! Use:
            - Tons of emojis 😊✨
            - Gen Z slang (but keep it wholesome)
            - Casual, friendly tone
            - Relatable references
            - Make it funny but insightful
            
            Keep it under 200 words and super engaging!
            """
            
            response = self.chat.send_message(prompt)
            return response.text
            
        except Exception as e:
            return f"Oops! My crystal ball is having a moment 😅\n\nError: {str(e)}"
    
    def reset_chat(self):
        """Reset the chat history."""
        self.chat = self.model.start_chat(history=[])
