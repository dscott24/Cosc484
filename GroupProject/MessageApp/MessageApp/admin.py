from django.contrib import admin

from .models import User
from .models import Member
from .models import Message
from .models import Thread

admin.site.register(Thread)
admin.site.register(User)
admin.site.register(Member)
admin.site.register(Message)