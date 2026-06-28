from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
def analyze_resume(resume_text):

    # Improvement 1: Check if resume is empty
    if not resume_text.strip():
        return "No text found in the uploaded resume."

    try:
        # Improvement 2: Better Prompt
        prompt = f"""
        You are an expert ATS Resume Analyzer.

        Analyze the following resume and provide the result in this format:

        ATS Score: <score>/100

        Strengths:
        - point 1
        - point 2

        Weaknesses:
        - point 1
        - point 2

        Missing Skills:
        - skill 1
        - skill 2

        Resume Suggestions:
        - suggestion 1
        - suggestion 2

        Recommended Projects:
        - project 1
        - project 2

        Suitable Job Roles:
        - role 1
        - role 2

        Courses to Learn:
        - course 1
        - course 2

        Interview Questions:
        1.
        2.
        3.

        Resume:
        {resume_text}
        """

        # Send prompt to Groq
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content
        return result

    # Improvement 3: Error Handling
    except Exception as e:
        return f"Error occurred: {e}"
    
    