import time
import random
from app.api import API

pcb = ["▸ Bachelor of Medicine and Bachelor of Surgery (MBBS)",
"▸ Bachelor of Dental Surgery",
"▸ Bachelor of Pharmacy",
"▸ Bachelor of Medical Lab Technology",
"▸ Diploma courses in operation theatre technology",
"▸ medical laboratory",
"▸ x-ray technology"]





pcm = ["▸ Bachelor of Technology",
       "▸ Bachelor of Science",
       "▸ BSc Nuclear Medicine Technology",
       "▸ Merchant Navy",
       "▸ Forensic Science",
       "▸ Criminology"]





pcmb = ["▸ Bachelor of Technology",
        "▸ Molecular Biologist",
        "▸ Forensic Science",
        "▸ Biochemical Engineer",
        "▸ Bio-Chemist",
        "▸ Dentist",
        "▸ Doctor"]





com = ["▸ Bachelors in Commerce",
       "▸ Chartered Accountant",
       "▸ Chartered Accountant",
       "▸ Cost Accountant",
       "▸ Bachelor in Business Administration",
       "▸ Bachelors of Economics",
       "▸ Journalism and Mass Communication"]





arts = ["▸ Bachelor of Arts (B.A.)",
"▸ Bachelor of Fine Arts (B.F.A.)",
"▸ Bachelor of Business Administration (B.B.A.)",
"▸ Bachelor of Journalism and Mass Communication (B.J.M.)",
"▸ Bachelor of Fashion Design (B.F.D.)",
"▸ Bachelor of Hotel Management (B.H.M.)"]





def subject(sub,api:API):
    if(sub=='1' or sub=='pcm'):
        concat = ""
        for i in pcm:
          concat += i + '\n'
        api.send_text(concat) 
        j = random.choice(pcm) 
        j = j.replace("▸","")
        time.sleep(3)
        api.template_courses_new('app/images/course.png',j,j)
        time.sleep(3)
        api.template_other_services()
        del api
        return "null"
    elif(sub=='2' or sub=='pcb'):
        concat = ""
        for i in pcb:
          concat += i + '\n'
        api.send_text(concat)  
        j = random.choice(pcb) 
        j = j.replace("▸","")
        time.sleep(3)
        api.template_courses_new('app/images/course.png',j,j)
        time.sleep(3)
        api.template_other_services()
        del api
        return "null"
    elif(sub=='3' or sub=='pcmb'):
        concat = ""
        for i in pcmb:
          concat += i + '\n'
        api.send_text(concat)  
        j = random.choice(pcmb) 
        j = j.replace("▸","")
        time.sleep(3)
        api.template_courses_new('app/images/course.png',j,j)
        time.sleep(3)
        api.template_other_services()
        del api
        return "null"
    elif(sub=='4' or sub=='com'):
        concat = ""
        for i in com:
          concat += i + '\n'
        api.send_text(concat)  
        j = random.choice(com) 
        j = j.replace("▸","")
        time.sleep(3)
        api.template_courses_new('app/images/course.png',j,j)
        time.sleep(3)
        api.template_other_services()
        del api
        return "null"
    elif(sub=='5' or sub=='arts'):
        concat = ""
        for i in arts:
          concat += i + '\n'
        api.send_text(concat) 
        j = random.choice(arts) 
        j = j.replace("▸","")
        time.sleep(3)
        api.template_courses_new('app/images/jobs.jpg',j,j)
        time.sleep(3)
        api.template_other_services()
        del api
        return "null"





# print(subject('pcm'))






