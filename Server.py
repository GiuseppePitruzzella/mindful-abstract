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
        self.defineRoutes()
        self.Video = Video()
        self.GPT = GPT()
        # self.GPT = None
        self.startServer()
        self.API = None

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

        return data
    
    def defineRoutes(self):
        @self.app.route('/')
        def getIndex():
            return render_template('index.html')
        
        # @self.app.route('/setAPI')
        # def setAPI():
        #     self.API = request.form['input_data']
        #     self.GPT = GPT()
        
        @self.app.route('/getAbstract', methods=['POST'])
        def getAbstract():
            return render_template('summarium.html', data = self.formatData(data = """
                Summary:
                Dependency injection is a technique where one piece of code is passed into another code instead of being directly used. This allows for more flexibility and modularity in the code structure. In the provided context, dependency injection is used to build a business app where users can chat, send attachments, and store them in different storage locations depending on the user's company. Different stages of the attachment process, such as virus scanning, image scaling, preview generation, and encryption, are also incorporated using dependency injection.

                Points:
                🔑 Dependency injection involves passing one piece of code into another code instead of directly using it.
                📩 A business app allows users to chat and send attachments, which are uploaded to an attachment service.
                💾 The attachment service is responsible for storing, retrieving, and processing attachments.
                ⚙️ Dependency injection is used to handle multiple storage locations, depending on the user's company.
                📷 Various stages, such as virus scanning, image scaling, preview generation, and encryption, are incorporated using dependency injection.
                🔒 Different implementations of scanners, image scalers, preview generators, and encryption are injected into the code.
                🧪 Dependency injection enables easy testing of individual components by injecting mock or fake implementations.
            """))
            return render_template('summarium.html', data=json.dumps(self.GPT.getAnswer(self.Video.getTranscription(link = request.form['input_data']))))