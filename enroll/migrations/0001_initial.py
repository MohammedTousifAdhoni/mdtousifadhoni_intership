# Generated by Django 3.2.6 on 2022-01-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
