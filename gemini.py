import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured in the .env file."
    )



client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.1-flash-lite"



RESUME_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },

        "email": {
            "type": "string"
        },

        "phone": {
            "type": "string"
        },

        "location": {
            "type": "string"
        },

        "linkedin": {
            "type": "string"
        },

        "github": {
            "type": "string"
        },

        "summary": {
            "type": "string"
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
                    "grade": {
                        "type": "string"
                    }
                },
                "required": [
                    "degree",
                    "institution",
                    "year",
                    "grade"
                ]
            }
        },

        "experience": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "job_title": {
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
                    "job_title",
                    "company",
                    "duration",
                    "description"
                ]
            }
        },

        "skills": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        "projects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
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
                    }
                },
                "required": [
                    "name",
                    "description",
                    "technologies",
                    "link"
                ]
            }
        },

        "certifications": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "issuer": {
                        "type": "string"
                    },
                    "year": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "issuer",
                    "year"
                ]
            }
        },

        "achievements": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },

    "required": [
        "name",
        "email",
        "phone",
        "location",
        "linkedin",
        "github",
        "summary",
        "education",
        "experience",
        "skills",
        "projects",
        "certifications",
        "achievements"
    ]
}



SYSTEM_PROMPT = """
You are a resume information extraction assistant.

Your task is to extract information from the provided resume text
and return it in the exact JSON structure requested.

IMPORTANT RULES:

1. Use ONLY information present in the resume.
2. NEVER invent, assume, or hallucinate information.
3. Do not add skills, projects, companies, degrees, dates,
   certifications or achievements that are not present.
4. Preserve the meaning of the original resume.
5. If a simple text field is missing, return an empty string.
6. If an array section is missing, return an empty array.
7. Return ONLY valid JSON.
8. Do not add Markdown.
9. Do not add ```json.
10. Do not add explanations before or after the JSON.
11. Keep the output compatible with the provided JSON schema.
"""


def generate_resume_json(resume_text):
    """
    Takes raw resume text and converts it into structured JSON.
    """

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
            raise RuntimeError(
                "Gemini returned an empty response."
            )


        resume_data = json.loads(response.text)

        return resume_data


    except json.JSONDecodeError as error:

        raise RuntimeError(
            "Gemini returned invalid JSON."
        ) from error


    except Exception as error:

        raise RuntimeError(
            f"Gemini API request failed: {error}"
        ) from error



def resume_to_json_string(resume_text):
    """
    Returns formatted JSON string.
    Useful when another module needs JSON text.
    """

    resume_data = generate_resume_json(resume_text)

    return json.dumps(
        resume_data,
        indent=4,
        ensure_ascii=False
    )



if __name__ == "__main__":
    print("Gemini Resume Parser is ready.")
    print("Use generate_resume_json(resume_text) to convert resume text into structured JSON.")
    