# app.py

import streamlit as st
import random

# Set up the Streamlit app
st.set_page_config(page_title="Mental Wellness Chatbot")
st.title("AI Mental Wellness Chatbot")
st.write("Hi there! Talk to me about how you're feeling today.")

# Crisis trigger phrases
crisis_keywords = [
    "i can't cope", "no hope", "i give up", "end it", "suicide", "i want to die"
]

# Simple CBT response suggestions
cbt_responses = [
    "Let's try the 4-7-8 breathing method: Inhale for 4 sec, hold for 7 sec, exhale for 8 sec.",
    "You're doing your best, and that counts. One small step at a time.",
    "Let's write down 3 things that went well today."/
    "Try taking a short walk or stretching for 5 minutes.",
    "Take a moment to pause and just breathe deeply for 30 seconds."
]

# Badge system
user_badge = []

def award_badge():
    if "Calm Starter" not in user_badges:
        user_badges.append("Calm Starter")
        return "You've earned the 'Calm Starter' badge!"
        return None

  # input from user
        user_input = st.text_input("You:")
if user_input:
    lower_input = user_input.lower()

    # Check for crisis keywords
    if any(keyword in lower_input for keyword in crisis_keywords):
        st.error("Crisis detected! A message has been sent to a trusted contact.")
        else:
            # Choose a random CBT-style response
            bot_reply = random.choice(cbt_responses)
            st.success(f"Bot: {bot_reply}")

            # Award badge
            badge_msg = award_badge()
            if badge_msg:
                st.info(badge_msg)

                # Display earned badges
                if user_badges:
                    st.sudheader("Your Badges")
                    st.write(", ".join(user_badges))