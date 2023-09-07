import streamlit as st

st.set_page_config(layout="wide")


def main():
    st.title("Streamlit within Flask")
    st.write('Hello')
    st.write('new')
    st.write('sff')

    # Use st.selectbox for a single select box or st.multiselect for multiple selections
    selected_option = st.sidebar.selectbox('Select an option', ['hello', 'ok', 'world'])
    st.write(f'Selected option: {selected_option}')



    # Your Streamlit app code here

if __name__== "__main__":
    main()

