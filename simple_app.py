import streamlit as st

def main():
    st.set_page_config(
        page_title="DreamBot", 
        page_icon="✨", 
        layout="wide"
    )
    
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = True
    
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if st.session_state.logged_in:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: rgba(0,0,0,0.3); border-radius: 20px; margin: 2rem;'>
            <h1 style='color: white; font-size: 4rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.8);'>
                ✨ DreamBot ✨
            </h1>
            <h3 style='color: white; font-size: 1.8rem; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);'>
                Your Gen Z Dream Interpreter 🔮✨
            </h3>
            <p style='color: white; font-size: 1.3rem; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);'>
                Welcome, dreamer! ✨ Share your dreams and let me decode them! 🌙💫
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Simple form
        with st.form("dream_form"):
            dream_input = st.text_area("Tell me your dream...", placeholder="I had a dream I was flying...", height=100)
            submitted = st.form_submit_button("Decode My Dream ✨")
            
            if submitted and dream_input:
                st.success(f"Got your dream: {dream_input}")
        
        # Welcome message when no input
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 20px; margin: 2rem;'>
            <h3 style='color: white; font-size: 2rem; text-shadow: 2px 2px 6px rgba(0,0,0,0.7);'>
                💫 Ready to decode your dreams? 💫
            </h3>
            <p style='color: white; font-size: 1.2rem; text-shadow: 1px 1px 4px rgba(0,0,0,0.6);'>
                ✨ Share your dream above and let the magic begin! ✨
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("Not logged in")

if __name__ == "__main__":
    main()