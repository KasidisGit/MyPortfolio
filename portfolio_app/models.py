from django.db import models

class Form(models.Model):
    contact_email = models.EmailField(null=False)
    contact_subject = models.CharField(null=False,max_length=500)
    contact_message = models.CharField(null=False,max_length=1000)

    def __str__(self):
        return 'Inbox from: '+ self.contact_email
