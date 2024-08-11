import streamlit as st
from src.helper import get_pdf_text, get_chunks, get_vector_store, get_conversational_chain

def user_input(user_question):
    if st.session_state.conversation:
        try:
            # Provide the input with correct keys
            input_data = {
                'question': user_question,
                'chat_history': st.session_state.chat_history or []
            }
            response = st.session_state.conversation(input_data)
            st.session_state.chat_history = response['chat_history']

            for i, message in enumerate(st.session_state.chat_history):
                if i % 2 == 0:
                    st.write("User : ", message.content)
                else:
                    st.write("Reply : ", message.content)
        except Exception as e:
            st.error(f"An error occurred while processing the question: {e}")
    else:
        st.warning("Conversation model is not initialized.")




def main():
    st.set_page_config(page_title="PDF Reader App", layout="wide")
    st.header("PDF Reader App 📚")

    user_questions = st.text_input("Ask questions from the PDF file")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if user_questions:
        user_input(user_questions)


    with st.sidebar:
        st.title("Menu:")
        st.write("Upload your PDF file 📂")
        uploaded_files = st.file_uploader("Upload your PDF files and Click on Submit button", type=["pdf"], accept_multiple_files=True)

        if st.button("Submit"):
            if uploaded_files:
                with st.spinner("Please wait, we are processing your PDF files"):
                    try:
                        # Process all uploaded files
                        raw_text = get_pdf_text(uploaded_files)

                        text_chunks = get_chunks(raw_text)

                        vector_store = get_vector_store(text_chunks)

                        st.session_state.conversation = get_conversational_chain(vector_store)

                        st.success("Done")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
            else:
                st.warning("Please upload at least one PDF file.")

if __name__ == "__main__":
    main()
