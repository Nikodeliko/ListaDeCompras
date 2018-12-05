from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")

    def __str__(self):
        return '{}'.format(self.user.username)

@receiver(post_save, sender=User)
def CrearPerfilUsuario(sender, instance=None, created=False, **kwargs):
    if created:
        Perfil.objects.get_or_create(user=instance)

@receiver(pre_delete, sender=User)
def EliminarPerfilUsuario(sender, instance=None, **kwargs):
    if instance:
        user_profile = Perfil.objects.get(user=instance)
        user_profile.delete()
