# -*- coding: UTF-8 -*-
import os
import openai
import config
import json

class GPT:    
    def __init__(self, API = None):
        print("[INFO] Init GPT API...")

        print(API)

        if (API): openai.api_key = API
        else: openai.api_key = config.CHATGPT_API_KEY

        self.model_id = "gpt-3.5-turbo"
        self.messages = []

    def getAnswer(self, question):
        print("[INFO] Question : \n" + config.TASK + '\n\n' + question)
        # Append question into messages list
        self.messages.append({"role": "user", "content": config.TASK + '\n\n' + question})
        # Generate Response from GPT
        self.completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        # Print Response
        print("[INFO] Answer : \n\n" + self.completion.choices[0].message.content)
        answer = self.completion.choices[0].message.content
        # Erase context to free up space needed for new questions
        self.messages = []
        return answer

