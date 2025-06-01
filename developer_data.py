import streamlit as st
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("Profile_img.png", width=400)

with col2:
    st.title("Dipesh Mani Tiwari", anchor=False)
    st.write(
        "Free Python Coder"
    )


st.header("Dipesh Mani Tiwari")
st.write("**Nationality:**  Indian")
st.write("**Experinced:** Python ,Html")
st.write("**Email:** @tiwaridipesh739@gmail.com")
