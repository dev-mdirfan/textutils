# Pipeline for textutils

## Home Page

- We need to a home page.

```py
def index(request):
    return HttpResponse("<h3>Home</h3> <br> <p>This is Home Page</p>")
```

```py
urlpatterns = [
    path('', views.index, name='index'),
]
```

### Remove Punctuation

```py
# Creating Pipeline
urlpatterns = [
    path('removepunc', views.removepunc, name='removepunc'),
]
```

__How to get the text inputed in removepunc :__

```py
def removepunc(request):
    # Getting text and printing
    print(request.GET.get('text', 'default'))
    #  Get the text
    text = request.GET.get('text', 'default')
    print(text)

    # Analyze the text
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <h1>Remove Punctuation :</h1> <a href=''></a>")
```

### Capitalize

```py
urlpatterns = [
    path('capitalize', views.capitalize, name='capitalize'),
]
```

```py
def capitalize(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Capitalize :</b> <a href=''></a>")
```

### New Line Remove

```py
urlpatterns = [
    path('newlineremove', views.newlineremove, name='newlineremove'),
]
```

```py
def newlineremove(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>New Line Remove :</b> <a href=''></a>")
```

### Space Remove

```py
urlpatterns = [
    path('spaceremove', views.spaceremove, name='spaceremove'),
]
```

```py
def spaceremove(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Space Remover :</b> <a href=''></a>")
```

### Character Count

```py
urlpatterns = [
    path('charcount', views.charcount, name='charcount')
]
```
```py
def charcount(request):
    return HttpResponse("<a href='/'>Back to Home Page</a> <br><br> <b>Character Count :</b> <a href=''></a>")
```







