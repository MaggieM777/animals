import streamlit as st

# Заглавие
st.title("Галерия")

# Списък със животни (започваме празен или с пример)
if "animals" not in st.session_state:
    st.session_state.animals = [
        {"име": "Котка", "описание": "Котка", 
         "картинка": "https://cdn.pixabay.com/photo/2017/11/09/21/41/cat-2934720_1280.jpg"},
        {"име": "Куче", "описание": "Най-добрият приятел на човека", 
         "картинка": "https://cdn.pixabay.com/photo/2015/03/26/09/54/dog-690176_1280.jpg"}
    ]

st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area("Описание")
image_url = st.text_input("URL на картинка")

if st.button("Добави"):
    if name and description and image_url:
        st.session_state.animals.append({
            "име": name,
            "описание": description,
            "картинка": image_url
        })
        st.success(f"{name} е добавено!")
    else:
        st.warning("Попълнете всички полета!")

# Премахване
if st.session_state.animals:
    st.header("Премахни животно")
    remove_name = st.selectbox("Избери животно за премахване", 
                               [a["име"] for a in st.session_state.animals])
    if st.button("Премахни"):
        st.session_state.animals = [a for a in st.session_state.animals if a["име"] != remove_name]
        st.success(f"{remove_name} е премахнато!")

# Визуализация на галерията
st.header("Галерия")
if st.session_state.animals:
    cols = st.columns(3)  # 3 колонки
    for idx, animal in enumerate(st.session_state.animals):
        with cols[idx % 3]:
            st.subheader(animal["име"])
            st.image(animal["картинка"], use_column_width=True)
            st.write(animal["описание"])
else:
    st.info("Галерията е празна. Добавете животни!")
