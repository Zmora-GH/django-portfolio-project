from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
    	return f'<{self.user} account>'

    @receiver(models.signals.post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)
        instance.account.save()

