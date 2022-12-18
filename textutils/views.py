# I have created this file - Irfan

# @author: md-irfan

from django.http import HttpResponse    # HttpResponse give the 
from django.shortcuts import render     # It import the templates file like index.html and renders


def index(request):
    return render(request, 'index.html')

# About Page
def about(request):
    return HttpResponse('About HttpResponse Hello Irfan')


# Exercise-1 --- Solution ------------------------------>
def exercise1(request):
    with open(r'D:\Python🔒\Django\Projects\CWH-Projects\textutils✔️\textutils\1.txt', 'r') as file:
        content = file.read()
    return HttpResponse(content)


# Exercise-2 --- Solution ------------------------------>
def exercise2(request):
    return HttpResponse('''<h1>Welcome to my favorite websites list</h1> <h3>Question : Create a page for listing your 5 favorite website links</h3> <a href="https://www.linkedin.com" target="_blank">Go to LinkedIn</a> <br><br> <a href="https://leetcode.com/">Go to Leetcode</a> <br><br> <a href="https://www.codechef.com/">Go to CodeChef</a> <br><br> <a href="https://getbootstrap.com/">Got to Bootstrap</a> <br><br> <a href="https://www.djangoproject.com/">Go to Django Website</a> <br><br><br> <a href='/'>Back to Home Page</a>''')

# Pipeline for textutils ------------------------------->
def home(request):
    return render(request, 'pipeline.html')
# Remove Punctuation
def removepunc(request):
    #  Get the text
    text = request.GET.get('text', 'default')
    print(text)
    # Analyze the text
    return HttpResponse("<a href='/home'>Back to Home Page</a> <br><br> <h1>Remove Punctuation :</h1>")
# Capitalize
def capitalize(request):
    return HttpResponse("<a href='/home'>Back to Home Page</a> <br><br> <h1>Capitalize :</h1>")
# New Line Remove
def newlineremove(request):
    return HttpResponse("<a href='/home'>Back to Home Page</a> <br><br> <h1>New Line Remove :</h1>")
# Space Remove
def spaceremove(request):
    return HttpResponse("<a href='/home'>Back to Home Page</a> <br><br> <h1>Space Remover :</h1>")
# Character Count
def charcount(request):
    return HttpResponse("<a href='/home'>Back to Home Page</a> <br><br> <h1>Character Count :</h1>")



## Actual Code for Project text Utils -------------------------->
def analyze(request):
    #  Get the text
    text = request.GET.get('text', 'default')
    
    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    # print(removepunc)
    # print(text)
    
    # Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed, 'original_text':text}
        # Analyze the text
        # return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <h1>Remove Punctuation :</h1> <a href=''></a>")
        return render(request, 'analyze.html', params)
    
    if uppercase=="on":
        analyzed = ""
        for char in text:
            analyzed += char.upper()
        params = {'purpose':'Changed in Upper Case', 'analyzed_text':analyzed, 'original_text':text}
        return render(request, 'analyze.html', params)
    
    if newlineremove=="on":
        analyzed = ""
        for char in text:
            if char!="\n":
                analyzed += char
        params = {'purpose':'New Line Remove', 'analyzed_text':analyzed, 'original_text':text}
        return render(request, 'analyze.html', params)
    
    if spaceremove=="on":
        analyzed = ""
        # for index in range(len(text)-1):
        for index, char in enumerate(text):
            if not(text[index]==" " and text[index+1]==" "):
                analyzed += char
        params = {'purpose':'Removed Spaces', 'analyzed_text':analyzed, 'original_text':text}
        return render(request, 'analyze.html', params)
    
    if charcount=="on":
        analyzed = 0
        # for index in range(len(text)-1):
        for index in range(len(text)):
            if 'a'<=text[index]<='z' or 'A'<=text[index]<='Z':
                analyzed += 1
        params = {'purpose':'Characters are counted', 'analyzed_text':analyzed, 'original_text':text}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("<br><br><center><h1>Error</h1><br><h1>404 Error</h1><br><h1>Please check the CheckBox </h1> <h2><a href='/'>Back to Analyze Page</a></h2></center>")


# Templates
# def index(request):
#     return render(request, 'index.html')
