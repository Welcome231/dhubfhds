from django.db import models

class nameee(models.Model):
    title = models.CharField(max_length=30, null=True)
    #author = models.CharField(max_length=30)
    content = models.EmailField(max_length=255)
    

    class Meta:
        db_table = "nameee"



