# Generated by Django 2.2.6 on 2020-05-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='posted_when',
            field=models.DateTimeField(auto_now=True),
        ),
    ]