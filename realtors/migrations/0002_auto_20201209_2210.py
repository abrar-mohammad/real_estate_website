# Generated by Django 3.1.4 on 2020-12-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]