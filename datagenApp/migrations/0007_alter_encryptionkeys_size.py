# Generated by Django 5.0.4 on 2024-05-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0006_encryptionkeys_adm1_encryptionkeys_adm6_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encryptionkeys",
            name="size",
            field=models.CharField(max_length=5),
        ),
    ]
