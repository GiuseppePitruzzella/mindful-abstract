from youtube_transcript_api import YouTubeTranscriptApi
#srt = YouTubeTranscriptApi.get_transcript(video_id)
from GPT import *

class Video:
    def __init__(self):
        pass

    def getID(self, link):
        ID = link[32:43]
        print("[INFO] ID : " + ID)
        return ID

    def getTranscription(self, link):
        ID = self.getID(link)
        transcript_list, unretrievable_videos = YouTubeTranscriptApi.get_transcripts([ID], continue_after_error=True)
        text_list = []
        try:
            for i in transcript_list.get(ID):
                text_list.append(i['text'])
            transcription = ' '.join(text_list)

            print("[INFO] Transcription : " + transcription)

            return transcription
        except TypeError:
            print("[ERROR] Unretrivable Video!")