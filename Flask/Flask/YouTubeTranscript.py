import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import speech_recognition as sr
import conversion
from conversion import downloadvideo,startConvertion

from pytube import YouTube
import os
from transformers import pipeline
import nltk
import re
from nltk.corpus import stopwords
import transformers
from googletrans import Translator
from transformers import BartTokenizer, BartForConditionalGeneration
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
# import sklearn
# from sklearn.feature_extraction.text import TfidfVectorizer
global flag
link = "https://www.youtube.com/watch?v=g85WsxE1gAU" 
def getSummary(link):
    unique_id = link.split("=")[1]
    if os.path.isfile('Audio/output.wav'):
                        os.remove('output.wav')
    def transcript(sub):
        subtitle = " ".join([x['text'] for x in sub])
        input_tensor = tokenizer.encode( subtitle, return_tensors="pt", max_length=512)
        outputs_tensor = model.generate(input_tensor, max_length=260, min_length=120, length_penalty=2.0, num_beams=4, early_stopping=True)
        outputs_tensor
        text=tokenizer.decode(outputs_tensor[0])
        text2=text[7:-4]
        file1 = open("summary.txt", "w+") 
        for j in text2.split('.'):
            file1.write('-'+j +'.'+ '\n'+'\n')
          
        
        file1.close()
        file1 = open('summary.txt', 'r')
        p=file1.read()
        file1.close()
        file2 = open("English.txt", "w+") 
        file2.write(p)
        file2.close()
        
        print(p)
        return p
    
    # def startConvertion(path = 'Audio/output.wav',lang = 'en-IN'):
    #         with sr.AudioFile(path) as source:
    #             print('Fetching File')
    #             r=sr.Recognizer()
    #             audio_text = r.listen(source)
    #             try:
    #                 print('Converting audio transcripts into text ...')
    #                 text = r.recognize_google(audio_text,language=lang)
    #                 print(text)
    #                 summarization = pipeline('summarization')
    #                 summarized_text = summarization(text)
    #                 summary=summarized_text[0]['summary_text']
    #                 print(summary)
    #                 file1 = open("summary.txt", "w+") 
    #                 for j in summary.split('.'):
    #                     file1.write('-'+j +'.'+ '\n'+'\n')
    #                 file1.close()
    #                 file1 = open('summary.txt', 'r')
    #                 p=file1.read()
    #                 file1.close()
    #                 file2 = open("English.txt", "w+") 
    #                 file2.write(p)
    #                 file2.close()
    #                 print(p)
    #                 return p
                    
                    
                                       
    #             except:
    #                 print('Sorry.. run again...')
                    #return("Can not summarize")
         
                
                    
        
      
        
    try: 
        print('in try')
        sub = YouTubeTranscriptApi.get_transcript(unique_id) 
        return transcript(sub)
        
    
    except Exception as e:
        print('error')
        
        s=downloadvideo(link)
        if s:
            q=startConvertion()
            return q
        # yt = YouTube(link)
        # yt.streams.filter(only_audio = True, file_extension = 'mp4').first().download(filename = 'Audio/ytaudio.mp4')
        # os.system('ffmpeg -i Audio/ytaudio.mp4 Audio/output.wav')
        # p=startConvertion()
        else:
            return "Not done"
    

def hinditranslate():
    translator =Translator()
    file1 = open('English.txt','r', encoding='utf8')
    p=file1.read()
    file1.close()
    ch=translator.translate(p, dest='hi')
    m=ch.text
    file2=open('summary.txt','w+', encoding='utf8')
    file2.write(m)
    
    file2.close()
    flag='hindi'
    
    print(m)
    
    return m
def englishtranslate():
    translator =Translator()
    file1 = open('English.txt','r', encoding='utf8')
    p=file1.read()
    file1.close()
    ch=translator.translate(p, dest='en')
    m=ch.text
    file = open('summary.txt', 'w+')
    file.write(m)
    file.close()
    print('yesss')
    print(m)
    
    return p
def mrathitranslate():
    translator =Translator()
    file1 = open('english.txt', 'r', encoding='utf8')
    p=file1.read()
    file1.close()
    ch=translator.translate(p, dest='mr')
    m=ch.text
    file2=open('summary.txt','w+', encoding='utf8')
    file2.write(m)
    
    file2.close()
    
    
    print(m)
    
    return m
def checkforlang():
    return flag
    
