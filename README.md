# Resume Reviewer AI

Resume Reviewer AI is a web application powered by FastAPI and LangChain's GoogleGenerativeAI. It analyzes resumes uploaded by users and generates feedback on the candidate's qualifications, skills, and experience related to a specified job role.

## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)


## Installation

To set up the project locally, follow these steps:

1. Install Dependencies:
    ```bash
    pip install -r requirements.txt

2. Clone the repository:

    ```bash
    git clone https://github.com/vikascod/resume-reviewer

3. Set up environment variables:

Create a .env file in the project root directory and add the following:

    ```bash
    GOOGLE_API_KEY=your_google_api_key_here

4. To run the application locally, execute the following command:

    ```bash
    uvicorn main:app --reload


## API Endpoints

### Resume Feedback

- **Endpoint:** `/resume-feedback/`
- **Method:** POST
- **Description:** Analyzes the uploaded resume file and generates feedback.
- **Request Body:**
  - `file`: The resume file to be analyzed (PDF format).
- **Response:**
  - JSON object containing the generated feedback.

#### Example Request:

    ```bash
    {
        "feedback": "The candidate possesses strong programming skills and experience in software development, which makes them a suitable candidate for the Software Development Engineer role."
    }
