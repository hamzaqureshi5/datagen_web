from django.db import models

# Create your models here.


class TextFile(models.Model):
    file = models.FileField(upload_to="text_files/")

    def __str__(self):
        return self.file.name


class EncryptionKeys(models.Model):
    k4 = models.CharField(max_length=64, null=False)
    op = models.CharField(max_length=64, null=False)
    size = models.CharField(max_length=5, null=False)
    iccid = models.CharField(max_length=20, null=False)
    imsi = models.CharField(max_length=15, null=False)
    pin1 = models.CharField(max_length=8, null=False)
    puk1 = models.CharField(max_length=8, null=False)
    pin2 = models.CharField(max_length=8, null=False)
    puk2 = models.CharField(max_length=8, null=False)
    adm1 = models.CharField(max_length=8, null=False)
    adm6 = models.CharField(max_length=8, null=False)

    def __str__(self):
        return self.iccid
