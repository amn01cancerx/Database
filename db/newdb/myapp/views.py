from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from datetime import datetime, timedelta
import requests
from django.http import HttpResponse
import datetime

# from .serializers import *
from rest_framework.renderers import JSONRenderer
from datetime import datetime, timedelta
from datetime import date
import time
import json
import pytz

# use this for Lab Booking flow
class LabApi(APIView):
    def post(self,request):
        data = request.data
        print(data)
        return Response(data)

# Use this for Buy Medicine Flow
class BuyMedicine(APIView):
    def post(self, request):
        data = request.data
        print(data)
        return Response(data)

# Use this for Book Appointment flow
class BookApt(APIView):
    def post(self, request):
        data = request.data
        print(data)
        return Response(data)

# Use this for Miss Lab test slots details
class MissLab(APIView):
    def post(self,request):
        data = request.data
        return Response(data)

# Use this for Miss deliver medicine slots details
class MissMed(APIView):
    def post(self,request):
        data = request.data
        print(data)
        return Response(data)

class CheckIntoArray(APIView):
    def post(self,request):
        data = request.data
        print(data)
        return Response(data)


# This is use for English(Main) flow
# class MyApi(APIView):
#     def post(self,request):
#         data = request.data
#         dr_num = data['test_data']
#         print(dr_num)
#         if "+" in dr_num:
#             f= requests.Session()
#             wati_auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmQ0NDkxYS1kNTFjLTQ2ZWItYWUwZS0wN2UxZWIzMzg1OTMiLCJ1bmlxdWVfbmFtZSI6Im1hbkBjYW5jZXJ4LmluIiwibmFtZWlkIjoibWFuQGNhbmNlcnguaW4iLCJlbWFpbCI6Im1hbkBjYW5jZXJ4LmluIiwiYXV0aF90aW1lIjoiMTIvMTIvMjAyMiAwNTozMDo1NSIsImRiX25hbWUiOiI4OTUyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZHtF1G8ap1MVn7Si1_EVM4pf4p1PAs-CGjhwGKjAqlg"
#             wati_endpoint = "https://live-server-8952.wati.io/api/v1/sendSessionMessage/919319073110?messageText=Correct format thankyou"
#             headers = {
#             'method' : 'post',
#             'Content-type' : 'application/json',
#             'Authorization': wati_auth_token,
#             }
#             send_message = f.post(wati_endpoint, headers=headers, verify=False)
#             print("true")
#             return Response(data)
#         else:
#             f= requests.Session()
#             wati_auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmQ0NDkxYS1kNTFjLTQ2ZWItYWUwZS0wN2UxZWIzMzg1OTMiLCJ1bmlxdWVfbmFtZSI6Im1hbkBjYW5jZXJ4LmluIiwibmFtZWlkIjoibWFuQGNhbmNlcnguaW4iLCJlbWFpbCI6Im1hbkBjYW5jZXJ4LmluIiwiYXV0aF90aW1lIjoiMTIvMTIvMjAyMiAwNTozMDo1NSIsImRiX25hbWUiOiI4OTUyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZHtF1G8ap1MVn7Si1_EVM4pf4p1PAs-CGjhwGKjAqlg"
#             wati_endpoint = "https://live-server-8952.wati.io/api/v1/sendSessionMessage/919319073110?messageText=Please enter the number in correct format"
#             headers = {
#             'method' : 'post',
#             'Content-type' : 'application/json',
#             'Authorization': wati_auth_token,
#             }
#             send_message = f.post(wati_endpoint, headers=headers, verify=False)
#             print("False")


class MyApi(APIView):
    def post(self,request):

        data = request.data
        print(data)
        new = json.loads(list(data.keys())[0])
        print(new)
        for i in new:
            # time1, time2, time3 = i['med_time1'], i['med_time2'], i['med_time3']
            all_time = i['med_time1'], i['med_time2'], i['med_time3']
            all_days = i['days1'], i['days2'], i['days3']

            print(all_days, "this is days........................")
            # print(time1, time2, time3)
            print(all_time)
            phone_number = i['phone']
            name = i['user_name']
            print(phone_number)
            
            ist = pytz.timezone('Asia/Kolkata')
            currentDateAndTime = datetime.now(tz=ist)

            today_day = currentDateAndTime.strftime("%a")
            print(today_day,"this is today date")
            
            # print("The current date and time is", currentDateAndTime)
            # currentTime = currentDateAndTime.strftime("%H:%M:%S")
            # print("The current time is", currentTime)
            
            # print(datetime.now(ist).time()., "this is current time")
            check_time = ['{{med_time2}}', '{{med_time3}}']
            check_days = ['{{days2}}', '{{days3}}']
            
            for index, time_ in enumerate(all_time):
                send_reminder = False
                days_ = all_days[index]
                if days_ == "Everyday":
                    send_reminder = True
                else:
                    new = days_.split()
                    print(new, "This is new day")
                    final_list = [x.title().replace('day', '') for x in new]
                    print(final_list,"This is final list")
                    if today_day in final_list:
                        send_reminder = True
                    #     # pass
                    # else:
                    #     continue

                    # elif len(days_) != 13 or 16:
                print(send_reminder)
                if time_ not in check_time and days_ not in check_days:
                    med_time_string = time_.lower().replace(':', '').replace(' ', '')
                    # if 'ist' not in med_time_string:
                        # med_time_string += ' +0530'
                    if ('am' in med_time_string) or ('pm' in med_time_string):
                        # import pdb; pdb.set_trace()
                        med_time_only = datetime.strptime(med_time_string, '%I%M%p').time()
                        med_time = datetime.combine(datetime.now().date(), med_time_only)
                        med_time = ist.localize(med_time)
                        
                    else:
                        med_time_only = datetime.strptime(med_time_string, '%H%M').time()
                        med_time = datetime.combine(datetime.now().date(), med_time_only)
                        med_time = ist.localize(med_time)

                    print(med_time)

                    time_diff = (med_time - currentDateAndTime).total_seconds()
                    print(currentDateAndTime)
                    print(time_diff)
                    if (time_diff <= (5*60)) and (time_diff >= -60):
                        if send_reminder:
# ----------------------------------------This part is basically use for sending the templates -------------------------------------------------
                            f = requests.Session()   
                            wati_auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmQ0NDkxYS1kNTFjLTQ2ZWItYWUwZS0wN2UxZWIzMzg1OTMiLCJ1bmlxdWVfbmFtZSI6Im1hbkBjYW5jZXJ4LmluIiwibmFtZWlkIjoibWFuQGNhbmNlcnguaW4iLCJlbWFpbCI6Im1hbkBjYW5jZXJ4LmluIiwiYXV0aF90aW1lIjoiMTIvMTIvMjAyMiAwNTozMDo1NSIsImRiX25hbWUiOiI4OTUyIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.ZHtF1G8ap1MVn7Si1_EVM4pf4p1PAs-CGjhwGKjAqlg"
                            wati_endpoint = "https://live-server-8952.wati.io/api/v1/sendTemplateMessage?whatsappNumber="+ phone_number
                            
                            payload = json.dumps({
                                "template_name": "med_reminder",
                                "broadcast_name" : "med_reminder",
                                "parameters" : [
                                            {
                                            "name" : "c_name",
                                            "value": name
                                    }
                                    ]
                                })


                            headers = {
                                'method' : 'post',
                                'Content-type' : 'application/json',
                                'Authorization': wati_auth_token,
                
                            }
                            send_message = f.post(wati_endpoint, data = payload, headers=headers, verify=False)
                            print("message send")
# -------------------------------------------------------------------------------------------                            
        s = "this is the response"
        return Response(s)