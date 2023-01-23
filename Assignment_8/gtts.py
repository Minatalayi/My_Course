import gtts
from gtts import gTTS
my_text="i am mina, a python programmer"
x=gtts.gTTS(my_text, lang="en", slow=False)
x.save("Assignment_8/voice.mp3")


