#!/usr/bin/env python

"""reboot_dispatch.py - dispatch a reboot request to a machine
from a Twilio request.

-Scott Fenton <sctfen@gmail.com>"""

import os
import urllib
import urllib2

import twilio.twiml
from flask import Flask, request, redirect

MACHINES = {
    1 : 'stibbons',
    2 : 'luggage'
}

REBOOT_PORT = 5000


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rebooter():
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say('Welcome to reboot')
    with resp.gather(numDigits=1, action='/handle-key', method='POST') as g:
        for num, machine in sorted(MACHINES.items()):
            resp.say('To reboot {0}, press {1}.'.format(machine, num))
    return str(resp)

@app.route('/handle-key', methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits', None)
    digit = int(digit_pressed)

    try:
        machine = MACHINES[digit]
        try:
            data = urllib.urlencode({'auth' : 'go'})
            url = 'http://{0}:{1}/'.format(machine, REBOOT_PORT)
            req = urllib2.Request(url, data)
            response.urllib2.urlopen(req)
        except urllib2.URLError:
            pass
        resp.say('Reboot signal sent to {0}'.format(machine))
        return str(resp)
            
    except KeyError:
        resp.say("I'm sorry. That number is not matched to a machine.")
        return redirect('/')
