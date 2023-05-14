import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# specify the audio file path
audio_file = "path/to/audio/file.wav"

# use the recognizer to open the audio file
with sr.AudioFile(audio_file) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)

# transcribe the audio data
text = r.recognize_google(audio_data)

# print the transcribed text
print(text)
