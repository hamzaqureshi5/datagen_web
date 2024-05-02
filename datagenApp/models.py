from django.db import models

# Create your models here.


class TextFile(models.Model):
    file = models.FileField(upload_to="text_files/")

    def __str__(self):
        return self.file.name


class EncryptionKeys(models.Model):
    k4 = models.CharField(max_length=64, null=False, default="FFFFFFFFFFFFFFFFFFFFF")
    op = models.CharField(max_length=64, null=False, default="FFFFFFFFFFFFFFFFFFFFF")
    size = models.CharField(max_length=5, null=False, default="FFFFFFFFFFFFFFFFFFFFF")
    iccid = models.CharField(
        max_length=20, null=False, default="FFFFFFFFFFFFFFFFFFFFFF"
    )
    imsi = models.CharField(max_length=15, null=False, default="1111111111111111")
    pin1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    puk1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    pin2 = models.CharField(max_length=8, null=False, default="1234FFFF")
    puk2 = models.CharField(max_length=8, null=False, default="1234FFFF")
    adm1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    adm6 = models.CharField(max_length=8, null=False, default="1234FFFF")
    pin1_rand = models.BooleanField(null=False, default=False)
    puk1_rand = models.BooleanField(null=False, default=False)
    pin2_rand = models.BooleanField(null=False, default=False)
    puk2_rand = models.BooleanField(null=False, default=False)
    adm1_rand = models.BooleanField(null=False, default=False)
    adm6_rand = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.iccid
