from  django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from MessageApp.models import User
from MessageApp.forms import RegistrationForm


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"homepage.html", {})


# Create your views here.
def login_view(request, *args, **kwargs):
    return render(request,"login.html", {})

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'signup.html', args)

def profile_view(request, *args, **kwargs):
    return render(request,'profile.html', {})

 #   def get_context_data(self, **kwargs):
  #      user = User.objects.get(pk=self.kwargs['pk'])
   #     return {'user': user}

class HomePageView(TemplateView):
    template_name = 'pages/home.html'