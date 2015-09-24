from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rebooter():
    auth = request.values.get('auth', None)
    if auth == 'go':
        os.system('reboot')
    else:
        return 'Need auth key!'
        
if __name__ == '__main__':
    app.run(host='0.0.0.0')

