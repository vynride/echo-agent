from assembly import get_transcript
from murf import gen_voiceover

try:
    transcript = get_transcript()
    print(f"Got Transcript from AssemblyAI\n {transcript}")

    voice_id = "en-US-amara"
    style = "Conversational"

    gen_voiceover(transcript, voice_id, style)
    
except Exception as e:
    print(f"Error {e} occured when calling AssemblyAI for transcription.")
