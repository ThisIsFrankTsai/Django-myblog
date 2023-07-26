# Generated by Django 4.0.4 on 2023-07-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='Edit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pic_url',
            field=models.URLField(default='Nono', max_length=250),
            preserve_default=False,
        ),
    ]