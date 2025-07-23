from assembly import get_transcript
from murf import play_transcript

def play_transcript(TRANSCRIPT, VOICEID, STYLE):

try:
    transcript = get_transcript()
    print(f"Got Transcript from AssemblyAI\n {transcript}")
    
    print(f"Calling Murf for playing response")
    voice_id = "en-US-amara"
    style = "Conversational"
    
    play_transcript(transcript, voice_id, style)
    print("Finished playing response")
    
except Exception as e:
    print(f"Error {e} occured")
