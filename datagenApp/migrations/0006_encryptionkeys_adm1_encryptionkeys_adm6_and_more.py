# Generated by Django 5.0.4 on 2024-05-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0005_remove_encryptionkeys_adm1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="encryptionkeys",
            name="adm1",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="adm6",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="iccid",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="imsi",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="pin1",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="pin2",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="puk1",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="puk2",
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="size",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]