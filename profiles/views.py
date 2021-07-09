from django.http.response import JsonResponse
from django.shortcuts import render
from requests.api import request
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import UsernameForm
import requests
import json
import os

def home(request):
    form = UsernameForm()
    return render(request, 'profiles/home.html', {'form': form})


def joined_date(date):
    months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
              '07': 'July', '08': 'August', '09': 'Saptember', '10': 'Octomber', '11': 'November', '12': 'December'}
    # print(date)
    year = date[:4]
    month = months[date[5:7]]
    day = date[8:10]

    return month+' '+day+', '+year


def get_username(request):

    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = UsernameForm(request.GET)
        # print(form.cleaned_data['username'])
        # check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            headers = {
                "Authorization": os.getenv('GITHUB_ACCESS_TOKEN')
            }
            # To get the User data and store in userdata
            url1 = "https://api.github.com/users/{}".format(
                form.cleaned_data['username'])
            response = requests.get(url1, headers=headers)
            userdata = response.json()

            # print(userdata)
            # print(userdata)
            # If response contains 'message' in it then the username is invalid. Return the error message.
            if 'message' in userdata.keys():
                form = UsernameForm(request.GET)
                note = "I can't find your Octoprofile.😟"
                return render(request, 'profiles/home.html', {'form': form, 'note': note})

            userdata['created_at'] = joined_date(userdata['created_at'])

            # To get the Repositories data and store in repodata
            url2 = "https://api.github.com/users/{}/repos".format(
                form.cleaned_data['username'])
            response = requests.get(url2, headers=headers)
            repodata = response.json()
            # To use repodata in another function
            request.session['repodata'] = repodata

            # Opening JSON file
            data = open('./profiles/static/json/colors.json',)
            # Returns JSON object as a dictionary
            colors = json.load(data)
            # print(colors['Python']['color'])
            data.close()

            return render(request, 'profiles/profile_page.html', {'userdata': userdata, 'repodata': repodata, 'colors': colors})
        
        form = UsernameForm()
        return render(request, 'profiles/home.html', {'form': form})
    # If a GET (or any other method) we'll create a blank form
    form = UsernameForm()
    return render(request, 'profiles/home.html', {'form': form})


def get_repodata(request):
    # Collect the saved data from function get_username()
    repodata = request.session.get('repodata')

    data = open('./profiles/static/json/colors.json')
    # Load json dictionary in colors
    colors = json.load(data)
    data.close()

    # To get Top languages by user
    top_lang = {}
    for item in repodata:
        # print(item['name'], item['language'])
        top_lang[item['language']] = top_lang.get(item['language'], 0) + 1

    sorted_top_lang = list(
        sorted(top_lang.items(), key=lambda item: item[1], reverse=True))
    # sliced the list to get top 5 items
    sorted_top_lang = dict(sorted_top_lang[0:5])
    # change 'null' key to 'Others'
    sorted_top_lang['Others'] = sorted_top_lang.pop(None)
    # print(top_lang)
    # print(sorted_top_lang)

    # To get Most starred repositories
    most_starred = {}
    for item in repodata:
        # print(item['name'], item['stargazers_count'])
        most_starred[item['name']] = item['stargazers_count']
        sorted_most_starred = list(
            sorted(most_starred.items(), key=lambda item: item[1], reverse=True))
        # sliced the list to get top 5 items
        sorted_most_starred = dict(sorted_most_starred[0:5])
        # print(sorted_most_starred)

    # To get stars per languages
    star_per_lang = {}
    for item in repodata:
        star_per_lang[item['language']] = star_per_lang.get(
            item['language'], 0) + item['stargazers_count']
    # print(star_per_lang)
    # change 'null' key to 'Others'
    star_per_lang['Others'] = star_per_lang.pop(None)

    return sorted_top_lang, sorted_most_starred, star_per_lang, colors

# To create API endpoints for top 5 languages


class TopLanguages(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = get_repodata(request)[0]
        colors_data = get_repodata(request)[3]
        colors = [colors_data[key]["color"] for key in data.keys()]
        chart_data = {
            "labels": data.keys(),
            "values": data.values(),
            "colors": colors,
        }
        return Response(chart_data)

# To create API endpoints for top 5 most starred repos


class MostStarred(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = get_repodata(request)[1]
        chart_data = {
            "labels": data.keys(),
            "values": data.values(),
        }
        return Response(chart_data)

# To create API endpoints for stars per languages


class StarsPerLanguages(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        data = get_repodata(request)[2]
        colors_data = get_repodata(request)[3]
        colors = [colors_data[key]["color"] for key in data.keys()]
        chart_data = {
            "labels": data.keys(),
            "values": data.values(),
            "colors": colors,
        }
        return Response(chart_data)
