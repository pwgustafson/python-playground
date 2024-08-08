from openai import OpenAI
from pathlib import Path
from config import openai_api_key

client = OpenAI(
    # Put your openai api key in the config.py file in this dir
    api_key = openai_api_key
)

audio_file = open("speech-files/harvard.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
print(transcript.text)


# speech_file_path = Path(__file__).parent / "speech-files/speech.mp3"
# response = client.audio.speech.create(
#   model="tts-1",
#   voice="alloy",
#   input="The quick brown fox jumped over the lazy dog."
# )
# response.stream_to_file(speech_file_path)


# stream = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Tell me a kids story about a dog who gets lost in the woods."}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)

