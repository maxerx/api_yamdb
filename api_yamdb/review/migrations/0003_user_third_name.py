# Generated by Django 2.2.16 on 2022-11-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20221115_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='third_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='third name'),
        ),
    ]