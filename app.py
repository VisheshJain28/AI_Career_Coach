from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from langchain.chains import LLMChain 
from config import UPLOAD_FOLDER
from src.vector_store import create_vector_store
from src.pdf_loader import extract_text_from_pdf
from src.llm import get_llm
from src.prompts import resume_prompt
from src.qa import perform_qa
llm = get_llm()

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
resume_analysis_chain = LLMChain(
    llm=llm,
    prompt=resume_prompt,
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extracted   the  text from the PDF
        resume_text = extract_text_from_pdf(file_path)
        create_vector_store(resume_text)
        
        # print(proposal_text)
        # Run SWOT analysis using the LLM chain
        resume_analysis = resume_analysis_chain.run(resume=resume_text)
        
        return render_template('results.html', resume_analysis=resume_analysis)

@app.route('/ask', methods=['GET', 'POST'])
def ask_query():
    if request.method == 'POST':
        query = request.form['query']
        result = perform_qa(query)
        return render_template('qa_results.html', query=query, result=result)
    return render_template('ask.html')

if __name__ == "__main__":
    app.run(debug=True)