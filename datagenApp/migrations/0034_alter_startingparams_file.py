# Generated by Django 5.0.4 on 2024-05-03 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0033_alter_textfile_file_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="startingparams",
            name="file",
            field=models.ForeignKey(
                auto_created=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="datagenApp.textfile",
            ),
        ),
    ]
