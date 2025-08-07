import streamlit as st
from PIL import Image
import base64

def set_page_config():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="✨ DreamBot - Your Gen Z Dream Interpreter",
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def get_theme_css(theme):
    """Get CSS based on selected theme."""
    if theme == "Dark Mode":
        return get_dark_theme_css()
    else:
        return get_light_theme_css()

def get_dark_theme_css():
    """CSS for dark mode."""
    return """
    <style>
    /* Dark Mode - Mystical & Dreamy */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Gen Z Aesthetic Elements */
    .gen-z-glow {
        text-shadow: 0 0 20px rgba(255, 107, 107, 0.8), 0 0 40px rgba(255, 107, 107, 0.6);
    }
    
    /* Prominent branding */
    .afra-branding {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        text-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Chat bubbles */
    .user-bubble {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        color: white;
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        animation: slideIn 0.5s ease-out;
    }
    
    .bot-bubble {
        background: linear-gradient(135deg, #4ecdc4, #44a08d);
        color: white;
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        animation: slideIn 0.5s ease-out;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #feca57);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Text areas */
    .stTextArea > div > div {
        border-radius: 15px;
        border: 2px solid #4ecdc4;
        background: rgba(255,255,255,0.1);
        color: white; /* Text color in dark mode input */
    }
    
    /* Headers */
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Sidebar - Dark Mode */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(102, 126, 234, 0.9) 0%, rgba(118, 75, 162, 0.9) 100%);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Prominent sidebar styling for dark mode */
    .css-1d391kg .stMarkdown h3 { /* Target sidebar headings (Settings, Personality, Quick Actions) */
        color: #ffffff !important; /* Full white */
        font-weight: 900 !important; /* Extra bold */
        font-size: 1.5rem !important; /* Larger font size */
        margin-bottom: 1rem !important;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.7) !important; /* Strong dark shadow */
    }
    
    .css-1d391kg .stMarkdown p,
    .css-1d391kg .stSelectbox label,
    .css-1d391kg .stSlider label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .css-1d391kg .stSelectbox > div > div {
        color: white !important;
        background: rgba(255,255,255,0.15) !important;
        border: 2px solid rgba(255, 107, 107, 0.5) !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
    }
    
    .css-1d391kg .stSelectbox > div > div:hover {
        background: rgba(255,255,255,0.25) !important;
        border-color: rgba(255, 107, 107, 0.8) !important;
    }
    
    /* Enhanced sidebar buttons */
    .css-1d391kg .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #feca57) !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .css-1d391kg .stButton > button:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
    }
    </style>
    """

def get_light_theme_css():
    """CSS for light mode."""
    return """
    <style>
    /* Light Mode - Clean & Instagram-inspired */
    .stApp {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 50%, #fd79a8 100%);
        color: #2d3436; /* Default text color for light mode */
    }
    
    /* Prominent branding for light mode */
    .afra-branding-light {
        background: linear-gradient(135deg, #fd79a8, #e84393);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        text-shadow: 0 0 5px rgba(253, 121, 168, 0.3);
    }
    
    /* Chat bubbles */
    .user-bubble {
        background: white;
        color: #2d3436; /* Dark text for user bubble in light mode */
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
        border: 2px solid #fd79a8;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease-out;
    }
    
    .bot-bubble {
        background: white;
        color: #2d3436; /* Dark text for bot bubble in light mode */
        padding: 15px;
        border-radius: 20px;
        margin: 10px 0;
        border: 2px solid #74b9ff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        animation: slideIn 0.5s ease-out;
    }
    
    /* Buttons */
    .stButton > button {
        background: white;
        color: #fd79a8;
        border: 2px solid #fd79a8;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: bold;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: #fd79a8;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    /* Text areas */
    .stTextArea > div > div {
        border-radius: 15px;
        border: 2px solid #74b9ff;
        background: white;
        color: #2d3436; /* Make text dark in light mode input */
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #2d3436; /* Dark headers for light mode */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Sidebar - Light Mode */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(255, 234, 167, 0.9) 0%, rgba(250, 177, 160, 0.9) 50%, rgba(253, 121, 168, 0.9) 100%);
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    /* Prominent sidebar styling for light mode */
    .css-1d391kg .stMarkdown h3 { /* Target sidebar headings (Settings, Personality, Quick Actions) */
        color: #ffffff !important; /* Full white */
        font-weight: 900 !important; /* Extra bold */
        font-size: 1.6rem !important; /* Slightly larger font size than dark mode */
        margin-bottom: 1rem !important;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8) !important; /* Strong dark shadow */
    }
    
    .css-1d391kg .stMarkdown p,
    .css-1d391kg .stSelectbox label {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        text-shadow: 2px 2px 3px rgba(0,0,0,0.6) !important;
    }
    
    .css-1d391kg .stSelectbox > div > div {
        color: #2d3436 !important; /* Text color inside the selectbox dropdown */
        background: rgba(255,255,255,0.95) !important;
        border: 2px solid #fd79a8 !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
    }
    
    .css-1d391kg .stSelectbox > div > div:hover {
        background: rgba(255,255,255,1) !important;
        border-color: #e84393 !important;
    }
    
    /* Slider text ("Chill", "Medium", "Extra AF") */
    .css-1d391kg .stSlider .st-cq { 
        color: white !important; 
        font-weight: 900 !important; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7) !important; 
    }

    /* Slider Track and Thumb Colors for Light Mode */
    .css-1d391kg .stSlider .st-ce { /* Active (filled) portion of the slider track */
        background-color: #fd79a8 !important; /* Primary pink from theme */
    }

    .css-1d391kg .stSlider .st-cg { /* Inactive (unfilled) portion of the slider track */
        background-color: rgba(255, 255, 255, 0.7) !important; /* Translucent white */
    }

    .css-1d391kg .stSlider .st-cf { /* Slider thumb (draggable circle) */
        background-color: white !important;
        border: 2px solid #fd79a8 !important; /* Pink border */
        box-shadow: 0 0 8px rgba(253, 121, 168, 0.7) !important; /* Pink glow/shadow */
    }
    
    /* Enhanced sidebar buttons for light mode */
    .css-1d391kg .stButton > button {
        background: linear-gradient(135deg, #fd79a8, #e84393) !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }
    
    .css-1d391kg .stButton > button:hover {
        transform: translateY(-2px) scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
    }
    </style>
    """

def add_custom_css():
    """Add custom CSS styling based on selected theme."""
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark Mode"
    
    css = get_theme_css(st.session_state.theme)
    st.markdown(css, unsafe_allow_html=True)

def display_header():
    """Display the main header based on theme."""
    if st.session_state.theme == "Dark Mode":
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='font-size: 3rem; margin-bottom: 0;'>✨ DreamBot ✨</h1>
            <h3 style='margin-top: 0; opacity: 0.8;'>Your Gen Z Dream Interpreter 🌙</h3>
            <p style='font-size: 1.2rem; opacity: 0.9;'>Tell me your wildest dreams and I'll decode them with ✨vibes✨</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='font-size: 3rem; margin-bottom: 0; color: #fd79a8;'>✨ DreamBot ✨</h1>
            <h3 style='margin-top: 0; color: #74b9ff;'>Your Gen Z Dream Interpreter 🌸</h3>
            <p style='font-size: 1.2rem; color: #636e72;'>Tell me your dreams and I'll decode them with ✨aesthetic✨ vibes</p>
        </div>
        """, unsafe_allow_html=True)

def display_chat_message(message, is_user=False):
    """Display a chat message with styling."""
    if is_user:
        st.markdown(f"""
        <div class='user-bubble'>
            <strong>You:</strong> {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='bot-bubble'>
            <strong>🧚‍♀️ DreamBot:</strong> {message}
        </div>
        """, unsafe_allow_html=True)

def display_sidebar():
    """Display sidebar content."""
    with st.sidebar:
        st.markdown("### 🎭 Settings")
        
        # Theme toggle
        theme = st.selectbox(
            "Theme", 
            ["Dark Mode", "Light Mode"], 
            index=0 if st.session_state.theme == "Dark Mode" else 1
        )
        
        # Update theme when changed
        if theme != st.session_state.theme:
            st.session_state.theme = theme
            st.rerun()
        
        # Personality settings
        st.markdown("### 🎨 Personality")
        personality = st.select_slider(
            "Vibe Level",
            options=["Chill", "Medium", "Extra AF"],
            value="Medium"
        )
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🔄 Reset Chat"):
            st.session_state.messages = []
            st.rerun()
        
        if st.button("📖 Dream Guide"):
            st.info("""
            **How to use:**
            1. Type your dream in detail
            2. Include emotions you felt
            3. Mention any symbols
            4. Get your ✨vibe check✨
            """)
        
        # Footer
        st.markdown("---")
        # Conditional branding for light/dark mode
        if st.session_state.theme == "Dark Mode":
            st.markdown("""
            <div style='text-align: center; padding: 1rem;'>
                <p style='margin: 0; font-weight: bold; font-size: 1.1rem;'>
                    Made with 💖 for Gen Z dreamers
                </p>
                <p class='afra-branding' style='margin: 0.5rem 0 0 0; font-size: 1rem;'>
                    Made by Afra ✨
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style='text-align: center; padding: 1rem;'>
                <p style='margin: 0; font-weight: bold; font-size: 1.1rem; color: #ffffff; text-shadow: 2px 2px 3px rgba(0,0,0,0.6);'>
                    Made with 💖 for Gen Z dreamers
                </p>
                <p class='afra-branding-light' style='margin: 0.5rem 0 0 0; font-size: 1rem;'>
                    Made by Afra ✨
                </p>
            </div>
            """, unsafe_allow_html=True)

# Main app logic
def main():
    set_page_config()
    
    # Initialize session state for theme if not present
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark Mode"

    # Apply custom CSS
    add_custom_css()

    # Sidebar
    display_sidebar()

    # Main content
    display_header()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history (placeholder for actual chat)
    for message in st.session_state.messages:
        display_chat_message(message["content"], message["is_user"])

    st.markdown("### 🌙 Tell me your dream...")
    st.markdown("<p style='font-size: 0.9rem; margin-top: -10px; opacity: 0.8;'>Describe your dream in detail:</p>", unsafe_allow_html=True)
    dream_input = st.text_area(
        "", # Removed label here as it's provided via markdown above
        "I had this crazy dream where I was flying over a rainbow city...",
        height=150,
        key="dream_text_area"
    )

    if st.session_state.theme == "Dark Mode":
        button_label = "✨ Decode My Dream ✨"
    else:
        # Changed for better contrast in Light Mode
        button_label = "✨ + Decode My Dream + ✨" 

    if st.button(button_label, key="decode_button"):
        if dream_input and dream_input != "I had this crazy dream where I was flying over a rainbow city...": # Check for actual input
            st.session_state.messages.append({"content": dream_input, "is_user": True})
            # Simulate a bot response
            bot_response = f"OMG, flying over a rainbow city?! That's like, super aesthetic! It totally means you're feeling on top of the world and embracing your inner child. Keep that positive energy, bestie! 💖🌈"
            st.session_state.messages.append({"content": bot_response, "is_user": False})
            st.rerun()
        else:
            st.warning("Spill the tea! What's your dream all about?")

    st.markdown("---")
    if st.session_state.theme == "Dark Mode":
        st.markdown("<p style='text-align: center; opacity: 0.7;'>Remember: Dreams are just your brain's way of processing vibes ✨</p>", unsafe_allow_html=True)
    else:
        # Ensure footer text is dark and visible in light mode
        st.markdown("<p style='text-align: center; color: #636e72; opacity: 0.8;'>Remember: Dreams are just your brain's way of processing vibes ✨</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()