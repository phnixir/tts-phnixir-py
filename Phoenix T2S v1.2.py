import win32com.client
e = win32com.client.Dispatch("SAPI.SpVoice")

def quickaccess():
       e.Speak(cmd)

print('Hello im Mr.Johnson')
e.Speak('hello im mister johnson')

tts = True
while tts == True:
    cmd = input()
    quickaccess()



