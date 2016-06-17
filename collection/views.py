from django.shortcuts import render

def index(request):
    #defining the variable
    number = 6
    thing = "Thing name"
    #passing the variable to the view
    return render(request, 'index.html', {'number':number, 'thing':thing,})
