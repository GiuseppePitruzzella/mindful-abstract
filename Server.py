from flask import Flask, render_template, request
import json
from video_handler import *
import json
from GPT import *

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRoutes()
        self.Video = Video()
        self.GPT = GPT()
        self.startServer()

    def startServer(self):
        self.app.run(debug = True, host = '0.0.0.0', port=10001)
    
    def defineRoutes(self):
        @self.app.route('/')
        def getIndex():
            return render_template('index.html')
        
        @self.app.route('/getAbstract', methods=['POST'])
        def getAbstract():
            return render_template('summarium.html', data=json.dumps(self.GPT.getAnswer(self.Video.getTranscription(link = request.form['link']))))
        
        

 
