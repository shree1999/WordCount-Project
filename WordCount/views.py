from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def countwords(request):
    text = request.GET['fulltext']
    count_dict = {}
    fulltext = text.split()
    for item in fulltext:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    sorted_words = sorted(count_dict.items(), key=operator.itemgetter(1), reverse=True)
    total = 0
    for key in count_dict.keys():
        total = total + count_dict[key]

    return render(request, 'count.html', {'string':text, 'total':total , 'frequency':sorted_words})
