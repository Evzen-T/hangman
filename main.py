import streamlit as st

st.title("Hangman")

if "count" not in st.session_state:
    st.session_state.count = 0

with st.container():
    if st.session_state.count == 1:
        st.code('''
_________________
|________________|
''')

    if st.session_state.count == 2:
        st.code('''
Try again...
       ___
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 3:
        st.code('''
Try again...
       _____________________
       | .__________________|
       | | / /      
       | |/ /
       | | /
       | |/
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')
    if st.session_state.count == 4:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /
       | | /
       | |/
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 5:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |         .-`--'.
       | |
       | |
       | |
       | |
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 6:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |          .-`--'.
       | |          \ . . /
       | |           |   |
       | |           | . |
       | |           |___|
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 7:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |          .-`--'.
       | |        //\ . . /
       | |       //  |   |
       | |      //   | . |
       | |     ('    |___|
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 8:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |          .-`--'.
       | |        //\ . . /\\
       | |       //  |   |  \\
       | |      //   | . |   \\
       | |     ('    |___|    ')
       | |
       | |
       | |
       | | 
_______|_|_______
|________________|
''')

    if st.session_state.count == 9:
        st.code('''
Try again...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |          .-`--'.
       | |        //\ . . /\\
       | |       //  |   |  \\
       | |      //   | . |   \\
       | |     ('    |___|    ')
       | |           ||
       | |           ||
       | |           ||
       |_|          <_|
_______|_|_______
|________________|
''')

    if st.session_state.count == 10:
        st.code('''
He died...
       ___________..________
       | .__________))______|
       | | / /      ||
       | |/ /       ||
       | | /        || .-''.
       | |/         ||/     |
       | |          |||     |
       | |           \\\ __ /
       | |          .-`--'.
       | |        //\ . . /\\
       | |       //  |   |  \\
       | |      //   | . |   \\
       | |     ('    |___|    ')
       | |           || ||
       | |           || ||
       | |           || ||
       | |          <_| |_>
_______|_|_______
|________________|
''')

word = "Deez nuts"
UC_word = word.upper()
listed_word = list(UC_word)

# len_word = len(word)
# for i in range(len_word):
#     st.markdown("_")

def correct_or_not(letter):
    b_status = st.button(str(letter))
    if b_status == True:
        if letter not in listed_word:
            st.session_state.count+=1
        elif letter in listed_word:
            correct_letters = letter
            listed_word.remove(letter)
            if listed_word == None:
                st.success(':white_check_mark: You have saved the man')

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6, kpi7, kpi8, kpi9 = st.columns(9)
with kpi1:
    correct_or_not("A")
    correct_or_not("J")
    correct_or_not("S")
with kpi2:
    correct_or_not("B")
    correct_or_not("K")
    correct_or_not("T")
with kpi3:
    correct_or_not("C")
    correct_or_not("L")
    correct_or_not("U")
with kpi4:
    correct_or_not("D")
    correct_or_not("M")
    correct_or_not("V")
with kpi5:
    correct_or_not("E")
    correct_or_not("N")
    correct_or_not("W")
with kpi6:
    correct_or_not("F")
    correct_or_not("O")
    correct_or_not("X")
with kpi7:
    correct_or_not("G")
    correct_or_not("P")
    correct_or_not("Y")
with kpi8:
    correct_or_not("H")
    correct_or_not("Q")
    correct_or_not("Z")
with kpi9:
    correct_or_not("I")
    correct_or_not("R")

if st.session_state.count > 10:
    retry_button = st.button("Retry")
    if retry_button:
        st.session_state.count = 0