from flask import Flask, render_template, request
import json
from video_handler import *
import json
from emoji import UNICODE_EMOJI
import regex
from GPT import *

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.GPT = GPT()
        self.defineRoutes()
        self.Video = Video()
        self.startServer()

    def getApp(self):
        return self.app;

    def startServer(self):
        self.app.run(debug = True, host = '0.0.0.0', port=10001)

    def addTag(self, data, target, openTag = None, closeTag = None):
        index = data.find(target)

        if openTag:
            data = data[:index] + openTag + data[index:]
        if closeTag:
            if openTag: 
                index += len(target) + len(openTag)
            else: index += len(target)
            data = data[:index] + closeTag + data[index:]

        return data

    def formatData(self, data):
        data = self.addTag(data = data, target = 'Summary:', openTag = '<h2>', closeTag = '</h2><p class=text-xs>')
        data = self.addTag(data = data, target = 'Points:', openTag = '</p><br><h2>', closeTag = '</h2><p class=text-xs>')
        data = self.addTag(data = data, target = data.split()[-1], closeTag = '</p>')

        emoji = ''.join(c for c in data if c in UNICODE_EMOJI['en'])
        for e in emoji[1:]: data = self.addTag(data = data, target = e, openTag = '<br>')

        # print(data)

        return data
    
    def defineRoutes(self):
        @self.app.route('/')
        def getIndex():
            return render_template('index.html')
        
        @self.app.route('/getAbstract', methods=['POST'])
        def getAbstract():
            request_data = request.get_json()
            link = request_data.get('input_data')

            transcription = self.Video.getTranscription(link = link)
            response = self.GPT.getAnswer(question = transcription) # Try adding config.SETUP_MSG + transcription

            data = self.formatData(response)

            return render_template('summarium.html', data = json.dumps(data))
        
            return render_template('summarium.html', data=json.dumps(
                self.formatData(
                self.GPT.getAnswer(
                self.Video.getTranscription(link = request.form['input_data'])))))