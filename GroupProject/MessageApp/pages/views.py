from  django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from MessageApp.models import User
from MessageApp.forms import RegistrationForm
from MessageApp.models import Thread, Message, Member


class Views():
    this_thread=None

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

    def create_thread(request):
        print("thread created")
        name_of_thread = request.POST.get('threads_name')
        print(name_of_thread)
        number_of_Members = request.POST.get('member_number')
        members = request.POST.get('member_username')

        newThread = Thread(name=name_of_thread)
        newThread.save()
        threads = Thread.objects.all()
        messages=Message.objects.all()
        return render(request,'profile.html',{'threads': threads, 'messages' : messages})


    def create_message(request):

        message_text=request.POST.get('text_message')
        current_user= request.user
        message_image= request.POST.get('message__image')
        message_thread_ID=request.POST.get('current_thread')
        print(message_thread_ID)
        message_thread=Thread.objects.get(thread_ID=message_thread_ID)
    
        newMessage = Message(text=message_text, user_ID=current_user, image=message_image, thread_ID= message_thread)
        newMessage.save()
        threads = Thread.objects.all()
        messages=Message.objects.all()
        return render(request,'profile.html',{'threads': threads, 'messages' : messages, 'current_thread': message_thread_ID})

    def get_messages(request):
        current_thread_ID = request.POST.get('current_thread')
        print(current_thread_ID)
        current_thread = Thread.objects.get(thread_ID=current_thread_ID)
        print(current_thread)
        threads = Thread.objects.filter()
        messages=Message.objects.filter(thread_ID=current_thread)
        return render(request,'profile.html', {'threads': threads, 'messages' : messages, 'current_thread': current_thread_ID})


    def profile_view(request, *args, **kwargs):
        current_user=request.user
        threads = Thread.objects.filter()
       
        return render(request,'profile.html', {'threads': threads})



class HomePageView(TemplateView):
    template_name = 'pages/home.html'