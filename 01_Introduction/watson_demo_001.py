from watson_developer_cloud import TextToSpeechV1
import subprocess
import json

text_to_speech = TextToSpeechV1(iam_apikey='4YWiR3Z5Lc7LY_eTW_5nzlWp4ALZXLTgTVQpkYIUYIXM', url='https://stream.watsonplatform.net/text-to-speech/api')
response = text_to_speech.synthesize('test this')
result = response.get_result()
data = result.content

audio_file = open('audio.wav', 'wb')
audio_file.write(data)
audio_file.close()


subprocess.check_call(['cvlc', 'audio.wav', '--play-and-exit'])
subprocess.check_call(['cvlc', 'audio.wav', '--play-and-exit'])


voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=2))