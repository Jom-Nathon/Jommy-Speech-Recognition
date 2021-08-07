import sys
sys.path.append('C:\Python39\Lib\site-packages')

import speech_recognition as sr

def main():
    print('This is main!')
    # r = sr.Recognizer()

    # useFile = False

    # if (useFile == False) :
    #     with sr.Microphone() as source:
    #         print('เริ่มพูดได้')
    #         audio = r.listen(source)

    #         try:
    #             text = r.recognize_google(audio, language='th')
    #             print('คุณพูด : {}'.format(text))

    #         except:
    #             print('ไม่สามารถแปลคำพูดได้')

    # elif(useFile == True) :
    #     print('ใส่ที่อยู่ไฟล์เสียง')
    #     fileName = input()
    #     with sr.AudioFile(fileName) as source:
    #         print('แปลภาษา')
    #         audio = r.listen(source)

    #         try:
    #             text = r.recognize_google(audio, language='th')
    #             print('แปลได้ : {}'.format(text))

    #         except:
    #             print('ไม่สามารถแปลคำพูดได้')

def fileAudio(folder_path):
    r = sr.Recognizer()
    
    with sr.AudioFile(folder_path) as source:
            print('แปลภาษา')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='th')
                return 'แปลได้ :' + ' ' + format(text)

            except:
                return ('ไม่สามารถแปลคำพูดได้')

def micAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
            print('เริ่มพูดได้')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='th')
                return 'แปลได้ :' + ' ' + format(text)

            except:
                return ('ไม่สามารถแปลคำพูดได้')

if __name__ == "__main__":
    main()
    micAudio()
    fileAudio()