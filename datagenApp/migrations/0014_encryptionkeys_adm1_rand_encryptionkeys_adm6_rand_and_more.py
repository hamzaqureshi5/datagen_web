# Generated by Django 5.0.4 on 2024-05-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0013_alter_encryptionkeys_pin1_rand"),
    ]

    operations = [
        migrations.AddField(
            model_name="encryptionkeys",
            name="adm1_rand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="adm6_rand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="pin2_rand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="puk1_rand",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="encryptionkeys",
            name="puk2_rand",
            field=models.BooleanField(default=False),
        ),
    ]
