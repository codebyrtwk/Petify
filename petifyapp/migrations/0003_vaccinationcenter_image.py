# Generated by Django 3.2.5 on 2021-07-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petifyapp', '0002_vaccinationcenter'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinationcenter',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
