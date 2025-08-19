import streamlit as st
import time

# Test the basic structure of the main app
def main():
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

    st.write("🔥 MAIN APP STRUCTURE TEST")
    st.write(f"Logged in: {st.session_state.logged_in}")
    st.write(f"Current page: {st.session_state.page}")
    
    # Add basic CSS
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #533483 100%);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Test routing logic
    if st.session_state.logged_in:
        st.success("✅ LOGGED IN - MAIN APP")
        st.write("This is where the main DreamBot app would be")
        
        # Test sidebar
        with st.sidebar:
            st.write("🎛️ SIDEBAR TEST")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
    else:
        st.info("🔐 NOT LOGGED IN - AUTH PAGE")
        st.write("This is where login/signup would be")
        
        # Simple login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username == "afra" and password == "vibecheck":
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")

if __name__ == "__main__":
    main()