# Exercise 2

__Question :__ Create a personal navigator for accessing your 5 favorite websites.

- Preview of the Page [/exercise2]()

```py
def exercise2(request):
    return HttpResponse('''<h1>Welcome to my favorite websites list</h1> <br> 
                        <a href="https://www.linkedin.com" target="_blank">Go to LinkedIn</a> <br><br> 
                        <a href="https://leetcode.com/">Go to Leetcode</a> <br><br> 
                        <a href="https://www.codechef.com/">Go to CodeChef</a> <br><br> 
                        <a href="https://getbootstrap.com/">Got to Bootstrap</a> <br><br> 
                        <a href="https://www.djangoproject.com/">Go to Django Website</a> <br><br> 
                        <a href='/'>Back to Home Page</a>''')
```