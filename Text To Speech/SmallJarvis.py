import pyttsx3

jarvis = pyttsx3.init()
jarvis.say("Hello")       #To fast
jarvis.runAndWait()       #To wait so that we can hear.

#We can also change the properties of the voice using jarvis.setProperty("voice", voices[1].id)
#We can change the speed and rate of the voice using
# jarvis.setProperty("volume", 1)
# jarvis.setProperty("rate", 200)
