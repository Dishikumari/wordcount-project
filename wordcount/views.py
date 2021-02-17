from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    # return HttpResponse('hello')
    #return render(request , 'homePage.html' , {'user_name' : 'this user name is dishi'})
    return render(request , 'homePage.html' )

# def activePage(request):
#     return HttpResponse('<h1>You are active</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordDictonary = {}
    # print("fulltext",fulltext)
    wordList = fulltext.split()
    length_wordList = len(wordList)

    for word in wordList:
        if word in wordDictonary:
            wordDictonary[word] += 1
        else:
            wordDictonary[word] = 1

    sortedwords = sorted(wordDictonary.items() , key=operator.itemgetter(1) , reverse=False)
    return render(request , 'count.html' , {'fulltext' : fulltext , 'count' : length_wordList , 'sortedwords' : sortedwords})


def about(request):
    return render(request , 'about.html')