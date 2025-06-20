import streamlit as st
from datetime import datetime
import base64

# Page Setup
st.set_page_config(page_title="Happy Birthday 💖", layout="centered")

# Custom Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #dda0dd, #ffc0cb);
        color: #2e003e;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #ff1493;
        text-align: center;
    }
    .section-title {
        font-size: 28px;
        color: #8e44ad;
        margin-top: 30px;
        text-align: center;
    }
    .message {
        font-size: 18px;
        color: #2c003e;
        margin-bottom: 10px;
    }
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 250px;
        perspective: 1000px;
        margin-bottom: 10px;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 10px;
    }
    .flip-card-front {
        background-color: #fff;
    }
    .flip-card-back {
        background-color: #ffc0cb;
        color: #2e003e;
        transform: rotateY(180deg);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🎂 Happy Birthday, My Sunshine! ☀️</div>', unsafe_allow_html=True)
st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", use_container_width=True)

# Special Messages
st.markdown('<div class="message">Wishing you a day full of love, laughter, and everything you dream of! 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="message">You are a blessing to everyone around you. May your year be filled with light, success, and happiness. 🌟</div>', unsafe_allow_html=True)

# Surprise Section
if st.button("Reveal My Surprise ✨"):
    st.balloons()
    st.success("You light up the world more than candles on your cake 🎂❤️")

    video_url = "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/video2.mp4"

    video_html = f"""
        <video autoplay loop controls width="100%" height="250px" style="border-radius: 10px; object-fit: cover;">
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)


# Special Memories Section (flip card version)
st.markdown('<div class="section-title">📸 Special Memories</div>', unsafe_allow_html=True)


image_urls = [
    "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/Memories.jpg",
    "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/image9.jpeg",
    "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/image10.jpeg"
]

memory_captions = [
    "Unforgettable Moment 💫",
    "Your Radiant Smile 😄",
    "Our Favorite Time Together 🥰"
]

cols = st.columns(len(image_paths))
for i, path in enumerate(image_paths):
    with cols[i]:
        try:
            with open(path, "rb") as img_file:
                img_bytes = img_file.read()
                img_b64 = base64.b64encode(img_bytes).decode()

            st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <img src="data:image/jpeg;base64,{img_b64}" style="width:100%; height:100%; object-fit:contain; border-radius:10px;">
                        </div>
                        <div class="flip-card-back">
                            {memory_captions[i]}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"Image not found at {path}")

# Letter Section
st.markdown('<div class="section-title">💌 A Personal Letter</div>', unsafe_allow_html=True)
with st.expander("Click here to open your birthday letter 💝"):
    st.write("""
    Hey beautiful Doli,

    On this special day, I want you to know just how much you mean to me.
    Your கருணை, your சிரிப்பு, your கனவுகள் – they inspire me every single day.
    I admire your strength and hope you never stop shining.

    I'm always cheering for you, every step of the way purinjukonga. 🌈

    Happy Birthday once again, with all my love 💕  
    — Someone who truly cares about you Dolar
             Varataa Maame....
    """)

# Gifts Section
st.markdown('<div class="section-title">🎀 A Gift Wish List (Just for Fun!)</div>', unsafe_allow_html=True)
gifts = [
    "💄 A self-care box full of your favorite skincare",
    "🎧 A playlist of songs that remind me of you",
    "🎨 A digital portrait of you as a queen 👑",
    "💌 A handmade letter with all my love"
]
for gift in gifts:
    st.markdown(f"- {gift}")

# Countdown Section
st.markdown('<div class="section-title">📅 Birthday Countdown</div>', unsafe_allow_html=True)

bday = datetime(datetime.now().year, 6, 21)  # Update birthday to June 21
now = datetime.now()

if now.month == 6 and now.day == 21:
    st.success("🎉 Today is your special day, my sunshine! 💖")
    st.balloons()
    st.markdown("**May your day be filled with laughter, surprises, and love beyond words. Happy Birthday! 🎂🌈**")
elif now > bday:
    next_bday = datetime(now.year + 1, 6, 21)
    days_left = (next_bday - now).days
    st.info(f"⏳ {days_left} days left until your next birthday!")
else:
    days_left = (bday - now).days
    st.info(f"⏳ {days_left} days left until your birthday!")

# Message Form
st.markdown('<div class="section-title">📬 Send Me a Message</div>', unsafe_allow_html=True)
with st.form("contact_form"):
    name = st.text_input("Your Name")
    message = st.text_area("Your Message to Me")
    if st.form_submit_button("Send Message 💌"):
        st.success("Message sent! I'll cherish it forever 🌷")

# Your Voice Section (Flip + Audio)
st.markdown('<div class="section-title">🎤 Your Beautiful Voice</div>', unsafe_allow_html=True)

songs = [
    {
        "image_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/image.jpg",
        "audio_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/Birthdaysong1.mp3",
        "compliment": "Your voice is as soothing as a lullaby. 💖"
    },
    {
        "image_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/image4.jpeg",
        "audio_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/Birthdaysong2.mp3",
        "compliment": "You sound like sunshine wrapped in a melody ☀️🎶"
    },
    {
        "image_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/image5.jpeg",
        "audio_path": "https://raw.githubusercontent.com/Ayapan8/Birthday21/main/assets/Birthdaysong1.mp3",
        "compliment": "Sweet, soft, and simply beautiful 💕"
    }
]

if "selected_song" not in st.session_state:
    st.session_state.selected_song = -1

cols = st.columns(len(songs))
for i, song in enumerate(songs):
    with cols[i]:
        try:
            with open(song["image_path"], "rb") as img_file:
                img_bytes = img_file.read()
                img_b64 = base64.b64encode(img_bytes).decode()

            st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <img src="data:image/jpeg;base64,{img_b64}" style="width:100%; height:100%; object-fit:contain; border-radius:10px;">
                        </div>
                        <div class="flip-card-back">
                            {song["compliment"]}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"▶️ Play Song {i+1}", key=f"play_{i}"):
                st.session_state.selected_song = i
        except FileNotFoundError:
            st.error(f"Image not found at {song['image_path']}")

# Display selected song
if st.session_state.selected_song != -1:
    try:
        selected = songs[st.session_state.selected_song]
        with open(selected["audio_path"], "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_b64 = base64.b64encode(audio_bytes).decode()
            st.markdown(f"""
                <audio controls autoplay style="width:100%; margin-top: 10px;">
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
            """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Audio file not found at {selected['audio_path']}")

# Footer
st.markdown("---")
st.markdown("Made with 💖 just for you.")
