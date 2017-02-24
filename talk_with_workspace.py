import speech_recognition as sr
import json
import requests

import config

r = sr.Recognizer()


def send_message(text, space):
    """Send text to workspace"""

    # get access token
    response = requests.post(
        url='https://api.watsonwork.ibm.com/oauth/token',
        auth=(config.VOICE_APP_ID, config.VOICE_APP_SECRET),
        data={
            'grant_type': 'client_credentials'
        }
    )
    access_token = json.loads(response.content.decode('utf-8'))['access_token']

    # send message to workspace
    requests.post(
        'https://api.watsonwork.ibm.com/v1/spaces/{space}/messages'.format(space=space),
        data=json.dumps(
            {
                'version': 1.0,
                'type': 'appMessage',
                'annotations': [{'version': 1.0, 'type': 'generic', 'text': text}]
            }
        ),
        allow_redirects=False,
        headers={
            'jwt': access_token,
            'content-type': 'application/json'
        }
    )


def run():
    while True:
        print('Say something')
        with sr.Microphone() as source:
            audio = r.listen(source)

        text = r.recognize_ibm(audio, username=config.IBM_USERNAME, password=config.IBM_PASSWORD)
        send_message(text, config.WORKSPACE_SPACE_ID)


run()