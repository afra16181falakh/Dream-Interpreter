import streamlit as st

# Very basic test
st.title("🔥 BASIC TEST")
st.write("If you see this, Streamlit is working!")
st.write("Current session state:", st.session_state)

# Test button
if st.button("Test Button"):
    st.success("Button clicked!")

# Test if we can see basic HTML
st.markdown("""
<div style="background: red; color: white; padding: 20px;">
    <h1>RED BOX TEST</h1>
    <p>If you see this red box, HTML rendering works!</p>
</div>
""", unsafe_allow_html=True)