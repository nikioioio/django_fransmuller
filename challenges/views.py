from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

month_list = {
    "january":"Eat no meat for the entire month",
    "february":"Walk for at least 20 minutes every day",
}

def monthly_challange(request,month):

    try:
        challenge_text = month_list[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")



def monthly_challenge_by_number(request,month):
    # month-=1
    months = list(month_list.keys())

    if month > len(months) or month==0:
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month-1]
    # функция reverse
    redirect_path = reverse('month_challenge',args=[redirect_month])
    print(redirect_path)
    return HttpResponseRedirect("/challenges/"+redirect_month)
