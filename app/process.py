from . import intentClassifier, subject_based_prediction,topcollege,db
from app.api import API
import requests
from app.db import check
import time


def process(r):
    print(r)
    api = API(r['sessionId'],r['from'])
    if (r['message']['type'] == 'text'):
        '''Text message'''
        if check('flow') == 'EMPTY' and (r['message']['text']['body'] == "1" or (r['message']['text']['body']).lower() == "pcm"):
            res = (r['message']['text']['body']).lower()
            subject_based_prediction.subject(res,api)
            return "null"

        elif check('flow') == 'EMPTY' and (r['message']['text']['body'] == "2" or (r['message']['text']['body']).lower() == "pcb"):
            res = (r['message']['text']['body']).lower()
            subject_based_prediction.subject(res,api)
            return "null"

        elif check('flow') == 'EMPTY' and (r['message']['text']['body'] == "3" or (r['message']['text']['body']).lower() == "pcmb"):
            res = (r['message']['text']['body']).lower()
            subject_based_prediction.subject(res,api)
            return "null"

        elif check('flow') == 'EMPTY' and (r['message']['text']['body'] == "4" or (r['message']['text']['body']).lower() == "commerce"):
            res = (r['message']['text']['body']).lower()
            subject_based_prediction.subject(res,api)
            return "null"

        elif check('flow') == 'EMPTY' and (r['message']['text']['body'] == "5" or (r['message']['text']['body']).lower() == "arts"):
            res = (r['message']['text']['body']).lower()
            subject_based_prediction.subject(res,api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "a" or (r['message']['text']['body']).lower() == "engineering"):
            topcollege.engineer(api)
            return "null"
        
        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "b" or (r['message']['text']['body']).lower() == "science"):
            topcollege.science(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "c" or (r['message']['text']['body']).lower() == "mbbs"):
            topcollege.mbbs(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "d" or (r['message']['text']['body']).lower() == "mass communication"):
            topcollege.massMedia(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "e" or (r['message']['text']['body']).lower() == "commerce"):
            topcollege.bcom(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "f" or (r['message']['text']['body']).lower() == "architecture"):
            topcollege.architecture(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "g" or (r['message']['text']['body']).lower() == "mba"):
            topcollege.mba(api)
            return "null"

        elif check('flow') == 'EMPTY' and ((r['message']['text']['body']).lower() == "h" or (r['message']['text']['body']).lower() == "law"):
            topcollege.law(api)
            return "null"
        else:
            resp = intentClassifier.search(r['message']['text']['body'],r['to'],r['from'],r['sessionId'])
            return {"response": resp}

    elif(r['message']['type'] == 'button'):
        print('''Button Reply''')
        api = API(r['sessionId'],r['from'])
        
        if r['message']['button']['text'] == 'Student':
            print("Student")
            api.send_text('Please fill this form👇')
            time.sleep(1)
            api.send_text('https://docs.google.com/forms/d/e/1FAIpQLSe1cPqpRhrqihrEAxfrw5ciPQZ9EAXDe3vKt7uf6SaROHNGAQ/viewform?usp=sf_link')
            time.sleep(7)
            api.template_student_option_buttons()
            del api
            return "null"

        elif r['message']['button']['text'] == 'Graduate':
            print("Graduate")
            api.send_text('Please fill this form👇')
            time.sleep(1)
            api.send_text('https://docs.google.com/forms/d/e/1FAIpQLSe1cPqpRhrqihrEAxfrw5ciPQZ9EAXDe3vKt7uf6SaROHNGAQ/viewform?usp=sf_link')
            time.sleep(7)
            del api
            intentClassifier.search("Looking for Job",r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == 'Looking for Job':
            print("Job")
            api.send_text('Please fill this form👇')
            time.sleep(1)
            api.send_text('https://docs.google.com/forms/d/e/1FAIpQLSe1cPqpRhrqihrEAxfrw5ciPQZ9EAXDe3vKt7uf6SaROHNGAQ/viewform?usp=sf_link')
            time.sleep(7)
            del api
            intentClassifier.search(r['message']['button']['text'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == 'Full Time':
            print("Full Time")
            intentClassifier.search(r['message']['button']['text'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == 'Part Time':
            print("Part Time")
            intentClassifier.search(r['message']['button']['text'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == 'Contract':
            print("Contractor")
            intentClassifier.search(r['message']['button']['text'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == 'CR':
            intentClassifier.search("Career Recommendation",r['to'],r['from'],r['sessionId'])
            return "null"
        
        elif r['message']['button']['text'] == 'VTC':
            api.template_college_catergory()
            del api
            return "null"
        
        elif r['message']['button']['text'] == 'SB':
            api.template_subject_choice_for_recommendation()
            del api
            return "null"

        elif r['message']['button']['text'] == 'Education News':
            api.template_education_new()
            del api
            return "null"
        
        elif r['message']['button']['text'] == 'Research Papers':
            api.template_research_paper()
            del api
            return "null"

        elif r['message']['button']['text'] == 'Yes, I am satisfied.':
            db.update_feedback('Yes, I am satisfied.')
            return "null"

        elif r['message']['button']['text'] == 'No, Could be better.':
            db.update_feedback('No, Could be better.')
            return "null"
        elif r['message']['button']['text'] == "1":
            intentClassifier.search(r['message']['button']['payload'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == "2":
            intentClassifier.search(r['message']['button']['payload'],r['to'],r['from'],r['sessionId'])
            return "null"

        elif r['message']['button']['text'] == "3":
            intentClassifier.search(r['message']['button']['payload'],r['to'],r['from'],r['sessionId'])
            return "null"
        else:
            pass
    # elif(r['type'] == 'list'):
    #     '''List Reply''' 