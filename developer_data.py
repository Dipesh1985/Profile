import streamlit as st
col1, col2 = st.columns([0.5,0.7], gap="small", vertical_alignment="center")
with col1:
    st.image("Profile_img.png", width=400)

with col2:
    st.title("Dipesh Mani Tiwari", anchor=False)
    st.write(
        "Free Python Coder"
    )
st.markdown("<br><br>",unsafe_allow_html=True)
st.write("**Nationality:**  Indian")
st.write("**Experinced:** Python ,Html")
st.write("**Email:** @tiwaridipesh739@gmail.com")
