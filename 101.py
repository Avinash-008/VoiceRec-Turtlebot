import speech_recognition as sr
r = sr.Recognizer()

with sr.WavFile('ho.wav')  as source:
    audio = r.record(source)
#r = sr.Recognizer()  if microphone is to be used, then this set of codes will be utilised
#with sr.Microphone() as source:
    #print("Say something!")
    #audio = r.listen(source)


try:
    s = r.recognize_google(audio)
    print("Text: "+s)
    if "kitchen" in s:
        import kitchen.py
    if "room one" in s:
        import room1.py
    if "room two" in s:
        import room2.py
    if "hall" in s:
        import hall.py
    if "charging" in s:
        import charging.py
        
except Exception as e:
    print("Exception: "+str(e))
