# Generated by Django 2.1.4 on 2018-12-22 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='../static/images/profile_default.jpg', upload_to='users/%Y', verbose_name='Аватарка'),
        ),
    ]