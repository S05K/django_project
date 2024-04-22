import pdb
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/')
    applicants = models.ManyToManyField(CustomUser, through='JobApplication')

    def __str__(self):
        return self.title
    

class JobApplication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.id}"




# SIGNALS IN DJANGO........
@receiver(post_save, sender=CustomUser)
def send_notification_email(sender,instance,created,**kwargs):
    if created:
       print("BHAAG DK BOSE..............")
       subject = "Testing maill"
       message = f"Welcome!!! {instance.username}"
       email_from = settings.EMAIL_HOST_USER
       recipient_list = [instance.email]
       send_mail(subject,message,email_from,recipient_list)
    

@receiver(post_delete, sender=CustomUser)
def delete1(sender, instance, **kwargs):
        print("BHAAAG DK BOSE......")


@receiver(post_init, sender = CustomUser)
def hello(sender, instance, **kwargs):
    print("Love the way you lie....")