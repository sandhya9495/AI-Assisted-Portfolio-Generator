def read_uploaded_resume(uploaded_file):

    if uploaded_file is None:
        raise ValueError("Please upload a resume.")

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        text = uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

    elif file_name.endswith(".pdf"):
        try:
            from PyPDF2 import PdfReader

            reader = PdfReader(uploaded_file)

            pages = []

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    pages.append(page_text)

            text = "\n".join(pages)

        except Exception as error:
            raise ValueError(
                f"PDF reading error: {error}"
            )

    elif file_name.endswith(".docx"):
        try:
            from docx import Document

            document = Document(uploaded_file)

            paragraphs = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():
                    paragraphs.append(
                        paragraph.text.strip()
                    )

            text = "\n".join(paragraphs)

        except Exception as error:
            raise ValueError(
                f"DOCX reading error: {error}"
            )

    else:
        raise ValueError(
            "Only TXT, PDF and DOCX resumes are supported."
        )

    cleaned_text = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    if not cleaned_text:
        raise ValueError(
            "Resume is empty or could not be read."
        )

    if len(cleaned_text) < 50:
        raise ValueError(
            "Resume is too short. Please upload a proper resume."
        )

    return cleaned_text