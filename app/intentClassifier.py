import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from keras import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Input
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
import time

from app.api import API 
from app.universalScraper import scrape_text
from app.pdfScraper import pdf_search
from app.videoScraper import scrape_video
from app.db import userauth, check, update
from app.career_prediction_final import growthRate
from app.job_scrape import job_seek


stop_words = stopwords.words('english')

def clean_corpus(corpus):
  corpus = [ doc.lower() for doc in corpus]
  cleaned_corpus = []
  
  stop_words = stopwords.words('english')
  wordnet_lemmatizer = WordNetLemmatizer()

  for doc in corpus:
    tokens = word_tokenize(doc)
    cleaned_sentence = [] 
    for token in tokens: 
      if token not in stop_words and token.isalpha(): 
        cleaned_sentence.append(wordnet_lemmatizer.lemmatize(token)) 
    cleaned_corpus.append(' '.join(cleaned_sentence))
  return cleaned_corpus

with open('app/intents.json', 'r',encoding='utf-8') as file:
  intents = json.load(file)

corpus = []
tags = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

cleaned_corpus = clean_corpus(corpus)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_corpus)
encoder = OneHotEncoder()
y = encoder.fit_transform(np.array(tags).reshape(-1,1))
model = Sequential([
                    Input((X.shape[1],)),
                    Dense(150,activation='relu'),
                    Dropout(0.2),
                    Dense(75, activation='relu'),
                    Dropout(0.2),
                    Dense(y.shape[1], activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
print(f"Model input: {model.input_shape}")

# history = model.fit(X.toarray(), y.toarray(), epochs=22, batch_size=1)
# model.save('app/chatbot.hdf5')

model = load_model('app/chatbot.hdf5')

INTENT_NOT_FOUND_THRESHOLD = 0.93

def predict_intent_tag(message):
  message = clean_corpus([message])
  X_test = vectorizer.transform(message)
  
  y = model.predict(X_test.toarray()) 

  if y.max() < INTENT_NOT_FOUND_THRESHOLD:
    return 'noanswer'
  
  prediction = np.zeros_like(y[0])
  prediction[y.argmax()] = 1
  tag = encoder.inverse_transform([prediction])[0][0]
  return tag

def get_intent(tag):
  
  for intent in intents['intents']:
    if intent['tag'] == tag:
      return intent


job_lst = []
rand = ['🤖Bot is thinking...', 'Hang on tight⌛', 'Gathering best results for you...🔍']
def search(query,bot_num,to_num,sessionID):

  tag = predict_intent_tag(query)
  intent = get_intent(tag)
  api  = API(sessionID,to_num)

  if intent != None and intent['tag'] == 'greeting' and check('flow') == 'EMPTY':
    db_check = userauth(to_num)
    if db_check == 'new User':
      api.template_welcome()
      # api.template_other_services()
      # api.send_text('We are all set👍')
      del api
      return "null"
    else:
      response = random.choice(intent['responses'])
      api.send_text(response)
      del api
      return "null"

  elif check('flow') == 'career' or (intent != None and intent['tag'] == 'career'):
    if(check('num') == -1):
        # update from EMPTY to career in db
        update('flow', 'EMPTY', 'career')
        update('num', -1, 1)
        # send list
        api.send_text('Please refer the below website to get an insight of all the skills👇')
        time.sleep(1)
        api.send_text('https://marcresi.github.io/CareerList/')
        time.sleep(1)
        api.send_text('Enter your skills:')
        # lst = ['career', 'Please refer the below website to get an insight of all the skills👇', 'https://marcresi.github.io/CareerList/', 'Enter you skills:']
        del api
        return "null"
    else:
        career_lst = growthRate(query,api)
        # update in db
        if type(career_lst) == list:
          update('flow', 'career', 'EMPTY')
          update('num', 1, -1)
          api.send_text(f'{career_lst[0]}')
          time.sleep(1)
          concat = ""
          for i in career_lst[1]:
            concat += '▸ ' + i + '\n'
          api.send_text(concat)
          time.sleep(1)
          api.send_media(career_lst[2],'Growth Rate of the top career paths recommended for')
          time.sleep(3)
          api.template_other_services()
        if career_lst == "NOT FOUND":
          update('flow', 'career', 'EMPTY')
          update('num', 1, -1)
        del api
        return "null"
    

  elif check('flow') == 'job' or (intent != None and intent['tag'] == 'job'):

    if(check('num') == -1):
        # update from EMPTY to job in db
        update('flow', 'EMPTY', 'job')
        update('num', -1, 1)
        api.send_text('Enter job:')
        del api
        return "null"

    elif (check('num') == 1):
        job_lst.append(query)
        update('num', 1, 2)
        api.send_text('Enter location:')
        del api
        return "null"

    elif (check('num') == 2):
        job_lst.append(query)
        update('num', 2, 3)
        api.template_job_type()
        del api
        return "null"

    elif (check('num') == 3):
        job_lst.append(query)
        api.send_text(random.choice(rand))
        job_res = job_seek(job_lst)
        print(job_res)
        job_lst.clear()
        # update in db
        update('flow', 'job', 'EMPTY')
        update('num', 3, -1)
        if job_res != None:
          for i in range(0,4):
            api.job_display('app/images/jobs.jpg',job_res[i]['job_name'],job_res[i]['company_name'],job_res[i]['location'],job_res[i]['link'])
        else:
          api.send_text("Sorry, Pragati couldn't find jobs for you 😔")
        time.sleep(7)
        api.template_other_services()
        del api
        return "null"
  
        
  elif intent != None and (intent['tag'] == 'goodbye' or intent['tag'] == 'thanks'):
    response = random.choice(intent['responses'])
    api.send_text(response)
    time.sleep(1)
    api.template_feedback()
    del api
    return "null"

  elif intent != None and intent['tag'] == 'college':
    api.template_college_catergory()
    del api
    return "null"

  elif intent != None and intent['tag'] == 'subject':
    api.template_subject_choice_for_recommendation()
    del api
    return "null"
  
    
  elif intent != None and intent['tag'] != 'document' and intent['tag'] != 'video':
    response = random.choice(intent['responses'])
    api.send_text(response)
    time.sleep(3)
    api.template_other_services()
    del api
    return "null"

  # api.send_text('🤖Bot is thinking...')

  if intent != None and intent['tag'] == 'document':
    api.send_text(random.choice(rand))
    pdf_res = pdf_search(query)
    for i in range(1,3):
      api.send_text(pdf_res[i])
    del api
    return "null"
  elif intent != None and intent['tag'] == 'video':
    api.send_text(random.choice(rand))
    vid_res = scrape_video(query)
    for i in range(1,len(vid_res)):
      api.send_text(vid_res[i])
    del api 
    return "null"

  api.send_text(random.choice(rand))
  print("Universal Scraping")
  res = scrape_text(query,api)
  # print(res)
  del api
  return res
