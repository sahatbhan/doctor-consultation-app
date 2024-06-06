from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import pywhatkit
from datetime import datetime


def send(request):
    currentDateAndTime = datetime.now()
    hour = currentDateAndTime.hour
    minute = currentDateAndTime.minute + 1
    doc_name = "Sarthak"
    number = '+918492010352'
    message = "Your meeting has been scheduled with Dr. " + doc_name
    pywhatkit.sendwhatmsg_instantly(number, message)

    return HttpResponse("Done")