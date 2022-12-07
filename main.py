import streamlit as st

st.title("Hangman")

if "count" not in st.session_state:
    st.session_state.count = 0
def failed_attempts():
    st.session_state.count+=1

with st.container():
    if st.session_state.count == 1:
        st.code('''
______________
''')
    if st.session_state.count == 2:
        st.code('''
Be careful!

       |
       |
       |
       |
       |
       |
       |
       |
       |
       |
_______|________
''')
    if st.session_state.count == 3:
        st.code('''
Are you sure about that?

       |-----------------
       |
       |
       |
       |
       |
       |
       |
       |
       |
_______|________
''')
    if st.session_state.count == 4:
        st.code('''
You are dogwater...

       |-----------------
       |                |
       |
       |
       |
       |
       |
       |
       |
       |
_______|________
''')

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6, kpi7, kpi8, kpi9 = st.columns(9)
with kpi1:
    A_button = st.button("A", disabled=1)
    J_button = st.button("J", disabled=1)
    S_button = st.button("S", disabled=1)
with kpi2:
    B_button = st.button("B", disabled=1)
    K_button = st.button("K", disabled=1)
    T_button = st.button("T", disabled=1)
with kpi3:
    C_button = st.button("C", disabled=1)
    L_button = st.button("L", disabled=1)
    U_button = st.button("U", disabled=1)
with kpi4:
    D_button = st.button("D", disabled=1)
    M_button = st.button("M", disabled=1)
    V_button = st.button("V", disabled=1)
with kpi5:
    E_button = st.button("E", disabled=1)
    N_button = st.button("N", disabled=1)
    W_button = st.button("W", disabled=1)
with kpi6:
    F_button = st.button("F", disabled=1)
    O_button = st.button("O", disabled=1)
    X_button = st.button("X", disabled=1)
with kpi7:
    G_button = st.button("G", disabled=1)
    P_button = st.button("P", disabled=1)
    Y_button = st.button("Y", disabled=1)
with kpi8:
    H_button = st.button("H", disabled=1)
    Q_button = st.button("q", disabled=1)
    Z_button = st.button("Z", disabled=1)
with kpi9:
    I_button = st.button("I", disabled=1)
    R_button = st.button("R", disabled=1)
button = st.button("Hi", on_click=failed_attempts)