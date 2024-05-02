from django.db import models

# Create your models here.


class TextFile(models.Model):
    file = models.FileField(upload_to="text_files/")

    def __str__(self):
        return self.file.name


class StartingParams(models.Model):
    size = models.CharField(max_length=5, null=False, default="FFFFFFFFFFFFFFFFFFFFF")
    iccid = models.CharField(max_length=20, null=False, default="222222222222222222222")
    imsi = models.CharField(max_length=15, null=False, default="1111111111111111")

    def __str__(self):
        return self.iccid


class EncryptionKeys(models.Model):
    k4 = models.CharField(max_length=64, null=False, default="FFFFFFFFFFFFFFFFFFFFF")
    op = models.CharField(max_length=64, null=False, default="FFFFFFFFFFFFFFFFFFFFF")


class SecurityKeys(models.Model):
    pin1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    puk1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    pin2 = models.CharField(max_length=8, null=False, default="1234FFFF")
    puk2 = models.CharField(max_length=8, null=False, default="1234FFFF")
    adm1 = models.CharField(max_length=8, null=False, default="1234FFFF")
    adm6 = models.CharField(max_length=8, null=False, default="1234FFFF")


class SecurityKeysRandomization(models.Model):
    pin1_rand = models.BooleanField(null=False, default=False)
    puk1_rand = models.BooleanField(null=False, default=False)
    pin2_rand = models.BooleanField(null=False, default=False)
    puk2_rand = models.BooleanField(null=False, default=False)
    adm1_rand = models.BooleanField(null=False, default=False)
    adm6_rand = models.BooleanField(null=False, default=False)


class ElectricalDataJson(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    parameter = models.CharField(null=False, default="DEFAULT", max_length=10)
    lclip = models.IntegerField(null=False, default=0)
    rclip = models.IntegerField(null=False, default=32)

class GraphicalDataJson(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    parameter = models.CharField(null=False, default="DEFAULT", max_length=10)
    lclip = models.IntegerField(null=False, default=0)
    rclip = models.IntegerField(null=False, default=32)


class Zong_Input_Dataframe(models.Model):
    id = models.IntegerField(primary_key=True)
    iccid = models.CharField(null=False, default="NaN", max_length=20)
    imsi = models.CharField(null=False, default="NaN", max_length=15)

