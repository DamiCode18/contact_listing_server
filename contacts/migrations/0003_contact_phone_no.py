# Generated by Django 3.0.7 on 2020-06-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200616_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_no',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
