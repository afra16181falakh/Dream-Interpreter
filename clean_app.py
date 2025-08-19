import streamlit as st
import time
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError

# Configure Google API
def configure_google_api():
    api_keys = [
        "AIzaSyAYlCXPS3FqLVU8i1_aMFoe9cHjnaxQCfg",
        "AIzaSyCMIgg735oFJTXiHQ3gWFKh8aIcKedCaME",
        "AIzaSyDLoVVBhxm0NMf9UafHRFasC7TwOOycxXI",
        "AIzaSyB9PO9OUbWzYKnJCFv5jr283-mjGpPHyIU"
    ]
    
    for i, key in enumerate(api_keys):
        try:
            genai.configure(api_key=key)
            # Test the API with a simple request
            model = genai.GenerativeModel('gemini-1.5-flash')
            test_response = model.generate_content("Hello")
            print(f"API configured successfully with key at index: {i}")
            return True
        except Exception as e:
            print(f"Failed to configure API with key {i}: {e}")
            continue
    return False

# Initialize API
api_working = configure_google_api()

def get_dream_interpretation(dream_text, mood="Mystical Vibes ✨", style="Gen Z Bestie 💅", category="All Dreams ✨"):
    """Get dream interpretation from Google's Gemini AI with fallback responses."""
    
    # If API isn't working, provide a creative fallback response
    if not api_working:
        return get_fallback_interpretation(dream_text, mood, style)
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        You are DreamBot. Respond ONLY as a {style} with {mood} energy.
        
        Dream Category: {category}
        Dream: "{dream_text}"
        
        IMPORTANT: Respond ONLY in the {style} style with {mood} energy. Do not mix styles.
        
        Style Rules:
        - Gen Z Bestie 💅: Trendy slang, emojis, "bestie", "sis", "queen", casual
        - Wise Therapist 🧠: Professional, psychological analysis, therapeutic language
        - Mystical Guide 🔮: Spiritual, cosmic, mystical, "dear soul", ethereal
        - Comedy Mode 😂: Funny, jokes, entertaining, light-hearted humor
        
        Keep under 150 words. Stay in character!
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except ResourceExhausted:
        return "Whoa! My dream-decoding powers are recharging. Try again in a few minutes! ⚡"
    except GoogleAPIError as gae:
        return get_fallback_interpretation(dream_text, mood, style)
    except Exception as e:
        return get_fallback_interpretation(dream_text, mood, style)

def get_fallback_interpretation(dream_text, mood, style):
    """Provide creative fallback interpretations when API isn't available."""
    import random
    
    # Analyze dream for common symbols
    dream_lower = dream_text.lower()
    symbols = []
    
    if any(word in dream_lower for word in ['fly', 'flying', 'float']):
        symbols.append("flying (freedom, escape from limitations)")
    if any(word in dream_lower for word in ['water', 'ocean', 'sea', 'river']):
        symbols.append("water (emotions, subconscious)")
    if any(word in dream_lower for word in ['house', 'home', 'building']):
        symbols.append("buildings (your psyche, different aspects of self)")
    if any(word in dream_lower for word in ['animal', 'dog', 'cat', 'bird']):
        symbols.append("animals (instincts, natural desires)")
    if any(word in dream_lower for word in ['chase', 'chasing', 'running']):
        symbols.append("being chased (avoiding something in waking life)")
    
    if style == "Gen Z Bestie 💅":
        responses = [
            f"Okay bestie, this dream is giving me major {mood.split()[0].lower()} energy! ✨ The symbols I'm picking up: {', '.join(symbols) if symbols else 'pure vibes'}. This could mean you're processing some deep feelings or maybe your subconscious is just being extra creative! Either way, your mind is serving looks even while you sleep! 💅✨",
            f"Sis, your dream is absolutely sending me! 🔥 Based on the {mood.split()[0].lower()} vibes, I think your subconscious is trying to tell you something important. {symbols[0] if symbols else 'The overall energy'} suggests you might be going through some changes or growth. Keep dreaming those dreams, queen! 👑✨"
        ]
    elif style == "Wise Therapist 🧠":
        dream_tone = "the dream's emotional tone"
        responses = [
            f"This dream reflects interesting psychological patterns. The {mood.split()[0].lower()} nature suggests your mind is processing experiences through symbolic representation. Key elements: {', '.join(symbols) if symbols else 'the overall narrative structure'} indicate potential areas of personal growth or unresolved emotions seeking integration. 🧠✨",
            f"From a therapeutic perspective, your dream shows healthy psychological processing. The symbolic content, particularly {symbols[0] if symbols else dream_tone}, may represent your psyche working through current life situations. This is a positive sign of mental wellness and self-reflection. 🌟"
        ]
    elif style == "Mystical Guide 🔮":
        dream_essence = "The dream's essence"
        responses = [
            f"The cosmic energies speak through your dream, dear soul! ✨ The {mood.split()[0].lower()} vibrations reveal that the universe is sending you messages through {', '.join(symbols) if symbols else 'ethereal symbolism'}. Your spirit guides are communicating important wisdom about your life path. Trust in the mystical journey ahead! 🔮🌙",
            f"Sacred dreamer, your vision carries profound spiritual significance! The {mood.split()[0].lower()} energy channels ancient wisdom through symbolic language. {symbols[0] if symbols else dream_essence} connects you to higher consciousness and divine guidance. Meditate on these messages from beyond the veil! ✨🌟"
        ]
    else:  # Comedy Mode
        committee_quote = "let's add some"
        plot_twists = "some wild plot twists"
        responses = [
            f"Haha, okay so your brain decided to throw a {mood.split()[0].lower()} party while you were sleeping! 😂 The dream committee in your head was like '{committee_quote} {symbols[0] if symbols else 'random chaos'}' and honestly? They delivered! Your subconscious has a great sense of humor - maybe it should start a comedy show! 🎭✨",
            f"LMAO your dream is giving me serious {mood.split()[0].lower()} comedy vibes! 😂 It's like your brain was bored and decided to create its own Netflix series starring you and {', '.join(symbols[:2]) if len(symbols) >= 2 else plot_twists}. 10/10 would watch this dream movie! 🍿✨"
        ]
    
    return random.choice(responses)

def load_css():
    """Load clean, working CSS."""
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
        
        /* Chat Messages */
        .user-bubble {
            background: linear-gradient(135deg, #ff6b6b, #feca57);
            color: white;
            padding: 20px;
            border-radius: 25px;
            margin: 15px 0;
            margin-left: 20%;
        }
        
        .bot-bubble {
            background: linear-gradient(135deg, #4ecdc4, #44a08d);
            color: white;
            padding: 20px;
            border-radius: 25px;
            margin: 15px 0;
            margin-right: 20%;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(30, 30, 46, 0.95) 0%, rgba(45, 45, 70, 0.95) 100%);
            backdrop-filter: blur(20px);
        }
        
        [data-testid="stSidebar"] h3 {
            color: white !important;
            font-weight: 900 !important;
        }
        
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

def login_page():
    """Display login page."""
    st.markdown("""
        <div class='auth-container'>
            <h1>✨ Welcome Back, Dreamer ✨</h1>
            <p style='text-align: center; color: rgba(255,255,255,0.8); font-size: 18px; margin-bottom: 2rem;'>
                Ready to decode some more dreams? Let's get this bread! 🍞
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("### 👤 Your Dreamer Name")
        username = st.text_input("Username", key="login_username", placeholder="Enter your username...")
        
        st.markdown("### 🔒 Your Secret Handshake")
        password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password...")
        
        if st.button("🚀 Let's Dream Together! 🚀", key="login_button", use_container_width=True):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success(f"Welcome back, {username}! ✨")
                st.rerun()
            else:
                st.error("Hmm, that doesn't match our records. Try again! 🤔")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🌟 New Dreamer? Sign Up! 🌟", key="switch_to_signup", use_container_width=True):
            st.session_state.page = "signup"
            st.rerun()

def signup_page():
    """Display signup page."""
    st.markdown("""
        <div class='auth-container'>
            <h1>✨ Join the Dream Squad ✨</h1>
            <p style='text-align: center; color: rgba(255,255,255,0.8); font-size: 18px; margin-bottom: 2rem;'>
                Ready to unlock the secrets of your subconscious? Let's go! 🌙
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("### 👤 Choose Your Dreamer Name")
        username = st.text_input("Username", key="signup_username", placeholder="Pick a cool username...")
        
        st.markdown("### 🔒 Create Your Secret Handshake")
        password = st.text_input("Password", type="password", key="signup_password", placeholder="Make it secure...")
        
        if st.button("🎉 Join the Dream Squad! 🎉", key="signup_button", use_container_width=True):
            if username and password:
                if username not in st.session_state.users:
                    st.session_state.users[username] = password
                    st.session_state.logged_in = True
                    st.session_state.user = username
                    st.success(f"Welcome to the squad, {username}! ✨")
                    st.rerun()
                else:
                    st.error("That username is already taken! Try another one! 🤷‍♀️")
            else:
                st.error("Please fill in both fields! 📝")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        if st.button("🚪 Already have an account? Login! 🚪", key="switch_to_login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

def display_sidebar():
    """Display sidebar with all functions."""
    with st.sidebar:
        st.markdown(f"### 👋 Hey, {st.session_state.user}!")
        
        st.markdown("---")
        st.markdown("### ⚙️ Settings")
        
        # Dream Mood
        dream_mood = st.selectbox(
            "🌙 Dream Mood", 
            ["Mystical Vibes ✨", "Chill Vibes 😌", "Cosmic Energy 🌌", "Dreamy Feels 💭"], 
            key="dream_mood_selector"
        )
        st.session_state.dream_mood = dream_mood
        
        # Interpretation Style
        interpretation_style = st.selectbox(
            "🎭 Interpretation Style", 
            ["Gen Z Bestie 💅", "Wise Therapist 🧠", "Mystical Guide 🔮", "Comedy Mode 😂"], 
            key="interpretation_style_selector"
        )
        st.session_state.interpretation_style = interpretation_style
        
        st.markdown("---")
        st.markdown("### 🎭 Personality")
        vibe = st.select_slider("✨ Vibe Level", options=["Chill 😌", "Medium 😊", "Extra AF 🔥"], value="Medium 😊")
        
        # Dream Category Filter
        dream_category = st.selectbox(
            "🔮 Dream Category", 
            ["All Dreams ✨", "Nightmares 😱", "Lucid Dreams 🌟", "Recurring Dreams 🔄", "Prophetic Dreams 🔮"],
            key="dream_category_selector"
        )
        st.session_state.dream_category = dream_category
        
        st.markdown("---")
        st.markdown("### ⚡️ Quick Actions")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Reset", help="Clear chat history"):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.button("📖 Guide", help="How to use DreamBot"):
                st.info("""
                🌙 **How to use DreamBot:**
                1. Describe your dream in detail
                2. Include emotions you felt
                3. Mention any symbols
                4. Get your ✨vibe check✨
                """)
        
        # Logout
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

def dreambot_app():
    """Main DreamBot application."""
    display_sidebar()
    
    # Header
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(0,0,0,0.3); border-radius: 20px; margin: 2rem;'>
        <h1 style='color: white; font-size: 4rem;'>✨ DreamBot ✨</h1>
        <h3 style='color: white; font-size: 1.8rem;'>Your Gen Z Dream Interpreter 🔮✨</h3>
        <p style='color: white; font-size: 1.3rem;'>Welcome, dreamer! ✨ Share your dreams and let me decode them! 🌙💫</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class='user-bubble'>
                <strong>You:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='bot-bubble'>
                <strong>🧚‍♀️ DreamBot:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # Dream input form
    with st.form("dream_form", clear_on_submit=True):
        dream_input = st.text_area(
            "✨ Tell me your dream...", 
            placeholder="I had this crazy dream where I was flying over a purple ocean...",
            height=100
        )
        submitted = st.form_submit_button("🔮 Decode My Dream ✨")
        
        if submitted and dream_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": dream_input})
            
            # Get interpretation using user's selected settings
            with st.spinner("🔮 Decoding your dream..."):
                interpretation = get_dream_interpretation(
                    dream_input, 
                    st.session_state.get('dream_mood', 'Mystical Vibes ✨'),
                    st.session_state.get('interpretation_style', 'Gen Z Bestie 💅'),
                    st.session_state.get('dream_category', 'All Dreams ✨')
                )
            
            # Clean the response thoroughly
            clean_interpretation = interpretation.replace("</div>", "").replace("<div>", "").replace("<div", "").replace(">", "").replace("<", "").strip()
            st.session_state.messages.append({"role": "assistant", "content": clean_interpretation})
            st.rerun()
    

    
    # Empty state
    if not st.session_state.messages:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 20px; margin: 2rem;'>
            <h3 style='color: white; font-size: 2rem;'>💫 Ready to decode your dreams? 💫</h3>
            <p style='color: white; font-size: 1.2rem;'>✨ Share your dream above and let the magic begin! ✨</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application function."""
    st.set_page_config(
        page_title="DreamBot", 
        page_icon="✨", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "users" not in st.session_state:
        st.session_state.users = {"afra": "vibecheck"}
    if "user" not in st.session_state:
        st.session_state.user = None
    if "dream_mood" not in st.session_state:
        st.session_state.dream_mood = "Mystical Vibes ✨"
    
    load_css()
    
    # Routing
    if st.session_state.logged_in:
        dreambot_app()
    else:
        # Hide sidebar for auth pages
        st.markdown("<style>[data-testid='stSidebar'] {display: none;}</style>", unsafe_allow_html=True)
        
        if st.session_state.page == "login":
            login_page()
        elif st.session_state.page == "signup":
            signup_page()

if __name__ == "__main__":
    main()