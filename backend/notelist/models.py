from django.db import models

# Create your models here.
class Notelist(models.Model):
    task = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField("Created date", auto_now_add=True)


    def __str__(self) -> str:
        return self.task
