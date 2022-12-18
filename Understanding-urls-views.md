# Understanding urls and views

### 1. Inside `views.py`

__Create new file `views.py` :__

- Write comment that you'r author -

```py
# I have created this file - Irfan
# @Author : Mohd Irfan
```

```py
# Import HttpResponse from django.http to render your HTML content
from django.http import HttpResponse
```

__Creating New Page :__

- This is Example for creating new page in `views.py` file that goes into `urls.py` file.

```py
def index(request):
    # This is another way to request HttpResponse
    return HttpResponse('<h1>Hello World</h1> here you can enter html')
    # OR
    return render(request, 'index.html')
```

```py
# This is index page
def index(request):
    return HttpResponse("Your Web page content can be written here!")
```

- This is another example for about page.

```py
# This is new about page
def about(request):
    return HttpResponse("This is about page.")
```

- You also have to map this views into urls by -

### 2. Inside `urls.py`

__path meaning :__

```py
path('about/', views.about, name='about')

# First parameter is your url name.
# Second parameter is fetch the page from views dot function.
# Third parameter is name.
```

__Mapping your page into `urls.py` :__

```py
urlpatterns = [
    path('admin/', admin.site.urls),

    # Add this for index page
    path('', views.index, name='index'),

    # Add this for about page
    path('about/', views.about, name='about')
]
```

## 3. Rendering Template

__Change Setting :__

```py
# include templates in TEMPLATES in setting.py
TEMPLATES = [
    {
        'DIRS': ['templates'],
    },
]
```

__Create templates folder :__ Create a directory named as `templates` where `manage.py` stays.
__Create a `html` file :__ Create a `index.html` file inside `templates` folder.

__Change `views.py` :__

```py
# Import the
from django.shortcuts import render

# Templates Render
def index(request):
    return render(request, 'index.html')
```

### Third variable parameter of render

```py
def index(request):
    # Dictionaries can be access from templates
    params = {'name': 'Harry', 'place': 'Mars'}
    # passing dictionary as a third variable
    return render(request, 'index.html', params)
```

- You also have to add this in `html` file.

__Dictionary can be access from template :__

```py
<p>{{ name }} from {{ place }}</p>
# Variables params accessing from view.py
{{name}} from {{place}}
```
