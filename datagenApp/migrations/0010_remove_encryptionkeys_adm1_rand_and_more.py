# Generated by Django 5.0.4 on 2024-05-02 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "datagenApp",
            "0009_alter_encryptionkeys_adm1_alter_encryptionkeys_adm6_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="adm1_rand",
        ),
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="adm6_rand",
        ),
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="pin1_rand",
        ),
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="pin2_rand",
        ),
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="puk1_rand",
        ),
        migrations.RemoveField(
            model_name="encryptionkeys",
            name="puk2_rand",
        ),
    ]
