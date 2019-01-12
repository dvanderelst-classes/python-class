import subprocess
import time
import tkinter as tk
from tkinter import W, E, S, END, font

from watson_developer_cloud import TextToSpeechV1

from course import sms


class HelloApp:
    def __init__(self, master):
        self.root = master

        # Set up tts engine
        self.key = '4YWiR3Z5Lc7LY_eTW_5nzlWp4ALZXLTgTVQpkYIUYIXM'
        self.url = 'https://stream.watsonplatform.net/text-to-speech/api'
        self.voice = 'en-GB_KateVoice'
        self.engine = TextToSpeechV1(iam_apikey= self.key, url=self.url)

        # Set up the sms query tool
        self.sms_tool = sms.SmsTool()
        self.last_id = 'none'

        # Define Fonts
        self.font1 = font.Font(family="Helvetica", size=36, weight="bold")
        self.font2 = font.Font(family="Helvetica", size=18, weight="bold")
        self.nr = '+1 513 817 0877'

        # Label value
        self.label_value = tk.StringVar()

        # Make widgets
        self.text_label = tk.Label(textvariable=self.label_value, width=50, justify=tk.CENTER, font=self.font1)
        self.sms_text = tk.Text(width=50, font=self.font2)

        # Add the widgets to their parents
        self.text_label.grid(row=0, column=0, sticky=W + E)
        self.sms_text.grid(row=1, column=0, sticky=W + E + S)

        # Start this thing...
        self.label_value.set('Send messages to ' + self.nr)
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
        current_id = last['msid']
        age = last['age']
        body = last['body']
        sender = last['from']
        if not current_id == self.last_id and age < 30:
            self.last_id = current_id
            return body, sender
        return False, False

    def speak(self, text):
        text = text.rstrip('.')
        text = text.rstrip(' ')
        text = text.capitalize()
        text = 'A new message. ' + text + '.'
        print('TEXT2SPEAK: ' + text)
        response = self.engine.synthesize(text, voice=self.voice)
        result = response.get_result()
        data = result.content
        audio_file = open('audio.wav', 'wb')
        audio_file.write(data)
        audio_file.close()
        subprocess.check_call(['cvlc', 'audio.wav', '--play-and-exit'])

    def update_sms_text(self, sender, text):
        text_string = time.asctime() + ' ' + str(sender) + ' said:\n' + text
        if sender is None: text_string = text
        text_string = text_string + '\n'
        # self.sms_text.delete(1.0, END) # delete text
        self.sms_text.insert(END, text_string)


if __name__ == "__main__":
    root = tk.Tk()
    app = HelloApp(root)
    root.mainloop()
