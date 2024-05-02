# Generated by Django 5.0.4 on 2024-05-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datagenApp', '0015_securitykeys_startingparams_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityKeysRandomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin1_rand', models.BooleanField(default=False)),
                ('puk1_rand', models.BooleanField(default=False)),
                ('pin2_rand', models.BooleanField(default=False)),
                ('puk2_rand', models.BooleanField(default=False)),
                ('adm1_rand', models.BooleanField(default=False)),
                ('adm6_rand', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='adm1_rand',
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='adm6_rand',
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='pin1_rand',
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='pin2_rand',
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='puk1_rand',
        ),
        migrations.RemoveField(
            model_name='securitykeys',
            name='puk2_rand',
        ),
    ]
