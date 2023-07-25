from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete,m2m_changed
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class EmployeeDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.BigIntegerField()
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save,sender=EmployeeDetails)
def create_new_employee_post_save(sender,instance,created,*args,**kwargs):
    print(args,kwargs)
    print('Im django signal post save')
    print('sender',sender)
    print('instance',instance)
    print('created',created)
    if created:
        print('Created New Empmloyee',instance.name)
        ''''
        after creating the may you can write the code for email sending
        '''
        # trigger pre save
        instance.save()
        # trigger post save

#post_save.connect(create_new_employee_post_save,sender=EmployeeDetails)


def create_new_employee_pre_save(sender,instance,*args,**kwargs):
    '''
    before save into db
    '''
    print('Im django signal pre save')
    print(sender,instance,args,kwargs)
    print('id',instance.id)
    print('name ',instance.name)
    #instance.save()

pre_save.connect(create_new_employee_pre_save,sender=EmployeeDetails)


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True,null=True)
    liked = models.ManyToManyField(User,blank=True)
    notify_user = models.BooleanField(default=False)
    notify_user_time_stamp = models.DateTimeField(blank=True,null=True,auto_now_add=False)
    active = models.BooleanField(default=True)
@receiver(pre_save,sender=BlogPost)
def create_blog_post_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)# this is my title ==> this-is-my-title
        instance.save()
    if instance.id and instance.notify_user:
        print('Notify User')
        instance.notify_user=False
        # celery worker task -> offloan -> Time & Tasks 2
        instance.notify_user_time_stamp = timezone.now()



# @receiver(post_save,sender=BlogPost)
# def create_blog_post_post_save(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug=slugify(instance.title)# this is my title ==> this-is-my-title
#         instance.save()


# pre_delete and post_delete

@receiver(pre_delete,sender=BlogPost)
def delete_blog_post_pre_delete(sender,instance,*args,**kwargs):
    # move or make a backup of this data
    print(f'{instance.id} will be removed')

@receiver(post_delete,sender=BlogPost)
def delete_blog_post_post_delete(sender,instance,*args,**kwargs):
    print(f'{instance.id} has been removed')

# m2m_changed singal

@receiver(m2m_changed,sender=BlogPost.liked.through)
def m2m_blog_post(sender,instance,action,model,pk_set,*args,**kwargs):
    print('args ',args)
    print('kwargs ',kwargs)
    print('#'*30)
    print(action)
    if action == 'pre_add':
        print('was added')
        qs = model.objects.filter(pk__in=pk_set)
        print(qs.count())
