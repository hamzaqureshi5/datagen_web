# Generated by Django 5.0.4 on 2024-05-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0003_encryptionkeys_adm1_encryptionkeys_adm6_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encryptionkeys",
            name="size",
            field=models.IntegerField(max_length=5),
        ),
    ]