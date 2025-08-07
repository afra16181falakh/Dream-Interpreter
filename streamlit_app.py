import streamlit as st
import os
from dream_interpreter import DreamInterpreter
from ui_components import set_page_config, add_custom_css, display_header, display_chat_message, display_sidebar

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "interpreter" not in st.session_state:
        try:
            st.session_state.interpreter = DreamInterpreter()
        except ValueError as e:
            st.error(f"⚠️ {str(e)}")
            st.stop()
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark Mode"

def main():
    """Main Streamlit application."""
    # Set up page configuration
    set_page_config()
    add_custom_css()
    
    # Initialize session state
    initialize_session_state()
    
    # Display header
    display_header()
    
    # Display sidebar
    display_sidebar()
    
    # Main chat interface
    st.markdown("### 🌙 Tell me your dream...")
    
    # Dream input
    dream_input = st.text_area(
        "Describe your dream in detail:",
        placeholder="I had this crazy dream where I was flying over a rainbow city...",
        height=150,
        key="dream_input"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        interpret_button = st.button(
            "✨ Decode My Dream ✨",
            use_container_width=True,
            type="primary"
        )
    
    # Process dream when button is clicked
    if interpret_button and dream_input:
        with st.spinner("🔮 Consulting the dream spirits..."):
            try:
                interpretation = st.session_state.interpreter.interpret_dream(dream_input)
                
                # Add to chat history
                st.session_state.messages.append({"role": "user", "content": dream_input})
                # Clean up interpretation text to remove any trailing HTML tags
                clean_interpretation = interpretation.strip()
                if clean_interpretation.endswith('</div>'):
                    clean_interpretation = clean_interpretation[:-6].strip()
                st.session_state.messages.append({"role": "assistant", "content": clean_interpretation})
                
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")
    
    # Display chat history
    if st.session_state.messages:
        st.markdown("### 💬 Your Dream Session")
        
        # Create a container for chat messages
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.messages:
                display_chat_message(
                    message["content"], 
                    is_user=(message["role"] == "user")
                )
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.session_state.interpreter.reset_chat()
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <p style='opacity: 0.8;'>Remember: Dreams are just your brain's way of processing vibes ✨</p>
        <p style='font-size: 0.9rem; opacity: 0.7;'>Keep dreaming, keep believing! 🌟</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
