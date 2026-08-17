def read_resume(filename="resume.txt"):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Error: {filename} not found."
        )

    
    cleaned_text = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    
    if not cleaned_text:
        raise ValueError(
            "Error: Resume is empty. Please provide your resume."
        )

    
    if len(cleaned_text) < 50:
        raise ValueError(
            "Error: Resume is too short. Please provide more information."
        )

    return cleaned_text

if __name__ == "__main__":
    try:
        resume = read_resume()

        print("Resume successfully loaded!")
        print("\n--- Cleaned Resume ---")
        print(resume)

    except (FileNotFoundError, ValueError) as error:
        print(error)


