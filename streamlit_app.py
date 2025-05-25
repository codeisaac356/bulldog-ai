import streamlit as st
import difflib

st.set_page_config(page_title="Bulldog AI Student Chatbot", page_icon="🐶", layout="centered")

# Sidebar with info and logo
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=80)
    st.markdown("## 🐾 Bulldog AI Help")
    st.info(
        "Welcome to Bulldog AI! \n\n"
        "Ask any question about your school. "
        "Try things like:\n"
        "- What time does the school building open?\n"
        "- Where is the Portola Activities Office?\n"
        "- Can visitors come to campus?\n"
        "\nIf you don't get an answer, try rephrasing your question."
    )
    st.markdown("---")
    st.caption("Made for Portola High School students.")

st.markdown("<h1 style='text-align: center; color: #6d28d9;'>🐶 Bulldog AI Student Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

faq = {
    "what time does the school building open": "The school building is open from 7:30 a.m. to 4:00 p.m.",
    "when does the school open": "The school building is open from 7:30 a.m. to 4:00 p.m.",
    "what are the school hours": "The school building is open from 7:30 a.m. to 4:00 p.m.",
    "when can students access the front office": "Students may access the front office before class, during snack and lunch, during office hours, and after school. Permission is needed at other times.",
    "can i go to the office during class": "Permission must be obtained to be in the office at any time other than before class, during snack and lunch, during office hours, and after school.",
    "where is the portola activities office": "The Portola Activities Office (P.A.C.) is open to service students. The specific times are posted outside the P.A.C.",
    "what should i do if i lose my textbook": "Lost & found articles are to be turned in to the front office. Fines are imposed if books are lost.",
    "can i lend my books to other students": "You should not lend books to other students. Identify your textbooks and school materials with your name.",
    "what happens if i lose my personal property": "The loss of personal property will not be reimbursed by the school.",
    "can i leave campus during assemblies": "Students may NOT leave campus during assemblies.",
    "what is the closed campus policy": "Portola High School maintains a closed campus policy. Those leaving campus without written approval will receive a penalty.",
    "can visitors come to campus": "Guests, visitors, or friends of PHS students are not permitted on campus. See your Assistant Principal in advance for procedure and permission. Visitors must obtain a visitor's pass from the front office.",
    "how are messages delivered to students": "Messages are only delivered to students in cases of extreme emergencies. The nature of all such emergencies must be established prior to the message delivery.",
    "can flowers or balloons be delivered to students": "Flowers, balloons, and similar items will not be accepted for delivery to students. All such items will be refused delivery at the front office.",
}

def get_answer(user_input):
    user_input = user_input.lower().strip()
    for question, answer in faq.items():
        if question in user_input:
            return answer
    questions = list(faq.keys())
    closest = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
    if closest:
        return faq[closest[0]]
    return "I'm sorry, I don't know the answer to that. Please ask the school office for more information."

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(
                f"<div style='background-color:#e0e7ff; padding:10px; border-radius:10px; margin-bottom:5px;'><b>You:</b> {message['content']}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div style='background-color:#f1f5f9; padding:10px; border-radius:10px; margin-bottom:10px;'><b>Bulldog AI:</b> {message['content']}</div>",
                unsafe_allow_html=True,
            )

user_input = st.chat_input("Type your question here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    answer = get_answer(user_input)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>© 2025 Portola High School • Bulldog
