# Exercise 1

__Ques :__ Create a `1.txt` file and render its content to a web page.

- Preview the page [/exercise1]()

## Guide to build

- Create a text file and fill the content as example given below -

```txt
<h1>Exercise : 1</h1>

<h2>Question : Create a text file and render to a web page.</h2> 

<p>Welcome!</p>
<p>This is paragraph of the text file.</p>
 
<p>Dummy Text</p>

<a href="/">Back to Home Page</a>
```

__Solution 1 :__

```py
# Solution 1 ->

def exercise1(request):
    file = open(r'D:\Python\Django\textutils\1.txt', 'r+')
    return HttpResponse(file.read())
```

__Solution 2 :__

```py
# Solution 2  -->
def exercise1(request):
    f1 = open(r'D:\Python\Django\Projects\textutils\1.txt', "r")
    return HttpResponse("<h1> %s </h1>"%(f1.read()))
```

__Solution 3 :__

```py
# Solution 3 -->
def exercise1(request):
    with open(r'D:\Python\Django\Projects\textutils\1.txt', 'r') as file:
        content = file.read()
    return HttpResponse(content)
```





