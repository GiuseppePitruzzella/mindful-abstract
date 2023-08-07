# -*- coding: UTF-8 -*-
import os
import openai
import config
import json

class GPT:
    def __init__(self):
        print("[INFO] Init GPT API...")
        openai.api_key = config.CHATGPT_API_KEY
        self.model_id = "gpt-3.5-turbo"
        self.messages = config.HISTORY

    def saveMessage(self, question = None, answer = None):
        if question: self.messages.append({"role": "user", "content": question})
        if answer: self.messages.append({"role": "assistant", "content": answer})

    def getAnswer(self, question):
        return "OK"
        print("[INFO] Question : \n\t" + question)
        self.saveMessage(question=question)
        self.completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        print("[INFO] Answer : \n\t" + self.completion.choices[0].message.content)
        answer = self.completion.choices[0].message.content
        self.saveMessage(answer=answer)
        return answer

