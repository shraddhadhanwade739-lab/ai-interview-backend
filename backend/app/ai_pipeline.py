import assemblyai as aai
import os

aai.settings.api_key = os.getenv("ASSEMBLYAI_KEY")

def transcribe_audio(file_path):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    return transcript.text
