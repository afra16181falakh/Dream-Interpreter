import streamlit as st
import time

def set_page_config():
    """Configure the Streamlit page."""
    st.set_page_config(
        page_title="✨ DreamBot Login",
        page_icon="🔑",
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
    
    /* Login Container - Glassmorphism */
    .login-container {
        background: rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 3rem;
        max-width: 450px;
        margin: 0 auto;
        margin-top: 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Text Inside Container */
    .login-container h1, .login-container p {
        color: white;
        text-align: center;
        margin-top: 0;
    }
    
    /* Force top positioning */
    .login-container {
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
    
    /* Force the login container to the very top - NUCLEAR OPTION */
    .login-container {
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
    .login-container * {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* SUPER VIBRANT bright text effects - VISIBLE AGAINST BLACK BG */
    .welcome-title {
        animation: superVibrantGlow 1.5s ease-in-out infinite alternate;
        color: #00FFFF !important; /* Bright Cyan */
        text-shadow: 0 0 30px #00FFFF, 0 0 60px #00FFFF, 0 0 90px #00FFFF, 0 0 120px #00FFFF !important;
        font-weight: 900 !important;
        background: linear-gradient(45deg, #00FFFF, #FF00FF, #FFFF00) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    .welcome-subtitle {
        animation: superVibrantGlow 2s ease-in-out infinite alternate;
        color: #FF00FF !important; /* Bright Magenta */
        text-shadow: 0 0 20px #FF00FF, 0 0 40px #FF00FF, 0 0 60px #FF00FF !important;
        font-weight: 700 !important;
        background: linear-gradient(45deg, #FF00FF, #00FFFF, #FFFF00) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    @keyframes superVibrantGlow {
        from { 
            text-shadow: 0 0 40px #00FFFF, 0 0 80px #00FFFF, 0 0 120px #00FFFF, 0 0 160px #00FFFF;
            transform: scale(1);
            filter: brightness(1);
        }
        to { 
            text-shadow: 0 0 80px #00FFFF, 0 0 160px #00FFFF, 0 0 240px #00FFFF, 0 0 320px #00FFFF;
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
        color: #00FFFF !important;
        text-shadow: 0 0 60px #00FFFF, 0 0 120px #00FFFF, 0 0 180px #00FFFF, 0 0 240px #00FFFF !important;
    }
    
    /* Enhanced container styling */
    .login-container {
        background: rgba(0, 0, 0, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.2);
    }

    .login-container h1 {
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
        border-color: #00FFFF !important;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.5) !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
        transform: scale(1.02);
    }

    .stTextInput > label {
        color: #00FFFF !important;
        font-weight: 700 !important;
        text-shadow: 0 0 15px rgba(0, 255, 255, 0.8) !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Login Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #00FFFF, #FF00FF);
        color: white;
        border: none;
        padding: 14px 30px;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.5), 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        margin-top: 1.5rem;
        border: 2px solid rgba(0, 255, 255, 0.5);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.8), 0 6px 20px rgba(0,0,0,0.3);
        border-color: rgba(0, 255, 255, 0.8);
    }

    /* Helper text below button */
    .sub-text {
        text-align: center;
        margin-top: 1.5rem;
        color: rgba(0, 255, 255, 0.8);
        font-size: 0.9rem;
    }
    .sub-text a {
        color: #FF00FF;
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
        
        // Force the login container to the top
        const loginContainer = document.querySelector('.login-container');
        if (loginContainer) {
            loginContainer.style.marginTop = '0px';
            loginContainer.style.paddingTop = '0px';
            loginContainer.style.position = 'relative';
            loginContainer.style.top = '0px';
        }
    };
    
    // Also run when page loads
    document.addEventListener('DOMContentLoaded', function() {
        window.scrollTo(0, 0);
    });
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 0; padding-top: 0; position: relative; top: 0;'>", unsafe_allow_html=True)
    
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    
    st.markdown("<h1 class='welcome-title' style='font-weight: 900; letter-spacing: 2px; font-size: 2.5rem;'>Welcome Back, Dreamer ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p class='welcome-subtitle' style='font-weight: 700; font-size: 1.3rem; margin-top: 1rem;'>Log in to keep the vibes going.</p>", unsafe_allow_html=True)
    
    # --- Login Form ---
    username = st.text_input("Your @...", placeholder="bestie@dreambot.ai")
    password = st.text_input("Password (the secret handshake)", type="password")
    
    if st.button("Let's Gooo 🚀"):
        if not username or not password:
            st.warning("Ayo, don't forget to fill everything out! 🙃")
        # In a real app, you would verify credentials here
        elif username == "afra" and password == "vibecheck": 
            with st.spinner('Logging you in... just a sec!'):
                time.sleep(2)
            st.success(f"Slay! Welcome back, {username}! ✨")
            st.balloons()
            # Here you would redirect to the main app page.
            # For this example, we'll just show the success message.
        else:
            st.error("Oof, wrong deets. Try again? 🤔")

    st.markdown(
        "<p class='sub-text'>First time here? <a href='#'>Sign Up</a> | <a href='#'>Forgot Password?</a></p>", 
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()