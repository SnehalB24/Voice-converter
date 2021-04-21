#import required modules

import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment

# Converting mp3 to wav file
input_file = "trees.mp3"
output_file = "Trees.wav"

music= AudioSegment.from_mp3(input_file)
music.export(output_file, format="wav")

# Converting Audio file into text

audioFile = "Trees.wav"
r = sr.Recognizer()

with sr.AudioFile(audioFile) as data:
    audio_data = r.record(data)
    text = r.recognize_google(audio_data)
    print(text)

#Converting male voice into female voice

engine=pyttsx3.init()
sound=engine.getProperty("voices")

print("Male voice:{0}".format(sound[0].id))
print("Female voice:{0}".format(sound[1].id))
engine.setProperty("voice", sound[1].id)


engine.say(text)
engine.runAndWait()
