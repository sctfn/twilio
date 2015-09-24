from flask import Flask, request, redirect
import os
import twilio.twiml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rebooter():
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say('Welcome to reboot')
    with resp.gather(numDigits=1, action='/handle-key', method='POST') as g:
        g.say('To reboot this machine, press 1. Press any other key to start over.')
    return str(resp)

@app.route('/handle-key', methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == '1':
        resp = twilio.twiml.Response()
        resp.say('Rebooting now')
        os.system('reboot')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
