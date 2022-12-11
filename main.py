import streamlit as st
import random

st.title("Hangman")


rletters = []
word = "Rick roll"
UC_word = word.upper()
l_word = list(UC_word)
chosen = '_'

if "count" not in st.session_state:
    st.session_state.count = 0
if "cletters" not in st.session_state:
    st.session_state.cletters = []

with st.container():
    if st.session_state.count == 0:
        st.code('''
Awaiting for letter input...

















What are you waiting for?
    ''')
    if st.session_state.count == 1:
        st.code('''
Wow you arent so good at this huh?!

















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

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6, kpi7, kpi8, kpi9 = st.columns(9)
with kpi1:
    button_a = st.button("A")
    if button_a:
        chosen = "A"

    button_j = st.button("J")
    if button_j:
        chosen = "J"

    button_s = st.button("S")
    if button_s:
        chosen = "S"

with kpi2:
    button_b = st.button("B")
    if button_b:
        chosen = "B"

    button_k = st.button("K")
    if button_k:
        chosen = "K"

    button_t = st.button("T")
    if button_t:
        chosen = "T"

with kpi3:
    button_c = st.button("C")
    if button_c:
        chosen = "C"

    button_l = st.button("L")
    if button_l:
        chosen = "L"
    
    button_u = st.button("U")
    if button_u:
        chosen = "U"

with kpi4:
    button_d = st.button("D")
    if button_d:
        chosen = "D"

    button_m = st.button("M")
    if button_m:
        chosen = "M"
    
    button_v = st.button("V")
    if button_v:
        chosen = "V"

with kpi5:
    button_e = st.button("E")
    if button_e:
        chosen = "E"
    button_n = st.button("N")
    if button_n:
        chosen = "N"
    
    button_w = st.button("W")
    if button_w:
        chosen = "W"

with kpi6:
    button_f = st.button("F")
    if button_f:
        chosen = "F"

    button_o = st.button("O")
    if button_o:
        chosen = "O"
    
    button_x = st.button("X")
    if button_x:
        chosen = "X"

with kpi7:
    button_g = st.button("G")
    if button_g:
        chosen = "G"

    button_p = st.button("P")
    if button_p:
        chosen = "P"

    button_y = st.button("Y")
    if button_y:
        chosen = "Y"

with kpi8:
    button_h = st.button("H")
    if button_h:
        chosen = "H"

    button_q = st.button("Q")
    if button_q:
        chosen = "Q"
    
    button_z = st.button("Z")
    if button_z:
        chosen = "Z"

with kpi9:
    button_i = st.button("I")
    if button_i:
        chosen = "I"
    button_r = st.button("R")
    if button_r:
        chosen = "R"

if chosen == '_' and st.session_state.count <= 10:
    st.stop()
elif chosen not in l_word and st.session_state.count <= 10:
    st.session_state.count+=1
elif chosen in l_word and st.session_state.count <= 10:
    st.session_state.cletters.append(chosen)
    for i in range(len(st.session_state.cletters)):
        st.text(st.session_state.cletters)
        break
else:
    retry_button = st.button("Retry?")
    if retry_button:
        st.session_state.count = 0