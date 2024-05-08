# Generated by Django 5.0.4 on 2024-05-03 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0035_alter_securitykeys_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encryptionkeys",
            name="file",
            field=models.ForeignKey(
                auto_created=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datagenApp.textfile",
            ),
        ),
        migrations.AlterField(
            model_name="securitykeys",
            name="file",
            field=models.ForeignKey(
                auto_created=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datagenApp.textfile",
            ),
        ),
    ]