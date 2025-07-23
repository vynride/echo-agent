from assemblyAI import get_transcript
from murfAI import play_transcript

def call_agent():
    try:
        transcript = get_transcript()
        print(f"Got Transcript from AssemblyAI\n {transcript}")
        
        print(f"Calling Murf for playing response")
        voice_id = "en-US-amara"
        style = "Conversational"

        play_transcript(transcript, voice_id, style)
        print("Finished playing response")

        return 0

    except Exception as e:
        print(f"Error {e} occured")

        return 1
