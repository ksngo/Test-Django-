# Generated by Django 2.2.6 on 2020-05-06 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200505_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
