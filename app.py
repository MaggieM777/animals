import streamlit as st
import pandas as pd

st.title("Галерия с животни")

# Празен списък
if "animals" not in st.session_state:
    st.session_state.animals = []

# Добавяне
name = st.text_input("Име")
desc = st.text_input("Описание")
img = st.text_input("URL на картинка")

if st.button("Добави"):
    if name and desc and img:
        st.session_state.animals.append({
            "име": name,
            "описание": desc,
            "картинка": img
        })
        st.success("Добавено!")
    else:
        st.warning("Попълни всичко!")

# Изтриване
st.header("Изтриване")
if st.session_state.animals:
    names = [a["име"] for a in st.session_state.animals]
    to_delete = st.selectbox("Избери животно", names)

    if st.button("Премахни"):
        st.session_state.animals = [
            a for a in st.session_state.animals if a["име"] != to_delete
        ]
        st.success("Премахнато!")
else:
    st.info("Няма какво да се трие.")

# Таблица
st.header("Таблица")
if st.session_state.animals:
    df = pd.DataFrame(st.session_state.animals)
    st.dataframe(df)
else:
    st.info("Няма добавени животни.")
