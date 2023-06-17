from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .forms import SignupForm
# Create your views here.
def chatTranslation(request):
    template = loader.get_template('chatTranslation/myfirst.html')
    return HttpResponse(template.render())

def signup(request):
    if request.POST:
        form = SignupForm(request.POST, request.FILES)
        print (request.FILES)
        if form.is_valid():
            form.save()
        return redirect(chatTranslation)
    return render(request, 'chatTranslation/index.html', {'form' : SignupForm})

