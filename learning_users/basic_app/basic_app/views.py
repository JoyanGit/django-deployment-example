from django.shortcuts import render

# Create your views here.
def index(request):
    joyan_context_dict = {'Joyan_Text': 'Hello World' , 'Joyan_Number' : 101 }
    return render(request, 'basic_app/index.html', joyan_context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
