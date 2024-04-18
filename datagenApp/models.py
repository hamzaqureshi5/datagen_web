from django.db import models

# Create your models here.

class TextFile(models.Model):
    file = models.FileField(upload_to='text_files/')

    def __str__(self):
        return self.file.name