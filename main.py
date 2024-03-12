from fastapi import FastAPI, UploadFile, File, HTTPException, status
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import fitz

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key, temperature=0.1)

app = FastAPI(title="Resume Reviewer AI")

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ' '.join(page.get_text() for page in doc)
        return text
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error occurred while extracting text: {e}")

def generate_feedback(text):
    message = HumanMessage(
        content=[
            {
                "type": text,
                "text": "You are tasked with reviewing a resume for the position of Software Development Engineer. Provide feedback on the candidate's qualifications, skills, and experience as they relate to the role.",
            },
        ]
    )
    feedback = llm.invoke([message])
    return feedback

@app.get('/')
def home():
    return "Resume Reviewer AI"

@app.post("/resume-feedback/")
async def get_feedback(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as buffer:
        buffer.write(await file.read())
    
    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf("temp.pdf")
    
    # Generate feedback using the extracted text
    feedback = generate_feedback(extracted_text)

    # Remove the temporary file
    os.remove("temp.pdf")

    return feedback
