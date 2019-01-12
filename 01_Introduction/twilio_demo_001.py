import time
# Reads out any new message sent to a text service
import tkinter as tk
from tkinter import W, E, N, S, END, font


from watson_developer_cloud import TextToSpeechV1
import subprocess

text_to_speech = TextToSpeechV1(iam_apikey='4YWiR3Z5Lc7LY_eTW_5nzlWp4ALZXLTgTVQpkYIUYIXM', url='https://stream.watsonplatform.net/text-to-speech/api')
response = text_to_speech.synthesize('test this')
result = response.get_result()
data = result.content

audio_file = open('audio.wav', 'wb')
audio_file.write(data)
audio_file.close()


subprocess.check_call(['cvlc', 'audio.wav', '--play-and-exit'])
subprocess.check_call(['cvlc', 'audio.wav', '--play-and-exit'])


import pyttsx3

from course import sms

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', 'en-scottish')
#engine.setProperty('rate', 95)

#
# nr = '+1 513 817 0877'
#
# msg_wait = 'Waiting for message. Send messages to ' + nr
#
# sms_tool = sms.SmsTool()
# last_id = 'none'
# print(msg_wait)
# for x in range(0, 1000):
#     last = sms_tool.get_last_msg(sms_type='inbound')
#     current_id = last['msid']
#     age = last['age']
#     body = last['body']
#     if not current_id == last_id and age < 30:
#         msg_rcvd = 'New message received: ' + body
#         print(msg_rcvd)
#         engine.say(msg_rcvd)
#         engine.runAndWait()
#         print(msg_wait)
#         last_id = current_id
#     time.sleep(5)


class HelloApp:
    def __init__(self, master):
        self.root = master
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english+f1')
        self.engine.setProperty('rate', 100)
        voices = self.engine.getProperty('voices')
        for voice in voices: print(voice, voice.id)

        self.sms_tool = sms.SmsTool()
        self.last_id = 'none'
        self.font1 = font.Font(family="Helvetica", size=36, weight="bold")
        self.font2 = font.Font(family="Helvetica", size=18, weight="bold")
        self.nr = '+1 513 817 0877'

        self.label_value = tk.StringVar()


        self.text_label = tk.Label(textvariable=self.label_value, width=50, justify=tk.CENTER, font=self.font1)
        self.sms_text = tk.Text(width=50, font=self.font2)

        # Add the widgets to their parents
        self.text_label.grid(row=0, column=0, sticky=W + E)
        self.sms_text.grid(row=1, column=0, sticky=W + E + S)

        self.label_value.set('Send messages to ' + self.nr)
        #self.update_sms_text(None, 'No messages yet')

        self.cycle()

    def cycle(self):
        print('Checked at ' + time.asctime())
        text, sender = self.check_for_text()
        if text:
            self.update_sms_text(sender, text)
            self.root.update()
            self.speak(text)
        self.root.after(5000, self.cycle)

    def check_for_text(self):
        last = self.sms_tool.get_last_msg(sms_type='inbound')
        print(last)
        current_id = last['msid']
        age = last['age']
        body = last['body']
        sender = last['from']
        if not current_id == self.last_id and age < 30:
            self.last_id = current_id
            return body, sender
        return False, False

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


    def update_sms_text(self, sender, text):
        text_string = time.asctime() +' ' + str(sender) + ' said:\n' + text
        if sender is None: text_string = text
        text_string = text_string + '\n'
        #self.sms_text.delete(1.0, END) # delete text
        self.sms_text.insert(END, text_string)






if __name__ == "__main__":
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()
