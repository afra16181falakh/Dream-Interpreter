# ✨ DreamBot Streamlit App - Your Gen Z Dream Interpreter

A modern, interactive web application for dream interpretation with a Gen Z personality, built with Streamlit and Google Generative AI.

## 🌟 Features

- **Interactive Chat Interface**: Modern chat-style dream interpretation
- **Gen Z Personality**: Casual, emoji-filled responses with current slang
- **Responsive Design**: Works on desktop and mobile
- **Dark Mode**: Aesthetic gradient backgrounds
- **Chat History**: Keep track of your dream sessions
- **Easy Deployment**: Ready for Streamlit Cloud

## 🚀 Quick Start

### Local Development

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd dreambot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env and add your Google API key
   ```

4. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

### Streamlit Cloud Deployment

1. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Add Streamlit app"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `streamlit_app.py` as the main file
   - Add your `GOOGLE_API_KEY` in the secrets

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### Streamlit Cloud Secrets

For Streamlit Cloud deployment, add these to your app secrets:

```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

## 📱 Usage

1. **Describe your dream** in the text area
2. **Click "Decode My Dream"** to get interpretation
3. **Read the Gen Z-style response** with emojis and slang
4. **Continue the conversation** or start fresh

## 🎨 Customization

### Personality Settings

- Adjust the "Vibe Level" in the sidebar
- Toggle between Dark/Light mode
- Clear chat history anytime

### Styling

- Edit `ui_components.py` for custom CSS
- Modify `dream_interpreter.py` for different AI personalities

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Generative AI (Gemini 1.5 Flash)
- **Styling**: Custom CSS with gradients
- **Deployment**: Streamlit Cloud ready

## 📋 Requirements

- Python 3.7+
- Google Generative AI API key
- Streamlit account (for cloud deployment)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🌈 Support

Having issues? Open an issue on GitHub or reach out for help!

---

**Made with 💖 for all the dreamers out there** ✨
