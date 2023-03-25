import requests 
import time
import hmac
import hashlib 
import base64

class API():
    url = "https://iqwhatsapp.airtel.in/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/"
    template_url = "https://iqwhatsapp.airtel.in/gateway/airtel-xchange/basic/whatsapp-manager/v1/template/send"
    headers ={
        'Authorization': 'Basic QUlSVEVMX0RJR19pdzFzRGJLOWdMZGN1ak5VejVmZzoxeipMVTZLTjxrenNMPytiVzQ2'
    }
    waba_number = "918904587744"
    businessId = 'Hackathon3_8904587744'

    def __init__(self,sessionID,userNumber) -> None:
        self.sessionID = sessionID
        self.userNumber = userNumber

    def send_user(self, url, data):
        response = requests.request("POST", url, headers= self.headers, json=data)

    def send_text(self,msg):
        new_url = self.url + 'text'

        data = {
            "sessionId": self.sessionID,
            "to": self.userNumber,
            "from": self.waba_number,
            "message": {
            "text" : msg
            }
        }

        self.send_user(new_url,data)

    def send_media(self,path,caption):

        new_url = self.url + 'media'

        if '.pdf' in path:
            type = 'DOCUMENT'
        else:
            type = 'IMAGE'

        id = self.upload_media(type,path)

        data = {
            "sessionId": self.sessionID,
            "to": self.userNumber,
            "from": self.waba_number,
            "mediaAttachment": {
                "type": type,
                "id": id['mediaId'],
                "caption": caption
                }
        }

        self.send_user(new_url,data)

    def send_button(self,msg:str,button:list):
        new_url = self.url + 'interactive/buttons'
        buttons = []

        for i in button:
            buttons.append({"tag":i,"title":i})

        data = {
            "sessionId": self.sessionID,
            "to": self.userNumber,
            "from": self.waba_number,
            "message": {
                "text": msg
            },
            "buttons": buttons
        }

        self.send_user(new_url,data)

    def send_list(self,):
        new_url = self.url + 'interactive/list'

        data = {
            "sessionId" : "dfkaldnfklnadkfaklnfklda",
            "to":"919538533738",
            "from":"918904587744",
            "message": {
                "text": "List"
            },
            "list": {
            "heading": "Select Store",
            "options": [
                {
                    "tag": "Skill1",
                    "title": "Skill1",
                    "description":"Description about Skill1"
                },
                {
                    "tag": "Skill2",
                    "title": "Skill2",
                    "description":"Description about Skill2"
                },
                {
                    "tag": "Skill3",
                    "title": "Skill3",
                    "description":"Description about Skill3"
                },
                {
                    "tag": "Skill4",
                    "title": "Skill4",
                    "description":"Description about Skill4"
                }
            ]
        }
        }
        self.send_user(new_url,data)

    def template_welcome(self):
    
        data = {
            "templateId": "9a6b3fa0-e2c7-455d-9816-183e4200a453",
            "to": self.userNumber,
            "from": self.waba_number,
        "mediaAttachment": {
            "type": "IMAGE",
            "id" : "872930854159427"
        },
        "message": {
            "payload": [
                "Student",
                "Graduate",
                "Looking for Job"
            ]
        }
        }
        self.send_user(self.template_url,data)

    def template_student_option_buttons(self):
        data = {
            "templateId": "37ca44bf-da5f-4639-9b21-721a8ee48f99",
            "to": self.userNumber,
            "from": self.waba_number,
            "message": {
            "payload": [
                "CR",
                "SB",
                "VTC"
            ]
            }
        }
        self.send_user(self.template_url,data)

    def template_related_searches(self, answer):
            data = {
            "templateId": "dc882971-91ef-40c6-9320-d1fde949adb6",
            "to": self.userNumber,
            "from": self.waba_number,
            "message": {
                "variables":[
                answer[1],
                answer[2],
                answer[3]],
            "payload": [
                answer[1],
                answer[2],
                answer[3]
            ]
            }
            }
            self.send_user(self.template_url,data)   

    def template_college_notify(self):
        data = {
        "templateId": "46232394-cb4c-44a8-aba5-376bd1952c8a",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
        "payload": [
                "Yes",
                "No"
            ]
        }
        }
        self.send_user(self.template_url,data)

    def template_tutor_list(self):

        data = {
            "templateId": "13706cff-e0ac-4e3b-8d38-c3580b5060bf",
            "to": "919538533738",
            "from": "918904587744"
        }
        self.send_user(self.template_url,data)

    def template_other_services(self):
        data = {
        "templateId": "f033dffa-c38e-47be-8264-5a6bab2ae17e",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "payload": [
                "Education News",
                "Research Papers"
            ]
        }
        }
        self.send_user(self.template_url,data)
        
    def template_information(self,img_path,query,answer):

        id = self.upload_media('IMAGE',img_path)
        data = {
        "templateId": "b2f7274e-72c3-4b16-bd57-c8fd55ef3705",
        "to": self.userNumber,
        "from": self.waba_number,
        "mediaAttachment": {
                "type": "IMAGE",
            "id" : id['mediaId']
        },
        "message": {
            "variables": [
                query,
                answer[4],
                answer[1],
                answer[2],
                answer[3]
            ],
        "payload": [
                answer[1],
                answer[2],
                answer[3]
        ]
        }
        } 
        self.send_user(self.template_url,data)  

    def template_college_catergory(self):
        data = {
        "templateId": "c7d5df67-c6f9-4dda-8a52-13c41ae928b4",
        "to": self.userNumber,
        "from": self.waba_number
        }
        self.send_user(self.template_url,data)

    def template_related_search(self,answer):
        data = {
        "templateId": "42fa2f9a-06c0-4ea6-a99e-afbf0e6e1864",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "variables": [
                answer[0],answer[1],answer[3]
            ]
        }
        }
        self.send_user(self.waba_number,data)

    def template_queries(self,query1,query2,answer):
        data = {
        "templateId": "9d115772-54d2-4b54-a3da-2e592a9d206a",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "variables": [
                query1,
                query2,
                answer[1],
                answer[2],
                answer[3],
            ],
        "payload": [
                answer[1],
                answer[2],
                answer[3]
        ]
        }
        } 
        self.send_user(self.template_url,data)  


    def template_tutor_service(self):
        data = {
        "templateId": "4414a803-dac8-4999-a93e-648426bdc024",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "payload": [
                "Yes, would love it",
                "No"
            ]
        }
        }
        self.send_user(self.template_url,data)

    def template_job_type(self):
        data = {
        "templateId": "3612f391-918e-48f6-937b-eb132a397f92",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "payload": [
                "Fulltime",
                "Part Time",
                "Contract"
            ]
        }
        }
        self.send_user(self.template_url,data)

    def template_see_career_path(self):
        data = {
        "templateId": "fd0d88b6-23aa-4513-9e29-5b0795868afd",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
            "payload": [
                "Based on my skills",
                "Top career paths"
            ]
        }
        }
        self.send_user(self.template_url,data)

    def template_waiting_time(self):
        data = {
        "templateId": "f0feb296-d523-4e51-8369-3ca43c210588",
        "to": self.userNumber,
        "from": self.waba_number
        }
        self.send_user(self.template_url,data)

    def template_tutor_list(self):
        data = {
        "templateId": "13706cff-e0ac-4e3b-8d38-c3580b5060bf",
        "to": self.userNumber,
        "from": self.waba_number
        }
        self.send_user(self.template_url,data)

    def template_subject_choice_for_recommendation(self):
        data = {
        "templateId": "72b233b5-0327-48db-9098-4dda75d851cd",
        "to": self.userNumber,
        "from": self.waba_number
        }
        self.send_user(self.template_url,data)

    def template_courses_new(self,img_path,title,suffix):
        id = self.upload_media('IMAGE',img_path)
        new_suffix = "search?query=" + suffix.replace(" ","+")
        # print(new_suffix)
        # print(id)
        data = {
        "templateId": "09a99413-78d4-497a-a89d-9552787e6321",
        "to": self.userNumber,
        "from": self.waba_number,
        "mediaAttachment": {
            "type": "IMAGE",
            "id" : "555820266388291"
        },
        "message": {
            "variables": [
                title
            ],
            "payload" :[
            "view courses"
        ],
        "suffix": new_suffix
        }
        }
        self.send_user(self.template_url,data)

    def template_feedback(self):
        data = {
        "templateId": "cd3dcc9c-e814-4ba9-9791-8d1920b72985",
        "to": self.userNumber,
        "from": self.waba_number,
        "message": {
        "payload": [
            "Yes, I am Satisfied.",
            "No, Could do better."
        ]
        }
        }
        self.send_user(self.template_url,data)
        

    # def college_display(self,img_path,name,exam,eligible,rank):
    #     id = self.upload_media('IMAGE',img_path)
    #     # print(id['mediaId'])
    #     data = {
    #     "templateId": "623c6aee-8484-4852-bac1-ef7c87b98fca",
    #     "to": self.userNumber,
    #     "from": self.waba_number,
    #     "mediaAttachment": {
    #         "type": "IMAGE",
    #         "id" : id['mediaId']
    #     },
    #     "message": {
    #         "variables": [
    #             name,
    #             exam,
    #             eligible,
    #             rank
    #         ]
    #     },
    #     }
    #     self.send_user(self.template_url,data)

    def college_display2(self,img_path,name,fees,rating,rank):
        id = self.upload_media('IMAGE',img_path)
        # print(id['mediaId'])
        data = {
        "templateId": "86b0c990-1eed-41e1-a312-409773c03337",
        "to": self.userNumber,
        "from": self.waba_number,
        "mediaAttachment": {
            "type": "IMAGE",
            "id" : "567461261856337"
        },
        "message": {
            "variables": [
                name,
                fees,
                rating,
                rank
            ]
        },
        }
        self.send_user(self.template_url,data) 

    def job_display(self,img_path,name,company,loc,link):
        id = self.upload_media('IMAGE',img_path)
        # print(id['mediaId'])
        data = {
        "templateId": "6c706987-0c8e-4ecb-bd9a-5e5cf9496af1",
        "to": self.userNumber,
        "from": self.waba_number,
        "mediaAttachment": {
            "type": "IMAGE",
            "id" : "692688279015993"
        },
        "message": {
            "variables": [
                name,
                company,
                loc,
                link
            ]
        },
        }
        self.send_user(self.template_url,data)    

    def template_education_new(self):
        data = {
        "templateId": "5e79d89e-677e-4f3c-a77a-00bb1b1a52d6",
        "to": self.userNumber,
        "from": self.waba_number,
        }  
        self.send_user(self.template_url,data)  

    def template_research_paper(self):
        data = {
        "templateId": "adb7ed2e-d353-4c8c-9fe7-4200f380bf7d",
        "to": self.userNumber,
        "from": self.waba_number,
        }  
        self.send_user(self.template_url,data)  

    def upload_media(self,type,path):
        url = "https://iqwhatsapp.airtel.in:443/gateway/airtel-xchange/whatsapp-manager/v1/media"
        data={'type': type,
        'businessId': 'Hackathon3_8904587744'}
        # print(path.split('/')[-1])
        files=[
        ('file',(path.split('/')[-1],open(path,'rb'),'image/jpeg'))
        ]
        # print(files)
        date = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.gmtime())
        # print(date)
        stringToSign = f'X-Date: {date}'
        username= 'WA_PROD_TEST_2'
        secret= 'airtel@#testing'
        signature =  base64.b64encode(hmac.new(secret.encode('utf-8'), stringToSign.encode('utf-8'),hashlib.sha256).digest())
        hmacAuth = 'hmac username="' + str(username) + '", algorithm="hmac-sha256", headers="X-Date", signature="' + signature.decode() + '"'
        # print(hmacAuth)
        headers = {
        'X-Correlation-ID': 'abcd',
        'X-Date': date,
        'Authorization': hmacAuth,
        'X-Consumer-Username': 'AIRTEL_DIG_iw1sDbK9gLdcujNUz5fg'
        }   

        resID = requests.request("POST",url,headers=headers,data=data,files=files)
        id  = resID.json()
        return id


# api = API('fdkhljkaldhfjasdjkfljdsa','916361276796')
# api.send_text('adfja\nfjdfjads\nhfas')
# api.template_education_new()
# api.template_research_paper()

