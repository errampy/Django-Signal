from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User

def login_success(sender,request,user,*args,**kwargs):
    print('------------------------------------')
    print('logged in signal')
    print('sender ',sender)
    print('request ',request)
    print('user ',user)
    print('args ',args)
    print('kewarg ',kwargs)

user_logged_in.connect(login_success,sender=User)

def logout_success(sender,request,user,*args,**kwargs):
    print('------------------------------------')
    print('logged out in signal')
    print('sender ',sender)
    print('request ',request)
    print('user ',user)
    print('args ',args)
    print('kewarg ',kwargs)

user_logged_out.connect(logout_success,sender=User)

def login_failed(sender,credentials,request,*args,**kwargs):
    print('------------------------------------')
    print('logged  in failed signal')
    print('sender ',sender)
    print('request ',request)
    print('credentials ',credentials)
    print('args ',args)
    print('kewarg ',kwargs)

user_login_failed.connect(login_failed)

