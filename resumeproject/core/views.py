from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'core/Home.html',{'home':'active'})

def contact(request):
    return render(request, 'core/contact.html',{'contact':'active'})