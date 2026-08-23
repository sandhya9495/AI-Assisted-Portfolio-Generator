# AI-Assisted Portfolio Generator

An AI-powered web application that automatically generates a professional personal portfolio from a user's resume.

## 🚀 Features

* Upload resume in TXT, PDF, or DOCX format
* Upload a profile photo
* Extract resume information using Google Gemini AI
* Convert resume information into structured JSON
* Automatically generate a professional HTML portfolio
* Display skills, education, experience, projects, achievements, and contact information
* Add GitHub links for projects
* Responsive portfolio design
* Simple and user-friendly interface
* Resume data is processed locally before portfolio generation

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* HTML
* CSS
* JavaScript
* python-dotenv

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
```

## ⚙️ How It Works

1. Upload your resume.
2. Upload your profile photo.
3. The application extracts the resume text.
4. Gemini AI converts the resume information into structured JSON.
5. The portfolio generator uses the extracted information.
6. A professional HTML portfolio is generated automatically.

## 🔑 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sandhya9495/AI-Assisted-Portfolio-Generator.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Assisted-Portfolio-Generator
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.env` file in the project directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your `.env` file or expose your Gemini API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔐 Environment Variables

The application uses the following environment variable:

```text
GEMINI_API_KEY
```

This key is required to communicate with the Google Gemini API.

## 📸 Project Preview

The application provides a simple interface where users can upload their resume and profile photo and generate a professional portfolio automatically.

## 🎯 Future Improvements

* Add multiple portfolio templates
* Add more portfolio design themes
* Add AI-generated professional summaries
* Add direct portfolio deployment
* Add custom domain support
* Add more resume file formats
* Add portfolio customization options

## 📄 License

This project is created for educational and portfolio purposes.
