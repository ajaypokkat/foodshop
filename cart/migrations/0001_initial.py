# Generated by Django 3.2.12 on 2022-04-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=250, unique=True)),
                ('dat_added', models.DateField(auto_now=True)),
            ],
        ),
    ]
