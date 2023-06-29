import streamlit as st

try:
    # Attempt to import langchain
    import langchain
    print("langchain is installed.")
    st.write("langchain is installed.")
    print("Version:", langchain.__version__)
except ImportError:
    print("langchain is not installed.")
    st.write("langchain is NOT installed.")

st.title("Hello world")
st.balloons()
