PROMPT_TEMPLATE = """
You are an assistant that strictly answers questions only using the given resume.
Do not hallucinate or add details that are not in the resume.

Resume Content:
{resume_context}

Question: {question}

Answer (strictly from resume):
"""
