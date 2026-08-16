import json


def parse_gemini_response(response):
    """
    Convert Gemini's JSON response into a Python dictionary.
    """

    try:
        data = json.loads(response)

    except json.JSONDecodeError:
        raise ValueError("Gemini returned invalid JSON.")

    if not isinstance(data, dict):
        raise ValueError("Gemini response must be a JSON object.")

    return data


def normalize_data(data):
    """
    Make sure all required fields exist.
    Missing fields are replaced with empty values.
    """

    portfolio = {
        "name": data.get("name", ""),
        "headline": data.get("headline", ""),
        "summary": data.get("summary", ""),
        "skills": data.get("skills", []),
        "education": data.get("education", []),
        "experience": data.get("experience", []),
        "projects": data.get("projects", []),
        "achievements": data.get("achievements", []),
        "contact": data.get("contact", {})
    }

    # Make sure list fields are lists
    if not isinstance(portfolio["skills"], list):
        portfolio["skills"] = []

    if not isinstance(portfolio["education"], list):
        portfolio["education"] = []

    if not isinstance(portfolio["experience"], list):
        portfolio["experience"] = []

    if not isinstance(portfolio["projects"], list):
        portfolio["projects"] = []

    if not isinstance(portfolio["achievements"], list):
        portfolio["achievements"] = []

    # Make sure contact is a dictionary
    if not isinstance(portfolio["contact"], dict):
        portfolio["contact"] = {}

    contact = portfolio["contact"]

    portfolio["contact"] = {
        "email": contact.get("email", ""),
        "phone": contact.get("phone", ""),
        "linkedin": contact.get("linkedin", ""),
        "github": contact.get("github", "")
    }

    return portfolio


def process_gemini_response(response):
    """
    Complete JSON processing pipeline.

    Gemini response
          ↓
    JSON parsing
          ↓
    Validation
          ↓
    Normalization
          ↓
    Clean portfolio data
    """

    data = parse_gemini_response(response)

    data = normalize_data(data)

    return data