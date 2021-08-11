from django.shortcuts import render

# Create your views here.
def Home(requst):
    context= {}
    return render(requst, 'index.html', context)
