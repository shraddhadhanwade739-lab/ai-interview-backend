import openai, os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_question(transcript, resume_text):
    prompt = f"""
    Candidate Resume: {resume_text}
    Last Answer Transcript: {transcript}
    Generate the next interview question.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_feedback(transcript):
    prompt = f"Give constructive interview feedback based on this answer: {transcript}"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
