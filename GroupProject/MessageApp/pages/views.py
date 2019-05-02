from  django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from MessageApp.models import User


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"signupNew.html", {})


# Create your views here.
def login_view(request, *args, **kwargs):
    return render(request,"login.html", {})



def profile_view(request, *args, **kwargs):
    return render(request,'profile.html', {})

 #   def get_context_data(self, **kwargs):
  #      user = User.objects.get(pk=self.kwargs['pk'])
   #     return {'user': user}

class HomePageView(TemplateView):
    template_name = 'pages/home.html'