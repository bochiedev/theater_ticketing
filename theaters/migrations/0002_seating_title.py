# Generated by Django 5.0.7 on 2024-07-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seating',
            name='title',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]
