# Generated by Django 5.0.4 on 2024-05-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0022_alter_zong_input_dataframe_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zong_input_dataframe",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
