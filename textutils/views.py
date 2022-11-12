# I have created this file - Irfan

# @author md-irfan

from django.http import HttpResponse    # HttpResponse give the 
from django.shortcuts import render

# from django.shortcuts import render


def index(request):
    # return HttpResponse('<h1>Hello World</h1> here you can enter html')
    return render(request, 'index.html')
def about(request):
    return HttpResponse('About HttpResponse Hello Irfan')

def webs(request):
    return HttpResponse('''<h1>Welcome to my favorite websites list</h1> <br> <a href="https://www.linkedin.com" target="_blank">Go to LinkedIn</a> <br><br> <a href="https://leetcode.com/">Go to Leetcode</a> <br><br> <a href="https://www.codechef.com/">Go to CodeChef</a> <br><br> <a href="https://getbootstrap.com/">Got to Bootstrap</a> <br><br> <a href="https://www.djangoproject.com/">Go to Django Website</a> <br><br> <a href='/'> Go to Back</a>''')
    #     return HttpResponse()

# Task by CodeWithHarry Solution -------------->

# Solution 1 -->
# def index(request):
#     file = open("1.txt", 'r+')
#     return HttpResponse(file.read())
# Solution 2  -->
# def index(request):
#     f1 = open("1.txt", "r")
#     return HttpResponse("<h1> %s </h1>"%(f1.read()))
# Solution 3 -->
# def index(request):
#     with open("1.txt", 'r') as file:
#         content = file.read()
#     return HttpResponse(content)


# Exercise-1 -------------------------------->
# Solution ->
# def index(request):
#     return HttpResponse('''<h1>Welcome to website</h1> <br> <a href="https://www.linkedin.com" target="_blank">Go to LinkedIn</a> <br><br> <a href="https://leetcode.com/">Go to Leetcode</a> <br><br> <a href="https://www.codechef.com/">Go to CodeChef</a> <br><br> <a href="https://getbootstrap.com/">Got to Bootstrap</a> <br><br> <a href="https://www.djangoproject.com/">Go to Django Website</a>''')

# def index(request):
#     # Dictionaries can be access from templates
#     # params = {'name': 'Harry', 'place': 'Mars'}
#     # passing dictionary as a third variable
#     # return render(request, 'index.html', params)
#     return render(request, 'index.html')

def removepunc(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Remove Punctuation :</b> <a href=''></a>")

def capitalize(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Capitalize :</b> <a href=''></a>")

def newlineremove(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>New Line Remove :</b> <a href=''></a>")

def spaceremove(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Space Remover :</b> <a href=''></a>")

def charcount(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Character Count :</b> <a href=''></a>")


# Templates
# def index(request):
#     return render(request, 'index.html')
