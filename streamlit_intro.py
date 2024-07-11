import streamlit as st
import langchain_helper

st.title("My GenAI App")

exercise_type = st.sidebar.selectbox("Pick exercise option :", ("Gym", "Yoga", "Aerobics", "Dance"))
component = st.sidebar.selectbox("Pick component :", ("Diet", "Exercise", "Dress Code"))

if exercise_type and component:
    response = langchain_helper.gen_data(exercise_type, component)
    st.header(response["exercise_type"].strip())
    exercise_items = response["exercise_items"]
    st.write("Components")
    st.write(exercise_items)
    # for item in exercise_items:
    #     st.write("-", item)

