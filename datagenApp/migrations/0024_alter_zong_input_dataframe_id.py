# Generated by Django 5.0.4 on 2024-05-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagenApp", "0023_alter_zong_input_dataframe_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zong_input_dataframe",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
