# AI-Assisted Portfolio Generator

An AI-powered web application that automatically generates a professional personal portfolio from a user's resume.

## 🚀 Features

- Upload resume in TXT, PDF, or DOCX format
- Upload a profile photo
- Extract resume information using Gemini AI
- Automatically generate structured portfolio content
- Generate portfolio projects, skills, education, experience, achievements, and contact details
- GitHub links for projects
- Responsive portfolio design
- Simple and user-friendly interface
- Resume data is processed locally before portfolio generation

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- HTML
- CSS
- JavaScript
- python-dotenv

## 📂 Project Structure

```text
AI-Assisted-Portfolio-Generator/
│
├── app.py
├── gemini.py
├── input_handler.py
├── json_handler.py
├── html_generator.py
├── template.html
├── style.css
├── requirements.txt
├── profile.jpg
└── README.md

## ⚙️ How It Works

1. Upload your resume.
2. Upload your profile photo.
3. The application extracts the resume text.
4. Gemini AI converts the resume information into structured JSON.
5. The portfolio generator uses the extracted information.
6. A professional HTML portfolio is generated automatically.

## 🔑 Setup

Clone the repository:

git clone https://github.com/sandhya9495/AI-Assisted-Portfolio-Generator.git

Navigate to the project directory:

cd AI-Assisted-Portfolio-Generator

Install dependencies:

pip install -r requirements.txt

Create a `.env` file and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

Run the application:

streamlit run app.py

## 🔐 Environment Variables

The project uses the following environment variable:

GEMINI_API_KEY

Never upload your `.env` file or expose your Gemini API key publicly.

## 🎯 Future Improvements

- More portfolio templates
- Multiple design themes
- AI-generated portfolio summaries
- Portfolio deployment directly from the application
- More resume formats
- Custom domain support

## 📄 License

This project is created for educational and portfolio purposes.