import time
import pymongo
from app.api import API

# from app.api import API

# Type 1 or 2 based on -------College 🏤 view categories....
# 1. Engineering 🦺
# 2. Science 💻️
# 3. MBBS ⛑️
# 4. Mass Communication 📚️
# 5. Commerce 📃
# 6. Architecture 💹💰️
# 7. MBA 📈📊
# 8. Law 💰️

client = pymongo.MongoClient("mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
mydb = client["pragati"]

mycol1 = mydb["engineering colleges"]
mycol2 = mydb["science"]
mycol3 = mydb["mbbs"]
mycol4 = mydb["mass_media"]
mycol5 = mydb["BCom"]
mycol6 = mydb["Architecture"]
mycol7 = mydb["mba"]
mycol8 = mydb["law"]

filcol1 = mycol1.find()
filcol2 = mycol2.find()
filcol3 = mycol3.find()
filcol4 = mycol4.find()
filcol5 = mycol5.find()
filcol6 = mycol6.find()
filcol7 = mycol7.find()
filcol8 = mycol8.find()



# api = API('fdkhljkaldhfjasdjkfljdsa','916361276796')


def engineer(api:API):
    i=0
    for z in filcol1 :
        if(i<5):
            api.college_display2("app/images/pragati.png",z['college_name'],z['exam'],z['eligibility'],z['college_nirf'])
            i=i+1
        else:
            break
    time.sleep(5)
    api.template_other_services()
    del api
    return    

def science(api:API):
    i=0
    for z in filcol2 :
        if(i<5):
            api.college_display2("app/images/collegephoto.png",z['college_name'],z['exams1'],z['eligibility1'],z['rank1'])
            i=i+1
        else:
            break
    time.sleep(5)
    api.template_other_services()
    del api
    return    
# science(api)

def mbbs(api:API):
    i=0
    for z in filcol3 :
        if(i<5):
            api.college_display2("app/images/bacha.jpg",z['college_name'],z['exam'],z['eligibility'],z['ranking'])
            i=i+1
        else:
            break    
    time.sleep(5)
    api.template_other_services()
    del api
    return 
# mbbs(api)

def massMedia(api:API):
    i=0
    for z in filcol4 :
        if(i<5):
            api.college_display2("app/images/pragati.png",z['college_name'],z['fees'],z['college_rating'],z['rank'])
            i=i+1
        else:
            break 
    time.sleep(5)
    api.template_other_services()
    del api
    return

def bcom(api:API):
    i=0
    for z in filcol5 :
        if(i<5):
            api.college_display2("app/images/collegephoto.png",z['college_name'],z['fees'],z['college_rating'],z['rank'])
            i=i+1
        else:
            break 
    time.sleep(5)
    api.template_other_services() 
    del api   
    return
# bcom(api)

def architecture(api:API):
    i=0
    for z in filcol6 :
        if(i<5):
            api.college_display2("app/images/bacha.jpg",z['college_name'],z['fees'],z['college_rating'],z['rank'])
            i=i+1
        else:
            break
    time.sleep(5)
    api.template_other_services()  
    del api  
    return 

# architecture(api)

def mba(api:API):
    i=0
    for z in filcol7 :
        if(i<5):
            api.college_display2("app/images/pragati.png",z['collegeName'],z['collegeDesc'][:15]+"...",z['adminProcess'][:15]+"...",f"{i+1} Rank")
            i=i+1
        else:
            break
    time.sleep(5)
    api.template_other_services()    
    del api
    return  
    
# mba(api)


def law(api:API):
    i=0
    for z in filcol8 :
        if(i<5):
            api.college_display2("app/images/collegephoto.png",z['college_name'],z['fees'],z['college_rating'],z['rank'])
            i=i+1
        else:
            break
    time.sleep(5)
    api.template_other_services() 
    del api   
    return

# for z in filcol7:
#     print(z['collegeName'],z['collegeDesc'],z['adminProcess'],f"Rank")
# massMedia(api)
# law(api)
# engineer(api)
# mba(api)

# Job Template
# api.job_display("app/images/jobs.jpg","DevOps Engineer","Airtel","Bengaluru","youtube.com")