

## Information Retrieval from Multiple PDF 💁💬 with PaLM2

### Overview
The **Information Retrieval from Multiple PDF** app is a Streamlit-based application that allows users to upload and interact with multiple PDF files. Using PaLM2, LangChain, and FAISS, the app enables users to ask questions about the content of the PDFs and receive accurate, contextually relevant responses.

### How to Run?

#### STEPS:

1. **Clone the Repository**

   Project repo: [https://github.com/Amartya-007/PDF-Reader-App](https://github.com/Amartya-007/PDF-Reader-App)

   ```bash
   git clone https://github.com/Amartya-007/PDF-Reader-App.git
   cd PDF-Reader-App
   ```

2. **Create a Conda Environment**

   After opening the repository, create and activate a Conda environment:

   ```bash
   conda create -n llmapp python=3.8 -y
   conda activate llmapp
   ```

3. **Install the Requirements**

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key. You can generate an API key by following the instructions at [Google PaLM API Setup](https://ai.google.dev/palm_docs/setup):

   ```bash
   GOOGLE_API_KEY= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   ```

5. **Run the App**

   Finally, run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

6. **Open the App**

   Open your web browser and navigate to:

   [http://localhost:8501](http://localhost:8501)

### Usage

1. **Upload PDF Files**
   - Use the sidebar to upload one or more PDF files.
   - Click the "Submit" button to process the files.

2. **Ask Questions**
   - Once the PDFs are processed, enter your question in the text input box.
   - The app will provide answers based on the content of the uploaded PDFs.

3. **View Chat History**
   - The chat history displays the questions you’ve asked and the app’s responses, simulating a conversation interface.

### Project Structure

```
PDF-Reader-App/
│
├── src/
│   ├── helper.py            # Contains helper functions for text extraction, chunking, vector store, and conversational chain.
│
├── app.py                   # Main Streamlit app file.
├── requirements.txt         # Python dependencies.
├── .env                     # Environment variables.
└── README.md                # Project documentation.
```

### Technologies Used

- **Python**: Programming language used for the app.
- **LangChain**: For managing conversational AI and text processing.
- **Streamlit**: For creating the web application.
- **PaLM2**: For generating embeddings and handling language model responses.
- **FAISS**: For efficient vector search.

### Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

If you have any questions or feedback, feel free to reach out to me at [your-email@example.com].
