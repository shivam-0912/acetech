from django.shortcuts import render,HttpResponse 
from django.http import HttpResponse,JsonResponse
import json       

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.core.mail import send_mail
import random
import math
from acetech.settings import EMAIL_HOST_USER     



def signup(request):
    if request.method=="POST":
        
        try:
            send_mail("Welcome to Winntus", "Hello "+request.POST['name']+",Welcome to Winntus ", EMAIL_HOST_USER,[request.POST['email']])

        except:
            return JsonResponse({'status':'201'})             

    return JsonResponse({'status':'400'})             



