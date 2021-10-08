import speech_recognition as sr
import pywhatkit
import datetime
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',125)
td = datetime.datetime.today()
td = str(td)
if int(td[17:19]) >= 40:
    tds = int(td[14:16])+2
else:
    tds = int(td[14:16])+1
def whatsy():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            try:
                voice = listener.listen(source)
            except:
                print("not recognized")
            command = listener.recognize_google(voice)
            command = command.lower()
            
            print(command)
            if command != '':
                print(command)
            if 'whatsy' in command:
                runwhatsy(command)     
    except:
        pass
def runwhatsy(command):
    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def contact(co):
        if co == 'maa' or co == 'ma' or co == 'mom' or co == 'mummy':
            return 'xxxxxxxxxx'
        elif co == 'papa':
            return 'xxxxxxxxxx'
        
        else:
            return 'no such contact exist , say ok to tell phone number otherwise say leave it'
        
    def removespace(string): 
        l = len(string)
        if l == 0:
            return string
        so = removespace(string[1:])
        if string[0] == ' ':
            return so
        else:
            return string[0] + so
        pass

    if  'thank you whatsy' in command or  'whatsy thank you' in command :
        talk('it was my pleasure')
    if 'whatsy you are very sweet' in command or 'you are sweet whatsy' in command:
        talk('thank you for being so kind')
    if 'whatsy send' in command or 'whatsy sent' in command or 'whatsy text' in command or 'whatsy test' in command:
        co = command.rindex(' ')
        if command[co+1].isdigit():
            k = 0
            for i in range(0,len(command)):
                if  command[i].isdigit() and command[i+1].isdigit() and command[i+2].isdigit():
                    k = i
                    break
            c = removespace(command[k:])
            c2 = c
            t = k-4
        else:
            c1 = command[co+1:]
            c1 = c1.lower()
            c = contact(c1)
            c2 = c1
            if c[0].isdigit():
                c = c
                t = co-3
            else:
                talk(c)
                t = co - 3
                with sr.Microphone() as sour:
                    print('Listening....')
                    voice = listener.listen(sour)
                    command2 = listener.recognize_google(voice)
                    command2 = command2.lower()
                    if command2 == 'ok' or command2 == 'okay':
                        talk('please tell me the number')
                        with sr.Microphone() as sou:
                            print('Listening....')
                            voice = listener.listen(sou)
                            command3 = listener.recognize_google(voice)
                            c = removespace(command3)
                            c2 = c
                    elif 'leave' in command2 or 'live' in command2:
                        talk('okay')
                    else:
                        talk('sorry , i was unable to recieve any instruction')
                
            num = '+91'+c
            if c[0].isdigit():
                sp = "Sending "+command[11:t]+" to "+ c2
                print(sp)
                talk(sp)
                pywhatkit.sendwhatmsg(num , command[11:t], int(td[11:13]) , tds, 10 )
                talk('message sent')
                with sr.Microphone() as so:
                        print('Listening....')
                        voice = listener.listen(so)
                        command4 = listener.recognize_google(voice)
                        command4 = command4.lower()
                        if command4 == 'whatsy dont send' or command4 == 'whatsy do not send' or 'whatsy leave it' in command4:
                            print('process terminated')

whatsy()
