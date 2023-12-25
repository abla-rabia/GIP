from django.db import models



class Participant(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200, unique = True)
    discord_id = models.CharField(max_length=20,unique=True, default='')
    organization = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    how_did_you_hear = models.CharField(max_length=255, blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name