import streamlit as st
import time

def set_page_config():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="✨ Sign Up for DreamBot",
        page_icon="📝",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

def load_css():
    """Load custom CSS for styling."""
    css = """
    <style>
    /* Base Body & Background */
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
        margin: 0;
        padding: 0;
    }
    
    /* Ensure content starts at the top */
    .stApp {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    .main .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    
    /* Hide Streamlit Header/Footer */
    .st-emotion-cache-18ni7ap, .st-emotion-cache-h4xjwg, .st-emotion-cache-1g8sf3p {
        display: none !important;
    }
    
    /* Hide any other elements that might push content down */
    .st-emotion-cache-1r6slb0, .st-emotion-cache-1wivap2 {
        display: none !important;
    }
    
    /* Sign-Up Container - Glassmorphism */
    .signup-container {
        background: rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 3rem;
        max-width: 450px;
        margin: 0 auto;
        margin-top: 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Text Inside Container */
    .signup-container h1, .signup-container p {
        color: white;
        text-align: center;
        margin-top: 0;
    }
    
    /* Force top positioning */
    .signup-container {
        margin-top: 0 !important;
        padding-top: 1rem !important;
        position: relative;
        top: 0;
    }
    
    /* Override Streamlit's default spacing */
    .stApp {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    .main .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    
    /* Force the form to the very top - NUCLEAR OPTION */
    .stMarkdown:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Override ALL Streamlit spacing */
    .stApp > div:first-child,
    .stApp > div:nth-child(2),
    .main .block-container {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Force the signup container to the very top - NUCLEAR OPTION */
    .signup-container {
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
    
    /* Force ALL elements to top */
    .signup-container * {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* SUPER VIBRANT bright text effects - VISIBLE AGAINST BLACK BG */
    .welcome-title {
        animation: superVibrantGlow 1.5s ease-in-out infinite alternate;
        color: #FFFF00 !important; /* Bright Yellow */
        text-shadow: 0 0 30px #FFFF00, 0 0 60px #FFFF00, 0 0 90px #FFFF00, 0 0 120px #FFFF00 !important;
        font-weight: 900 !important;
        background: linear-gradient(45deg, #FFFF00, #00FFFF, #FF00FF) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    .welcome-subtitle {
        animation: superVibrantGlow 2s ease-in-out infinite alternate;
        color: #00FFFF !important; /* Bright Cyan */
        text-shadow: 0 0 20px #00FFFF, 0 0 40px #00FFFF, 0 0 60px #00FFFF !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #00FFFF, #FFFF00, #FF00FF) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    @keyframes superVibrantGlow {
        from { 
            text-shadow: 0 0 40px #FFFF00, 0 0 80px #FFFF00, 0 0 120px #FFFF00, 0 0 160px #FFFF00;
            transform: scale(1);
            filter: brightness(1);
        }
        to { 
            text-shadow: 0 0 80px #FFFF00, 0 0 160px #FFFF00, 0 0 240px #FFFF00, 0 0 320px #FFFF00;
            transform: scale(1.05);
            filter: brightness(1.3);
        }
    }
    
    /* Additional vibrant effects */
    .welcome-title:hover {
        animation: superVibrantGlow 0.3s ease-in-out infinite alternate;
        transform: scale(1.1);
    }
    
    .welcome-subtitle:hover {
        animation: superVibrantGlow 0.3s ease-in-out infinite alternate;
        transform: scale(1.05);
    }
    
    /* Force maximum vibrancy */
    .welcome-title, .welcome-subtitle {
        color: #FFFF00 !important;
        text-shadow: 0 0 60px #FFFF00, 0 0 120px #FFFF00, 0 0 180px #FFFF00, 0 0 240px #FFFF00 !important;
    }
    
    /* Enhanced container styling */
    .signup-container {
        background: rgba(0, 0, 0, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.2);
    }

    .signup-container h1 {
        font-weight: 900;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
    }
    
    /* Styling for Streamlit Text Inputs */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 1.1rem;
        padding: 15px !important;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #FFFF00 !important;
        box-shadow: 0 0 30px rgba(255, 255, 0, 0.5) !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
        transform: scale(1.02);
    }

    .stTextInput > label {
        color: #FFFF00 !important;
        font-weight: 700 !important;
        text-shadow: 0 0 15px rgba(255, 255, 0, 0.8) !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Sign-Up Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FFFF00, #00FFFF);
        color: white;
        border: none;
        padding: 14px 30px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 0 30px rgba(255, 255, 0, 0.5), 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        margin-top: 1.5rem;
        border: 2px solid rgba(255, 255, 0, 0.5);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 0 50px rgba(255, 255, 0, 0.8), 0 6px 20px rgba(0,0,0,0.3);
        border-color: rgba(255, 255, 0, 0.8);
    }

    /* Helper text below button */
    .sub-text {
        text-align: center;
        margin-top: 1.5rem;
        color: rgba(255, 255, 0, 0.8);
        font-size: 0.9rem;
    }
    .sub-text a {
        color: #00FFFF;
        text-decoration: none;
        font-weight: bold;
    }

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    set_page_config()
    load_css()
    
    # Position the form at the very top with aggressive CSS + JavaScript
    st.markdown("""
    <style>
    /* Force everything to start at the very top */
    .stApp { margin-top: 0 !important; padding-top: 0 !important; }
    .main .block-container { margin-top: 0 !important; padding-top: 0 !important; }
    .stMarkdown:first-child { margin-top: 0 !important; padding-top: 0 !important; }
    .stTextInput { margin-top: 0 !important; padding-top: 0 !important; }
    .stButton { margin-top: 0 !important; padding-top: 0 !important; }
    
    /* Hide ALL top elements */
    .stApp > div:first-child,
    .stApp > div:nth-child(2),
    .stApp > div:nth-child(3) {
        margin-top: 0 !important;
        padding-top: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
    }
    </style>
    
    <script>
    // Force scroll to top and position form at top
    window.onload = function() {
        // Scroll to the very top
        window.scrollTo(0, 0);
        
        // Hide any elements pushing content down
        const elements = document.querySelectorAll('.stApp > div');
        for (let i = 0; i < 3; i++) {
            if (elements[i]) {
                elements[i].style.marginTop = '0px';
                elements[i].style.paddingTop = '0px';
                elements[i].style.height = '0px';
                elements[i].style.overflow = 'hidden';
            }
        }
        
        // Force the signup container to the top
        const signupContainer = document.querySelector('.signup-container');
        if (signupContainer) {
            signupContainer.style.marginTop = '0px';
            signupContainer.style.paddingTop = '0px';
            signupContainer.style.position = 'relative';
            signupContainer.style.top = '0px';
        }
    };
    
    // Also run when page loads
    document.addEventListener('DOMContentLoaded', function() {
        window.scrollTo(0, 0);
    });
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 0; padding-top: 0; position: relative; top: 0;'>", unsafe_allow_html=True)
    
    st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1 class='welcome-title' style='font-weight: 900; letter-spacing: 2px; font-size: 2.5rem;'>Join the Dream Team ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='welcome-subtitle' style='font-weight: 700; font-size: 1.3rem; margin-top: 1rem;'>Let's get you set up to decode your dreams.</p>", unsafe_allow_html=True)
    
    # --- Sign-Up Form ---
    username = st.text_input("Pick a username", placeholder="dreamy_afra")
    email = st.text_input("Your email", placeholder="bestie@dreambot.ai")
    password = st.text_input("Create your secret handshake", type="password")
    confirm_password = st.text_input("Confirm it one more time", type="password")
    
    if st.button("Create My Account 💫"):
        if not all([username, email, password, confirm_password]):
            st.warning("Hey, make sure you fill out all the fields! 💅")
        elif password != confirm_password:
            st.error("Oof, the passwords don't match. Give it another go! 😅")
        else:
            # In a real app, you would save the new user to your database here
            with st.spinner('Setting up your dream space...'):
                time.sleep(2)
            st.success(f"Yesss, you're in, {username}! Welcome to the club! 🥳")
            st.balloons()
            # Here you would redirect to the login page or main app.

    st.markdown(
        "<p class='sub-text'>Already have an account? <a href='#'>Log In</a></p>", 
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()