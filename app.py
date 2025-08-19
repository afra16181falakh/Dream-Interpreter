import streamlit as st
import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError # Import specific exceptions

# =======================================================================================
# SECTION 1: API CONFIGURATION & CORE LOGIC
# =======================================================================================

# --- IMPORTANT: YOUR GOOGLE API KEYS ---
# Place all your API keys in this list.
# The code will automatically try the next key if one is exhausted.
GOOGLE_API_KEYS = [
    "AIzaSyAYlCXPS3FqLVU8i1_aMFoe9cHjnaxQCfg",
    "AIzaSyCMIgg735oFJTXiHQ3gWFKh8aIcKedCaME",
    "AIzaSyDLoVVBhxm0NMf9UafHRFasC7TwOOycxXI",
    "AIzaSyB9PO9OUbWzYKnJCFv5jr283-mjGpPHyIU"
]

# Initialize API configuration and model
def init_api_model():
    """
    Tries to configure the Generative AI model with an API key from the list.
    Cycles through keys if initial attempts fail.
    """
    if "api_key_index" not in st.session_state:
        st.session_state.api_key_index = 0 # Start with the first key
    
    attempts = 0
    max_attempts = len(GOOGLE_API_KEYS) # Number of keys to try
    
    while attempts < max_attempts:
        try:
            current_key = GOOGLE_API_KEYS[st.session_state.api_key_index]
            genai.configure(api_key=current_key)
            
            # Try to get available models first to debug any issues
            try:
                models = genai.list_models()
                print(f"Available models: {[model.name for model in models]}")
            except Exception as model_list_error:
                print(f"Could not list models: {model_list_error}")
            
            # Use the current recommended model
            model = genai.GenerativeModel('gemini-1.5-flash')
            st.session_state.api_works = True # Mark API as working with this key
            print(f"API configured successfully with key at index: {st.session_state.api_key_index}")
            return model
        except Exception as e:
            st.session_state.api_works = False
            print(f"Failed to configure API with key at index {st.session_state.api_key_index}: {e}")
            # Move to the next key in the list (circularly)
            st.session_state.api_key_index = (st.session_state.api_key_index + 1) % len(GOOGLE_API_KEYS)
            attempts += 1
            time.sleep(0.5) # Small delay before trying the next key to avoid rapid failures
    
    print("All provided API keys failed to configure.")
    return None # All keys failed

# Initialize model globally (or ensure it's initialized on first run)
# This will be called once when the app starts, or when it reruns if model isn't in session_state
if "model" not in st.session_state or st.session_state.model is None:
    st.session_state.model = init_api_model()

def get_dream_interpretation_from_api(dream_text):
    """
    Sends the dream to the Gemini API and gets a high-quality interpretation.
    Includes logic to switch API keys if a ResourceExhausted error occurs.
    """
    if not st.session_state.api_works or st.session_state.model is None:
        return "OMG, the cosmic vibes are a little fuzzy right now because the API isn't set up or all keys are exhausted. Let's try again later! 💖"
    
    prompt = f"""
    You are DreamBot, a Gen Z dream interpreter. Your vibe is cool, empathetic, and a little bit spiritual but in a modern, aesthetic way.
    You use emojis like ✨, 💖, 🦋, 🌙, and you call the user "bestie" or just talk to them like a close friend.
    NEVER mention that you are an AI or a language model.
    A user had this dream: "{dream_text}"
    Give a meaningful, detailed, and nicely written interpretation of this dream. Make it sound cool and reassuring.
    Structure it in a few paragraphs. Start with a cool opening, then the main interpretation, and end with a positive, reassuring thought.
    """
    
    try:
        response = st.session_state.model.generate_content(prompt)
        return response.text
    except ResourceExhausted as re:
        print(f"Current API key exhausted: {re}. Attempting to switch key...")
        st.session_state.api_key_index = (st.session_state.api_key_index + 1) % len(GOOGLE_API_KEYS)
        st.session_state.model = init_api_model() # Try to re-initialize with the next key
        
        if st.session_state.api_works:
            print(f"Switched API key successfully to index: {st.session_state.api_key_index}. Retrying request...")
            time.sleep(0.5) # Small delay before retrying
            return get_dream_interpretation_from_api(dream_text) 
        else:
            return "Uh oh, it seems like all my API keys are taking a nap! I can't decode your dream right now. Check back later! 😴"
    except GoogleAPIError as gae:
        print(f"Google API Error: {gae}")
        return "Woah, there's a glitch in the Matrix! I hit an unexpected snag with the dream-decoding tech. Try again in a sec! 🦋"
    except Exception as e:
        print(f"Unexpected API error: {e}")
        return "My crystal ball is a bit foggy. Something went wrong with the dream interpretation. Can you try telling me your dream again? ✨"

# =======================================================================================
# SECTION 2: STYLING (UNIFIED AND ROBUST WITH THEME SWITCHING)
# =======================================================================================

def load_css():
    """Loads simplified CSS that actually works."""
    st.markdown("""
    <style>
        /* Base App Styling */
        .stApp { 
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
            color: white;
        }
        
        /* Text Styling */
        h1, h2, h3, p, label { 
            color: white !important;
        }
        
        /* Auth Container */
        .auth-container {
            background: rgba(0,0,0,0.4);
            padding: 3rem;
            border-radius: 25px;
            text-align: center;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.1);
            margin: 2rem auto;
            max-width: 500px;
        }
        
        /* Auth Title */
        .auth-container h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Input Fields */
        .stTextInput input {
            background: rgba(255,255,255,0.1) !important;
            color: white !important;
            border: 2px solid rgba(255,255,255,0.3) !important;
            border-radius: 10px !important;
        }
        
        /* Buttons */
        .stButton button {
            background: linear-gradient(135deg, #ff6b6b, #feca57) !important;
            color: white !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 15px 30px !important;
            font-weight: bold !important;
        }
        
        /* Reduce top margin from main content instead of hiding elements */
        
        /* Remove top margin from main content */
        .main .block-container {
            padding-top: 1rem !important;
        }

        /* --- Main App Core Styles (affect chat, input, buttons) --- */
        .user-bubble, .bot-bubble { 
            padding: 20px; 
            border-radius: 25px; 
            margin: 15px 0; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.15); 
            animation: slideIn 0.6s ease-out; 
            position: relative;
            overflow: hidden;
        }
        .user-bubble::before, .bot-bubble::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }
        .user-bubble:hover::before, .bot-bubble:hover::before {
            transform: translateX(100%);
        }
        
        .stTextArea > div > div { 
            border-radius: 20px; 
            border-width: 3px; 
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            background: rgba(255,255,255,0.15) !important;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.3) !important;
        }
        .stTextArea > div > div:focus-within {
            transform: scale(1.02);
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            border-color: #4ecdc4 !important;
            background: rgba(255,255,255,0.2) !important;
        }
        .stTextArea textarea {
            color: white !important;
            font-size: 16px !important;
            font-weight: 500 !important;
        }
        .stTextArea textarea::placeholder {
            color: rgba(255,255,255,0.7) !important;
            font-style: italic;
        }
        
        /* Form labels styling */
        .stTextArea label {
            color: white !important;
            font-size: 18px !important;
            font-weight: 700 !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
            margin-bottom: 10px !important;
        }
        
        /* Target buttons in main content only, not sidebar */
        .main .stButton > button { 
            border: none; 
            padding: 15px 35px; 
            border-radius: 30px; 
            font-weight: bold; 
            font-size: 16px;
            transition: all 0.3s ease; 
            position: relative;
            overflow: hidden;
        }
        .main .stButton > button:hover { 
            transform: translateY(-3px) scale(1.05); 
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .main .stButton > button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }
        .main .stButton > button:hover::before {
            left: 100%;
        }

        /* --- Mystical Theme Styles (Fixed) --- */
        body[data-theme="mystical"] { 
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%); 
            background-size: 400% 400%;
            animation: float 20s ease-in-out infinite;
        }
        body[data-theme="mystical"] .stApp, body[data-theme="mystical"] h1, body[data-theme="mystical"] h2, body[data-theme="mystical"] h3 { 
            color: white; 
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }
        body[data-theme="mystical"] .user-bubble { 
            background: linear-gradient(135deg, #ff6b6b, #feca57, #ff9ff3); 
            color: white; 
            border: 2px solid rgba(255,255,255,0.2);
        }
        body[data-theme="mystical"] .bot-bubble { 
            background: linear-gradient(135deg, #4ecdc4, #44a08d, #74b9ff); 
            color: white; 
            border: 2px solid rgba(255,255,255,0.2);
        }
        body[data-theme="mystical"] .stTextArea > div > div { 
            background: rgba(255,255,255,0.1); 
            color: white; 
            border-color: #4ecdc4; 
            backdrop-filter: blur(10px);
        }
        body[data-theme="mystical"] .main .stButton > button { 
            background: linear-gradient(135deg, #ff6b6b, #feca57); 
            color: white; 
            box-shadow: 0 0 20px rgba(255,107,107,0.4);
        }

        /* --- Sidebar Styles (Theme-Aware) --- */
        .css-1d391kg {
            background: linear-gradient(180deg, rgba(30, 30, 46, 0.95) 0%, rgba(45, 45, 70, 0.95) 100%);
            backdrop-filter: blur(20px); 
            border-right: 2px solid rgba(255, 255, 255, 0.2);
            box-shadow: 5px 0 25px rgba(0,0,0,0.3);
        }
        .css-1d391kg h3 { 
            color: #ffffff !important; 
            font-weight: 900 !important; 
            font-size: 1.5rem !important; 
            text-shadow: 0 0 20px rgba(255,255,255,0.5) !important; 
            animation: glow 3s ease-in-out infinite;
        }
        .css-1d391kg .stMarkdown p, .css-1d391kg .stSelectbox label, .css-1d391kg .stSlider label { 
            color: #ffffff !important; 
            font-weight: 600 !important; 
        }
        .css-1d391kg .stButton > button { 
            background: linear-gradient(135deg, #ff6b6b, #feca57) !important; 
            color: white !important; 
            border-radius: 20px !important;
            transition: all 0.3s ease !important;
        }
        .css-1d391kg .stButton > button:hover {
            transform: translateY(-2px) scale(1.05) !important;
            box-shadow: 0 8px 25px rgba(255,107,107,0.4) !important;
        }

        /* --- Auth Page Specific Styles --- */
        .auth-container { 
            background: rgba(255, 255, 255, 0.1); 
            backdrop-filter: blur(20px); 
            border: 2px solid rgba(255, 255, 255, 0.2); 
            border-radius: 30px; 
            padding: 3rem; 
            max-width: 450px; 
            margin: 0 auto; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            animation: slideIn 0.8s ease-out;
        }
        .auth-container h1 {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2.5rem;
            background: linear-gradient(45deg, #ff6b6b, #feca57, #4ecdc4, #74b9ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: glow 3s ease-in-out infinite;
        }
        .auth-container .stTextInput > div > div > input { 
            background: rgba(255,255,255,0.1) !important; 
            border: none !important; 
            border-bottom: 3px solid rgba(255,255,255,0.5) !important; 
            border-radius: 10px !important;
            padding: 15px !important;
            color: white !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
        }
        .auth-container .stTextInput > div > div > input:focus {
            border-bottom-color: #4ecdc4 !important;
            background: rgba(255,255,255,0.2) !important;
            transform: scale(1.02);
        }
        .auth-container .stButton > button { 
            width: 100%; 
            margin-top: 2rem; 
            background: linear-gradient(135deg, #ff6b6b, #feca57) !important;
            color: white !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 15px !important;
            font-size: 18px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 8px 25px rgba(255,107,107,0.3);
        }
        .auth-container .stButton > button:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 12px 35px rgba(255,107,107,0.5) !important;
        }
        
        /* Auth page background - NUCLEAR NO TOP SPACING */
        .auth-page {
            min-height: 100vh;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding: 0 !important;
            margin: 0 !important;
            position: relative !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            z-index: 1000 !important;
        }
        
        /* Force auth container to the very top */
        .auth-container {
            margin-top: 0 !important;
            padding-top: 0 !important;
            position: relative !important;
            top: 0 !important;
        }
        
        /* Nuclear option - force ALL elements to top */
        .auth-page *,
        .auth-page .stMarkdown,
        .auth-page .stTextInput,
        .auth-page .stButton,
        .auth-page .stSelectbox,
        .auth-page .stCheckbox {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Hide ALL Streamlit default spacing */
        .stApp > div:first-child,
        .stApp > div:nth-child(2),
        .main .block-container {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Override any remaining Streamlit spacing */
        .stMarkdown, .stTextInput, .stButton {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Ensure forms are visible and accessible */
        .auth-page .stMarkdown,
        .auth-page .stTextInput,
        .auth-page .stButton {
            position: relative !important;
            z-index: 1001 !important;
            visibility: visible !important;
            opacity: 1 !important;
        }
        
        /* Force forms to be at the top - NUCLEAR OPTION */
        .auth-page {
            min-height: 100vh;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding: 0 !important;
            margin: 0 !important;
            position: relative !important;
            top: 0 !important;
        }
        
        /* Override ALL Streamlit default spacing */
        .auth-page * {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Force the auth container to the very top */
        .auth-container {
            margin-top: 0 !important;
            padding-top: 1rem !important;
            position: relative !important;
            top: 0 !important;
        }
        
        /* Hide any elements that might push content down */
        .stApp > div:first-child,
        .stApp > div:nth-child(2),
        .main .block-container {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Enhanced form styling */
        .auth-page .stTextInput > div > div > input,
        .auth-page .stTextInput > div > div > input:focus {
            font-size: 16px !important;
            padding: 15px 20px !important;
            border-radius: 15px !important;
            transition: all 0.3s ease !important;
        }
        
        .auth-page .stButton > button {
            font-size: 18px !important;
            font-weight: bold !important;
            padding: 18px 30px !important;
            border-radius: 25px !important;
            transition: all 0.3s ease !important;
        }
        
        .auth-page .stButton > button:hover {
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 15px 40px rgba(255,107,107,0.4) !important;
        }
        
        /* Floating elements for aesthetic */
        .floating-element {
            position: fixed;
            width: 100px;
            height: 100px;
            background: linear-gradient(45deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
            z-index: -1;
        }
        .floating-element:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
        .floating-element:nth-child(2) { top: 20%; right: 15%; animation-delay: 2s; }
        .floating-element:nth-child(3) { bottom: 20%; left: 20%; animation-delay: 4s; }
        .floating-element:nth-child(4) { bottom: 10%; right: 10%; animation-delay: 6s; }
        
        /* Enhanced DreamBot title effects - SUPER VIBRANT */
        .dreambot-title {
            animation: superGlow 1.5s ease-in-out infinite alternate;
            text-shadow: 0 0 50px #ffffff, 0 0 100px #ffffff, 0 0 150px #ffffff, 0 0 200px #ffffff !important;
            color: #FFFFFF !important;
            font-weight: 900 !important;
        }
        
        .dreambot-subtitle {
            animation: superGlow 2s ease-in-out infinite alternate;
            text-shadow: 0 0 30px #ffffff, 0 0 60px #ffffff, 0 0 90px #ffffff !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }
        
        .dreambot-description {
            animation: superGlow 2.5s ease-in-out infinite alternate;
            text-shadow: 0 0 20px #ffffff, 0 0 40px #ffffff, 0 0 60px #ffffff !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }
        
        @keyframes superGlow {
            from { 
                text-shadow: 0 0 50px #ffffff, 0 0 100px #ffffff, 0 0 150px #ffffff, 0 0 200px #ffffff;
                transform: scale(1);
                filter: brightness(1);
            }
            to { 
                text-shadow: 0 0 100px #ffffff, 0 0 200px #ffffff, 0 0 300px #ffffff, 0 0 400px #ffffff;
                transform: scale(1.05);
                filter: brightness(1.2);
            }
        }
        
        /* Additional vibrant effects */
        .dreambot-title:hover {
            animation: superGlow 0.5s ease-in-out infinite alternate;
            transform: scale(1.1);
        }
        
        .dreambot-subtitle:hover {
            animation: superGlow 0.5s ease-in-out infinite alternate;
            transform: scale(1.05);
        }
        
        .dreambot-description:hover {
            animation: superGlow 0.5s ease-in-out infinite alternate;
            transform: scale(1.03);
        }
        
        /* Force maximum vibrancy */
        .dreambot-title, .dreambot-subtitle, .dreambot-description {
            color: #FFFFFF !important;
            text-shadow: 0 0 50px #ffffff, 0 0 100px #ffffff, 0 0 150px #ffffff, 0 0 200px #ffffff !important;
        }
        
        /* NUCLEAR OPTION - Force forms to the very top */
        .auth-page {
            margin-top: 0 !important;
            padding-top: 0 !important;
            position: relative !important;
            top: 0 !important;
        }
        
        .auth-container {
            margin-top: 0 !important;
            padding-top: 0 !important;
            position: relative !important;
            top: 0 !important;
        }
        
        /* Override ALL remaining Streamlit spacing */
        .stApp,
        .stApp > div,
        .main,
        .main .block-container {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* Force all auth elements to top */
        .auth-page * {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        
        /* NUCLEAR OPTION - Hide ALL top elements */
        .stApp > div:first-child,
        .stApp > div:nth-child(2),
        .stApp > div:nth-child(3),
        .stApp > div:nth-child(4) {
            margin-top: 0 !important;
            padding-top: 0 !important;
            height: 0 !important;
            overflow: hidden !important;
            display: none !important;
        }
        
        /* Force the page to start at the very top */
        body, html {
            margin-top: 0 !important;
            padding-top: 0 !important;
            scroll-padding-top: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

# =======================================================================================
# SECTION 3: UI & APP LOGIC (Main DreamBot App)
# =======================================================================================

def display_sidebar():
    """Displays the main app's sidebar - now with all elements restored."""
    with st.sidebar:
        st.markdown(f"""
            <div style='text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 15px; margin-bottom: 1rem;'>
                <h3 style='margin: 0; color: #4ecdc4;'>👋 Welcome back!</h3>
                <p style='margin: 0.5rem 0 0 0; font-size: 1.1rem; color: white;'><strong>{st.session_state.user}</strong></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("<h3><span style='margin-right: 10px;'>⚙️</span>Settings</h3>", unsafe_allow_html=True)
        
        # Dream Mood Selector (replaces theme switching)
        dream_mood = st.selectbox(
            "🌙 Dream Mood", 
            ["Mystical Vibes ✨", "Chill Energy 😌", "Party Mode 🎉", "Deep Thoughts 🤔"], 
            key="dream_mood", 
            help="Choose the energy for your dream interpretations!"
        )
        
        # Show current mood
        st.markdown(f"<small style='color: rgba(255,255,255,0.6);'>Current mood: {dream_mood}</small>", unsafe_allow_html=True)
        
        # Mood description
        mood_descriptions = {
            "Mystical Vibes ✨": "Spiritual insights with cosmic energy",
            "Chill Energy 😌": "Calm, peaceful interpretations",
            "Party Mode 🎉": "Fun, energetic vibes",
            "Deep Thoughts 🤔": "Philosophical and analytical"
        }
        st.markdown(f"<small style='color: rgba(255,255,255,0.5);'>{mood_descriptions[dream_mood]}</small>", unsafe_allow_html=True)
        
        # Dream Interpretation Style
        interpretation_style = st.selectbox(
            "🎭 Interpretation Style", 
            ["Gen Z Bestie 💅", "Wise Therapist 🧠", "Mystical Guide 🔮", "Comedy Mode 😂"], 
            key="interpretation_style", 
            help="How should DreamBot talk to you?"
        )
        
        # Style description
        style_descriptions = {
            "Gen Z Bestie 💅": "Casual, trendy, with lots of emojis",
            "Wise Therapist 🧠": "Professional, analytical, insightful",
            "Mystical Guide 🔮": "Spiritual, cosmic, mystical vibes",
            "Comedy Mode 😂": "Funny, entertaining, light-hearted"
        }
        st.markdown(f"<small style='color: rgba(255,255,255,0.5);'>{style_descriptions[interpretation_style]}</small>", unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("<h3><span style='margin-right: 10px;'>🎭</span>Personality</h3>", unsafe_allow_html=True)
        vibe = st.select_slider("✨ Vibe Level", options=["Chill 😌", "Medium 😊", "Extra AF 🔥"], value="Medium 😊")
        
        # Dream Category Filter
        dream_category = st.selectbox(
            "🔮 Dream Category", 
            ["All Dreams ✨", "Nightmares 😱", "Lucid Dreams 🌟", "Recurring Dreams 🔄", "Prophetic Dreams 🔮"], 
            key="dream_category", 
            help="Filter dreams by type for better organization"
        )
        
        st.markdown("---")
        st.markdown("<h3><span style='margin-right: 10px;'>⚡️</span>Quick Actions</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Reset", key="sidebar_reset_chat", help="Clear chat history"):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("📖 Guide", key="sidebar_dream_guide", help="How to use DreamBot"):
                st.success("🌙 DreamBot User Guide 🌙")
                st.markdown("""
                **1. 🌙 Describe Your Dream**
                • Be as detailed as possible
                • Include what you saw, heard, felt
                • Mention colors, people, places, objects
                """)
                
                st.markdown("""
                **2. 💭 Share Your Emotions**
                • How did you feel during the dream?
                • Were you scared, happy, confused?
                • Any strong emotions that stood out?
                """)
                
                st.markdown("""
                **3. ✨ Get Your Interpretation**
                • DreamBot will analyze everything
                • You'll get a Gen Z style explanation
                • Keep the conversation going!
                """)
                
                st.info("""
                **🚀 Pro Tips:**
                • The more details, the better the interpretation
                • Dreams about flying often mean freedom
                • Water dreams usually relate to emotions
                • Falling dreams often indicate anxiety
                • Animals in dreams represent your instincts
                """)
        
        st.markdown("---")
        
        # Dream Statistics
        if hasattr(st.session_state, 'messages') and st.session_state.messages:
            dream_count = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
            st.markdown("<h3><span style='margin-right: 10px;'>📊</span>Dream Stats</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 15px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='color: #4ecdc4; margin: 0;'>{dream_count}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;'>Dreams Decoded</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Additional Settings
        st.markdown("<h3><span style='margin-right: 10px;'>🔧</span>Advanced Settings</h3>", unsafe_allow_html=True)
        
        # API Key Status
        api_status = "🟢 Working" if st.session_state.get('api_works', False) else "🔴 Not Working"
        st.markdown(f"<small style='color: rgba(255,255,255,0.7);'>API Status: {api_status}</small>", unsafe_allow_html=True)
        
        # Dream History Length
        dream_history_length = st.slider("📚 Dream History", min_value=5, max_value=50, value=20, help="How many dreams to keep in memory")
        
        # Auto-save dreams
        auto_save = st.checkbox("💾 Auto-save Dreams", value=True, help="Automatically save your dreams")
        
        # Notification preferences
        st.markdown("<h4 style='color: #4ecdc4; margin-top: 1rem;'>🔔 Notifications</h4>", unsafe_allow_html=True)
        email_notifications = st.checkbox("📧 Email Updates", value=False)
        dream_reminders = st.checkbox("⏰ Dream Reminders", value=True)
        
        st.markdown("---")
        
        # User Profile
        st.markdown("<h3><span style='margin-right: 10px;'>👤</span>Profile</h3>", unsafe_allow_html=True)
        
        # User stats
        if hasattr(st.session_state, 'messages') and st.session_state.messages:
            total_dreams = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
            st.metric("Total Dreams", total_dreams)
        
        # Account actions
        if st.button("🚪 Log Out", key="sidebar_log_out", use_container_width=True, help="Sign out of your account"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.messages = []
            st.session_state.page = "login"
            st.rerun()

def dreambot_app():
    """The main DreamBot application page."""
    
    # Initialize messages before displaying sidebar
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    display_sidebar()
    
    # Add floating background elements for main app
    st.markdown("""
        <div class="floating-element" style="top: 15%; right: 5%; width: 80px; height: 80px;"></div>
        <div class="floating-element" style="top: 25%; left: 8%; width: 60px; height: 60px;"></div>
        <div class="floating-element" style="bottom: 30%; right: 15%; width: 70px; height: 70px;"></div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem; padding: 2rem; background: rgba(0,0,0,0.3); border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);'>
            <h1 class='dreambot-title' style='font-size: 4rem; margin-bottom: 0; color: #FFFFFF; font-weight: 900; letter-spacing: 2px; text-shadow: 2px 2px 8px rgba(0,0,0,0.8), 0 0 20px rgba(255,255,255,0.3);'>
                ✨ DreamBot ✨
            </h1>
            <h3 class='dreambot-subtitle' style='color: #FFFFFF; font-size: 1.8rem; margin-top: 0.5rem; font-weight: 700; text-shadow: 2px 2px 6px rgba(0,0,0,0.7), 0 0 15px rgba(255,255,255,0.2);'>
                Your Gen Z Dream Interpreter 🔮✨
            </h3>
            <p class='dreambot-description' style='color: #FFFFFF; font-size: 1.3rem; margin-top: 0.5rem; font-weight: 600; text-shadow: 1px 1px 4px rgba(0,0,0,0.6), 0 0 10px rgba(255,255,255,0.1);'>
                Welcome, dreamer! ✨ Share your dreams and let me decode them with aesthetic vibes and spiritual energy! 🌙💫
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Chat input area at the top
    with st.form(key='dream_form', clear_on_submit=True):
        dream_input = st.text_area("Tell me your dream...", placeholder="I had a dream I was flying over a rainbow city...", height=100, key="dream_input_area")
        submitted = st.form_submit_button(label="Decode My Dream ✨")
        
        if submitted:
            if dream_input.strip() == "":
                st.warning("Spill the tea! What's your dream all about?")
            else:
                st.session_state.messages.append({"role": "user", "content": dream_input})
                with st.spinner("Decoding the vibes... 🔮"):
                    bot_response = get_dream_interpretation_from_api(dream_input)
                    st.session_state.messages.append({"role": "bot", "content": bot_response})
                st.rerun()

    # Display chat history below the input
    if st.session_state.messages:
        st.markdown("---")
        st.markdown("### 💭 Dream Chat History")
        
        for msg in st.session_state.messages:
            is_user = msg["role"] == "user"
            bubble_class = "user-bubble" if is_user else "bot-bubble"
            name = "You" if is_user else "🧚‍♀️ DreamBot"
            st.markdown(f"<div class='{bubble_class}'><strong>{name}:</strong> {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); margin: 2rem 0;'>
            <h3 style='color: #FFFFFF; font-size: 2rem; margin-bottom: 1rem; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);'>
                💫 Ready to decode your dreams? 💫
            </h3>
            <p style='color: #FFFFFF; font-size: 1.2rem; margin-bottom: 1rem; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);'>
                ✨ Share your dream above and let the magic begin! ✨
            </p>
            <p style='color: rgba(255,255,255,0.8); font-size: 1rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.5);'>
                Tell me about flying dreams, mysterious places, or any wild adventures your mind created! 🌙🦋
            </p>
        </div>
        """, unsafe_allow_html=True)

# =======================================================================================
# SECTION 4: AUTHENTICATION (Login & Sign Up)
# =======================================================================================

def login_page():
    # Add floating background elements
    st.markdown("""
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-page">', unsafe_allow_html=True)
    
    # Position the form at the top
    st.markdown("<div style='margin-top: 0;'>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='auth-container'>
            <h1>✨ Welcome Back, Dreamer ✨</h1>
            <p style='text-align: center; color: rgba(255,255,255,0.8); font-size: 18px; margin-bottom: 2rem;'>
                Ready to decode some more dreams? Let's get this bread! 🍞
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create a centered form layout
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Username section
        st.markdown("### 👤 Your Dreamer Name")
        username = st.text_input(
            "Username", 
            key="login_username", 
            placeholder="Enter your username...",
            help="The username you used when signing up"
        )
        
        # Password section
        st.markdown("### 🔒 Your Secret Handshake")
        password = st.text_input(
            "Password", 
            type="password", 
            key="login_password", 
            placeholder="Enter your password...",
            help="The password you created for your account"
        )
        
        # Spacing
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Login button
        if st.button("🚀 Let's Decode Some Dreams! 🚀", key="login_button", use_container_width=True, type="primary"):
            if not username or not password:
                st.error("😅 Please enter both username and password!")
            elif username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.balloons()
                st.success(f"🎉 Welcome back, {username}! ✨")
                st.info("🚀 Ready to decode some dreams? Let's go!")
                time.sleep(2)
                st.rerun()
            else:
                st.error("😅 Oof, wrong deets. Try again? 🤔")
        
        # Spacing
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Navigation section
        st.markdown("---")
        st.markdown("### 🆕 New to the Dream Team?")
        if st.button("🌟 Sign Me Up! 🌟", key="nav_to_signup", use_container_width=True):
            st.session_state.page = "signup"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def signup_page():
    # Add floating background elements
    st.markdown("""
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
        <div class="floating-element"></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-page">', unsafe_allow_html=True)
    
    # Position the form at the top
    st.markdown("<div style='margin-top: 0;'>", unsafe_allow_html=True)
    
    # Main signup container
    st.markdown("""
        <div class='auth-container'>
            <h1>🌟 Join the Dream Team 🌟</h1>
            <p style='text-align: center; color: rgba(255,255,255,0.8); font-size: 18px; margin-bottom: 2rem;'>
                Ready to become a dream decoding legend? Let's make it happen! ✨
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create a centered form layout
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Username section
        st.markdown("### 👤 Choose Your Dreamer Name")
        username = st.text_input(
            "Username", 
            key="signup_username", 
            placeholder="Enter a unique username...",
            help="This will be your display name in the app"
        )
        
        # Password section
        st.markdown("### 🔐 Create Your Secret Handshake")
        password = st.text_input(
            "Password", 
            type="password", 
            key="signup_password", 
            placeholder="Create a strong password...",
            help="Make it secure but memorable"
        )
        
        # Password strength indicator
        if password:
            if len(password) < 6:
                st.warning("⚠️ Password should be at least 6 characters long")
            elif len(password) < 8:
                st.info("💪 Good password strength")
            else:
                st.success("🔒 Strong password! You're all set")
        
        # Confirm password section
        st.markdown("### ✅ Confirm Your Password")
        confirm_password = st.text_input(
            "Confirm Password", 
            type="password", 
            key="signup_confirm_password", 
            placeholder="Type your password again...",
            help="Make sure both passwords match"
        )
        
        # Password match indicator
        if confirm_password and password:
            if password == confirm_password:
                st.success("✅ Passwords match perfectly!")
            else:
                st.error("❌ Passwords don't match. Try again!")
        
        # Spacing
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create account button
        if st.button("💫 Create My Dream Account 💫", key="signup_button", use_container_width=True, type="primary"):
            if not all([username, password, confirm_password]):
                st.error("😅 Please fill out all the fields, bestie!")
            elif len(password) < 6:
                st.error("😱 Password must be at least 6 characters long!")
            elif password != confirm_password:
                st.error("😱 Oof, the passwords don't match!")
            elif username in st.session_state.users:
                st.error("😅 That username is already taken. Try another one!")
            else:
                st.session_state.users[username] = password
                st.balloons()
                st.success(f"🎉 Yesss, you're in, {username}! 🥳")
                st.info("✨ Welcome to the Dream Team! Now head to the login page to start your journey.")
                time.sleep(3)
                st.session_state.page = "login"
                st.rerun()
        
        # Spacing
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Navigation section
        st.markdown("---")
        st.markdown("### 🔙 Already Part of the Dream Team?")
        if st.button("🚪 Take Me to Login 🚪", key="nav_to_login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# =======================================================================================
# SECTION 5: MAIN ROUTER
# =======================================================================================

def main():
    # --- IMPORTANT: The ONE AND ONLY st.set_page_config() call ---
    st.set_page_config(
        page_title="DreamBot", 
        page_icon="✨", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state variables if they don't exist
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False  # Back to normal - show login first
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "users" not in st.session_state:
        st.session_state.users = {"afra": "vibecheck"} # Default user for testing
    if "user" not in st.session_state:
        st.session_state.user = None
    if "dream_mood" not in st.session_state:
        st.session_state.dream_mood = "Mystical Vibes ✨" # Default mood

    load_css() # Load all CSS styles

    # Set a fixed mystical theme for the app
    st.markdown('<body data-theme="mystical">', unsafe_allow_html=True)
    
    # Add mystical theme styling
    st.markdown("""
        <style>
            .stTextArea > div > div { 
                background: rgba(255,255,255,0.1) !important; 
                color: white !important;
                border-color: #4ecdc4 !important;
            }
            .stSelectbox > div > div { 
                background: rgba(255,255,255,0.1) !important; 
                color: white !important;
            }
            .stSelectbox > div > div > div { 
                background: rgba(255,255,255,0.1) !important; 
                color: white !important;
            }
            .stTextInput > div > div > input { 
                background: rgba(255,255,255,0.1) !important; 
                color: white !important;
            }
            .stMarkdown { color: white !important; }
            .stInfo { 
                background: rgba(78,205,196,0.2) !important; 
                border-color: #4ecdc4 !important;
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main routing logic
    if st.session_state.logged_in:
        dreambot_app()
    else:
        # Hide the sidebar for authentication pages using CSS
        st.markdown("<style>.css-1d391kg {display: none;}</style>", unsafe_allow_html=True)
        
        # Force auth pages to start at the very top - NUCLEAR OPTION
        st.markdown("""
        <style>
        /* Nuclear option - force auth pages to top */
        .stApp > div:first-child { margin-top: 0 !important; padding-top: 0 !important; }
        .stApp > div:nth-child(2) { margin-top: 0 !important; padding-top: 0 !important; }
        .main .block-container { margin-top: 0 !important; padding-top: 0 !important; }
        .stMarkdown:first-child { margin-top: 0 !important; padding-top: 0 !important; }
        .stMarkdown { margin-top: 0 !important; padding-top: 0 !important; }
        .stTextInput { margin-top: 0 !important; padding-top: 0 !important; }
        .stButton { margin-top: 0 !important; padding-top: 0 !important; }
        
        /* Force everything to start at the very top */
        body { margin-top: 0 !important; padding-top: 0 !important; }
        html { margin-top: 0 !important; padding-top: 0 !important; }
        
        /* Only hide specific elements that might push content down, not all content */
        .stApp > div:first-child:empty,
        .stApp > div:nth-child(2):empty {
            margin-top: 0 !important;
            padding-top: 0 !important;
            height: 0 !important;
            overflow: hidden !important;
        }
        </style>
        
        <script>
        // Only scroll to top for auth pages
        window.onload = function() {
            window.scrollTo(0, 0);
            
            // Force the auth page to be at the top
            const authPage = document.querySelector('.auth-page');
            if (authPage) {
                authPage.style.marginTop = '0px';
                authPage.style.paddingTop = '0px';
                authPage.style.position = 'relative';
                authPage.style.top = '0px';
            }
        };
        </script>
        """, unsafe_allow_html=True)
        
        if st.session_state.page == "login":
            login_page()
        elif st.session_state.page == "signup":
            signup_page()

if __name__ == "__main__":
    main()