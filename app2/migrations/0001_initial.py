# Generated by Django 4.2.7 on 2023-12-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('Ccname', models.CharField(max_length=100, primary_key=100, serialize=False)),
            ],
        ),
    ]
