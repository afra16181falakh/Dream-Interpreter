import streamlit as st
import streamlit.components.v1 as components

def set_page_config():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="✨ DreamBot - Your Gen Z Dream Interpreter",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def get_css():
    """Returns unified CSS for the entire app."""
    return """
    <style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        backdrop-filter: blur(15px);
    }
    
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 900;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
    }
    
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600;
    }
    
    /* Header Styles */
    .header-container {
        text-align: center;
        padding: 2rem 0;
    }
    
    .header-title {
        font-size: 3rem;
        margin-bottom: 0;
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    
    .header-subtitle {
        margin-top: 0.5rem;
        opacity: 0.9;
        font-size: 1.5rem;
    }
    
    /* Chat Styles */
    .chat-message {
        padding: 15px 20px;
        border-radius: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .user-message {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        color: white;
        margin-left: 20%;
    }
    
    .bot-message {
        background: rgba(255,255,255,0.15);
        color: white;
        margin-right: 20%;
        backdrop-filter: blur(10px);
    }
    
    /* Input Styles */
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid rgba(255,255,255,0.3);
        background: rgba(255,255,255,0.1);
        color: white;
        font-size: 1rem;
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(255,255,255,0.7);
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        .user-message, .bot-message {
            margin-left: 5%;
            margin-right: 5%;
        }
    }
    </style>
    """

def add_custom_css():
    """Add custom CSS styling."""
    st.markdown(get_css(), unsafe_allow_html=True)

def display_header():
    """Display the main header."""
    st.markdown("""
    <div class='header-container'>
        <h1 class='header-title'>✨ DreamBot ✨</h1>
        <h3 style='margin-top: 0; opacity: 0.8;'>Your Gen Z Dream Interpreter</h3>
        <p style='font-size: 1.2rem; opacity: 0.9;'>Tell me your wildest dreams and I'll decode them with ✨vibes✨</p>
    </div>
    """, unsafe_allow_html=True)

def display_chat_message(message, is_user=False):
    """Display a chat message with styling."""
    css_class = "user-message" if is_user else "bot-message"
    sender = "You" if is_user else "🧚‍♀️ DreamBot"
    st.markdown(f"""
    <div class='chat-message {css_class}'>
        <strong>{sender}:</strong> {message}
    </div>
    """, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar content."""
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        
        st.selectbox("Theme", ["Dark Mode"], index=0, disabled=True)
        
        st.markdown("### 🎨 Personality")
        st.select_slider("Vibe Level", 
                        options=["Chill", "Medium", "Extra AF"], 
                        value="Medium")
        
        st.markdown("### ⚡️ Quick Actions")
        
        if st.button("🔄 Reset Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        if st.button("📖 Dream Guide", use_container_width=True):
            st.info("""
            **How to use:**
            1. Type your dream in detail
            2. Include emotions you felt
            3. Mention any symbols
            4. Get your ✨vibe check✨
            """)
        
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; opacity: 0.8;'>
            <p>Made with 💖 for Gen Z dreamers</p>
            <p><strong>Made by Afra ✨</strong></p>
        </div>
        """)

# Remove the main() function since this is now a component library
# The main() function was causing conflicts with the main app.py
