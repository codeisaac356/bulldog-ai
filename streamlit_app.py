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
    # Existing FAQs
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

    # New FAQs from Portola_schedule
    "what is the monday schedule": "On Mondays, students attend all eight periods in shorter sessions. Period 1 starts at 8:30 AM and Period 8 ends at 3:50 PM.",
    "what is the finals schedule": "During finals week, the school follows adjusted schedules. For example, the 3-Block Finals Schedule starts with Period A at 8:30 AM and ends with Period C at 12:55 PM.",
    "what is the 2-block finals schedule": "The 2-Block Finals Schedule starts with Period A at 8:30 AM and ends with Period C at 1:15 PM.",
    "what is the 3-block finals schedule": "The 3-Block Finals Schedule starts with Period A at 8:30 AM and ends with Period C at 12:55 PM.",
    "what is the minimum day schedule": "On minimum days, all eight periods meet in a single day. Period 1 starts at 8:30 AM and Period 8 ends at 12:40 PM.",
    "what is the double assembly schedule": "On double assembly days, students are divided into two groups. Period 1/2 starts at 8:30 AM, and the day ends with Period 7/8 at 3:40 PM.",
    "what is the tuesday schedule": "On Tuesdays, students follow a block schedule with collaboration time starting at 8:00 AM. Period 1/2 starts at 8:45 AM and Period 7/8 ends at 3:40 PM.",
    "what is the wednesday schedule": "On Wednesdays, students follow a block schedule with collaboration time starting at 8:00 AM. Period 1/2 starts at 8:45 AM and Period 7/8 ends at 3:40 PM.",
    "what is the thursday schedule": "On Thursdays, students follow a block schedule without collaboration time. Period 1/2 starts at 8:30 AM and Period 7/8 ends at 3:40 PM.",
    "what is the friday schedule": "On Fridays, students follow a block schedule without collaboration time. Period 1/2 starts at 8:30 AM and Period 7/8 ends at 3:40 PM.",
    "what is the break time during finals": "During finals, breaks are scheduled between periods. For example, there is a 10-minute break between Period A and Period B.",
    "what is the lunch time on monday": "On Mondays, lunch is from 11:55 AM to 12:25 PM.",
    "what is the lunch time on block days": "On block days (Tuesday to Friday), lunch is from 12:15 PM to 12:45 PM.",

    # New FAQs from Portola_Courses
    "what courses are offered for 9th grade": "For 9th grade, courses include Literary & Language Arts 1 (CP), Literary & Language Arts 1 Honors, Integrated Math 1, Biology, World History, Spanish 1, French 1, Mandarin 1, PE 9, Art 1, Drama 1, Music Ensemble, AVID 9, and Introduction to Computer Science.",
    "what courses are offered for 10th grade": "For 10th grade, courses include American Literary & Language Arts (CP), American Literary & Language Arts Honors, Integrated Math 2, Chemistry, U.S. History, Spanish 2, French 2, Mandarin 2, PE 10, Art 2, Drama 2, Advanced Music Ensemble, AVID 10, and Computer Science Principles.",
    "what courses are offered for 11th grade": "For 11th grade, courses include British Literary & Language Arts (CP), AP English Language and Composition, Integrated Math 3, Pre-Calculus, Physics, AP Biology, AP Chemistry, Government, Economics, Spanish 3, French 3, Mandarin 3, PE Electives, Art 3, Drama 3, Advanced Music Ensemble, AVID 11, and AP Computer Science A.",
    "what courses are offered for 12th grade": "For 12th grade, courses include Expository Reading and Writing Course (ERWC), AP English Literature and Composition, Calculus, AP Calculus AB, AP Calculus BC, AP Physics, Environmental Science, AP Psychology, Sociology, Spanish 4, French 4, Mandarin 4, PE Electives, Art 4, Drama 4, Advanced Music Ensemble, AVID 12, and AP Computer Science Principles.",
    "what is the mathematics pathway": "The Mathematics Pathway includes Integrated Math 1 in 9th grade, Integrated Math 2 in 10th grade, Integrated Math 3 in 11th grade, and Pre-Calculus or Statistics in 12th grade. The Accelerated Pathway includes Integrated Math 1 Honors, Integrated Math 2 Honors, Pre-Calculus Honors, and AP Calculus AB or BC.",
    "what is the english pathway": "The English Pathway includes Literary & Language Arts 1 in 9th grade, American Literary & Language Arts in 10th grade, British Literary & Language Arts in 11th grade, and ERWC in 12th grade. The Honors/AP Pathway includes Literary & Language Arts 1 Honors, American Literary & Language Arts Honors, AP English Language and Composition, and AP English Literature and Composition.",
# Staff-related FAQs
    "who are the math teachers": "The math teachers at Portola High School are:\n- Michelle Becerra\n- Kelly Burke\n- Melanie Clarke\n- Michele Correll\n- Samantha Jennings\n- Nicole Larson\n- Kelli Moline\n- Shelley Godett\n- Rachel Schneble\n- Kayla Todd\n- Jessica Torres\n- Diana Vedder\n- Derek Zahn\n- Samantha Zimmerle.",
    "who are the science teachers": "The science teachers at Portola High School are:\n- Erin Arredondo\n- Erica Borquez\n- Leanne Jimenez\n- Ryan Johnson\n- Andrew Kranz\n- Maddie Kelly\n- Charity Lizardo\n- Courtney Moder\n- Caitlin Munn\n- Jeralyn Newton\n- Annmarie Ngo\n- Sharon Price\n- Christian Quinteros\n- Anthony Pham\n- Michael Tang\n- Meghan Truax.",
    "who are the social studies teachers": "The social studies teachers at Portola High School are:\n- Kathryn Beechinor\n- Samantha Ezratty\n- James Ferrel\n- Veronica Grammier\n- Daniel Hunter\n- Shameemah Motala\n- Virginia Nguyen\n- Rebecca Oh\n- Megan Saia\n- Natasha Schottland\n- Emily Sheridan\n- Brian Smith\n- Taryn Sorrentino\n- Katie Wi\n- Marisa Wilkerson.",
    "who are the literary and language arts teachers": "The Literary & Language Arts teachers at Portola High School are:\n- Maria Abeyta\n- Kate Avery\n- Alex Carino\n- Jill Cavotta\n- Eric Cho\n- Maithy Do\n- Stephanie Green\n- Desmond Hamilton\n- Christina Han\n- Lyndsey Hicks\n- Katherine Hooper\n- Doris Schlothan\n- Olivia Wallace\n- Vinny Rico\n- Cale Kavanaugh.",
    # Add more departments as needed...
}
staff = {
    "michelle becerra": {
        "position": "Math Teacher",
        "department": "Math",
        "email": "MichelleBecerra@iusd.org"
    },
    "samantha zimmerle": {
        "position": "Math Teacher",
        "department": "Math",
        "email": "SamanthaZimmerle@iusd.org"
    },
    "wind ralston": {
        "position": "Social Studies Teacher / Head Golf Coach",
        "department": "Athletics, Social Studies",
        "email": "WindRalston@iusd.org"
    },
    "adrian rangel-sanchez": {
        "position": "Performing Arts Teacher: Vocal Music",
        "department": "Visual & Performing Arts",
        "email": "AdrianRangelSanchez@iusd.org"
    },
    "nazy rashidi": {
        "position": "Attendance",
        "department": "Literary & Language Arts",
        "email": "NazaninRashidi@iusd.org"
    },
    # Add more staff members here...
}
import difflib

def get_answer(user_input, context=None):
    user_input = user_input.lower().strip()

    # Step 1: Check for teacher-specific queries
    for teacher_name, details in staff.items():
        if teacher_name in user_input:
            return (
                f"{teacher_name.title()} is a {details['position']} in the {details['department']} department. "
                f"You can contact them at {details['email']}."
            )

    # Step 2: Exact match for general FAQs
    for question, answer in faq.items():
        if question in user_input or user_input in question:
            return answer

    # Step 3: Keyword-based inference
    keywords = user_input.split()
    best_match = None
    best_score = 0

    for question, answer in faq.items():
        score = sum(1 for word in keywords if word in question)
        if score > best_score:
            best_score = score
            best_match = answer

    if best_score > 0:
        return best_match

    # Step 4: Fuzzy matching as a fallback
    questions = list(faq.keys())
    closest = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.4)
    if closest:
        return faq[closest[0]]

    # Step 5: Contextual response
    if context:
        return f"I'm not sure about that, but based on our conversation, you might be interested in: {context}"

    # Step 6: Default response if no match is found
    return "I'm sorry, I don't know the answer to that. Please ask the school office for more information."
    questions = list(faq.keys())
    closest = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
    if closest:
        return faq[closest[0]]
    return "I'm sorry, I don't know the answer to that. Please ask the school office for more information."

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.context = None  # Store context for the conversation

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
    # Append the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate the bot's response
    answer = get_answer(user_input, context=st.session_state.context)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Update context for future responses
    st.session_state.context = answer
    
    # Force rerun to display the response immediately
    st.experimental_rerun()

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>© 2025 Portola High School • Bulldog AI</div>", unsafe_allow_html=True)


