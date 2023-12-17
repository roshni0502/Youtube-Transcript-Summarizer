import speech_recognition as sr
from pytube import YouTube
import subprocess
import os
from transformers import pipeline
from transformers import BartTokenizer, BartForConditionalGeneration
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
import librosa
import soundfile as sf
import transformers
from googletrans import Translator
from transformers import BartTokenizer, BartForConditionalGeneration
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
# import sklearn
# from sklearn.feature_extraction.text import TfidfVectorizer

def downloadvideo(link):
    try:
        yt = YouTube(link)
        yt.streams.filter(only_audio = True, file_extension = 'mp4').first().download(filename = 'Audio/ytaudio.mp4')
        os.system('ffmpeg -i Audio/ytaudio.mp4 -acodec pcm_s16le -ar 16000 ytaudio.wav')
        input_file = 'ytaudio.wav'
        print(librosa.get_samplerate(input_file))
        stream = librosa.stream(
            input_file,
            block_length=30,
            frame_length=16000,
            hop_length=16000)
        for i,speech in enumerate(stream):
            sf.write(f'{i}.wav', speech, 16000)
            audio_path =[]
        for a in range(i+1):
            audio_path.append(f'/Audio/{a}.wav')
            print(audio_path)
        return True
    except:
        return False


def startConvertion(path = 'ytaudio.wav',lang = 'en-IN'):
    input_file = 'ytaudio.wav'
    print(librosa.get_samplerate(input_file))
    stream = librosa.stream(
    input_file,
    block_length=30,
    frame_length=16000,
    hop_length=16000)
    for i,speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, 16000)
    audio_path =[]
     
    for a in range(i+1):
        audio_path.append(f'{a}.wav')
    print(audio_path)
    full_transcript = ' '
    for a in (audio_path):
            with sr.AudioFile(a) as source:
                print('Fetching File')
                r=sr.Recognizer()
                audio_text = r.listen(source)
                f=0
                try:
                    print('Converting audio transcripts into text ...')
                    text = r.recognize_google(audio_text,language=lang)
                    f=1
                    print(text)
                    full_transcript += ''.join(text)
                    full_transcript += ''.join('.')
                except:
                    print('Sorry.. run again...')
            
    print('transcript is:')        
    print(full_transcript) 
    translator =Translator()
    
    
    ch=translator.translate(full_transcript, src='en',dest='hi')
    m=ch.text
    print(m)
    q=translator.translate(m,dest='en')
    trans=q.text 
    input_tensor = tokenizer.encode(trans, return_tensors="pt", max_length=512)
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
    # summarization = pipeline('summarization')
    # summarized_text = summarization(full_transcript)
    # summary=summarized_text[0]['summary_text']
    print('summary is \n')
    print(text2)
    return p
# link=input('link')
# link='https://www.youtube.com/watch?v=hWLf6JFbZoo'
# #downloadvideo(link)
# startConvertion()