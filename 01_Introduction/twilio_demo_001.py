import sys
import time

# Reads out any new message sent to a text service

# This line adds the course module to the python path.
sys.path.insert(0, '/home/dieter/Dropbox/PythonRepos')

from course import sms
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'en-scottish')
engine.setProperty('rate', 95)

nr = '+1 513 817 0877'

msg_wait = 'Waiting for message. Send messages to ' + nr

sms_tool = sms.SmsTool()
last_id = 'none'
print(msg_wait)
for x in range(0, 1000):
    last = sms_tool.get_last_msg(sms_type='inbound')
    current_id = last['msid']
    age = last['age']
    body = last['body']
    if not current_id == last_id and age < 30:
        msg_rcvd = 'New message received: ' + body
        print(msg_rcvd)
        engine.say(msg_rcvd)
        engine.runAndWait()
        print(msg_wait)
        last_id = current_id
    time.sleep(5)
