# Generated by Django 5.0.4 on 2024-05-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0010_remove_encryptionkeys_adm1_rand_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="encryptionkeys",
            name="pin1_rand",
            field=models.BooleanField(default=True),
        ),
    ]
