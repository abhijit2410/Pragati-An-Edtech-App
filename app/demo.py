# import requests
# class API:
#     url = "https://iqwhatsapp.airtel.in/gateway/airtel-xchange/basic/whatsapp-manager/v1/session/send/"
#     template_url = "https://iqwhatsapp.airtel.in/gateway/airtel-xchange/basic/whatsapp-manager/v1/template/send"
#     headers ={
#         'Authorization': 'Basic QUlSVEVMX0RJR19pdzFzRGJLOWdMZGN1ak5VejVmZzoxeipMVTZLTjxrenNMPytiVzQ2'
#     }
#     waba_number = "918904587744"
#     businessId = 'Hackathon3_8904587744'

#     def __init__(self,sessionID,userNumber) -> None:
#         self.sessionID = sessionID
#         self.userNumber = userNumber

#     def send_user(self, url, data):
#         response = requests.request("POST", url, headers= self.headers, json=data)

#     def send_text(self,msg):
#         new_url = self.url + 'text'

#         data = {
#             "sessionId": self.sessionID,
#             "to": self.userNumber,
#             "from": self.waba_number,
#             "message": {
#             "text" : msg
#             }
#         }

#         self.send_user(new_url,data)

# api = API('fasdjkfhajdadsfjkads','916361276796')
# api.send_text("Hi Harshith")
# del api
# api = API('fasdjkfhajdladsfjkladsdfjkalkads','916361276796')
# api.send_text("Detroyed")

# from datetime import datetime
# from time import gmtime, strftime

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# print("Your Time Zone is GMT", strftime("%z", gmtime()))

# from final_new_updated_model import prediction
# from api import API

# api = API("jadshfjakdsfjewehf","919538533738")

# print(prediction(["finance",]))