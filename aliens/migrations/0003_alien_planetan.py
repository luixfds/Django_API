# Generated by Django 3.2.8 on 2021-10-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliens', '0002_rename_aliens_alien'),
    ]

    operations = [
        migrations.AddField(
            model_name='alien',
            name='planetaN',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
