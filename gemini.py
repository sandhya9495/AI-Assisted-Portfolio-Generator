import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured in the .env file.")


client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.1-flash-lite"


RESUME_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "headline": {
            "type": "string"
        },
        "summary": {
            "type": "string"
        },
        "image": {
            "type": "string"
        },
        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "education": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "degree": {
                        "type": "string"
                    },
                    "institution": {
                        "type": "string"
                    },
                    "year": {
                        "type": "string"
                    },
                    "details": {
                        "type": "string"
                    }
                },
                "required": [
                    "degree",
                    "institution",
                    "year",
                    "details"
                ]
            }
        },
        "experience": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string"
                    },
                    "company": {
                        "type": "string"
                    },
                    "duration": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                },
                "required": [
                    "role",
                    "company",
                    "duration",
                    "description"
                ]
            }
        },
        "projects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "technologies": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "link": {
                        "type": "string"
                    },
                    "images": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "title",
                    "description",
                    "technologies",
                    "link",
                    "images"
                ]
            }
        },
        "achievements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                },
                "required": [
                    "title",
                    "description"
                ]
            }
        },
        "contact": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string"
                },
                "phone": {
                    "type": "string"
                },
                "linkedin": {
                    "type": "string"
                },
                "github": {
                    "type": "string"
                }
            },
            "required": [
                "email",
                "phone",
                "linkedin",
                "github"
            ]
        }
    },
    "required": [
        "name",
        "headline",
        "summary",
        "image",
        "skills",
        "education",
        "experience",
        "projects",
        "achievements",
        "contact"
    ]
}


SYSTEM_PROMPT = """
You are an AI-assisted resume portfolio generator.

Extract information from the provided resume and return it
using exactly the JSON structure provided.

Rules:

1. Use only information present in the resume.
2. Never invent or assume information.
3. Do not create fake skills, experience, projects,
   companies, dates, achievements or links.
4. If information is missing, use an empty string.
5. If a list section is missing, use an empty array.
6. Keep the summary short and factual.
7. Return only valid JSON.
8. Do not return Markdown.
9. Do not add explanations.
10. Keep all field names exactly as provided.
"""


def generate_resume_json(resume_text):

    if not isinstance(resume_text, str):
        raise TypeError("resume_text must be a string.")

    resume_text = resume_text.strip()

    if not resume_text:
        raise ValueError("Resume text cannot be empty.")

    prompt = f"""
{SYSTEM_PROMPT}

RESUME TEXT:
--------------------
{resume_text}
--------------------

Extract the resume information now.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=RESUME_SCHEMA,
                temperature=0
            )
        )

        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")

        return json.loads(response.text)

    except json.JSONDecodeError as error:
        raise RuntimeError("Gemini returned invalid JSON.") from error

    except Exception as error:
        raise RuntimeError(
            f"Gemini API request failed: {error}"
        ) from error


def resume_to_json_string(resume_text):

    resume_data = generate_resume_json(resume_text)

    return json.dumps(
        resume_data,
        indent=4,
        ensure_ascii=False
    )


if __name__ == "__main__":

    print("Gemini Resume Parser is ready.")
    print(
        "Use generate_resume_json(resume_text) "
        "to convert resume text into structured JSON."
    )
    
