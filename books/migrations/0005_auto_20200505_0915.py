# Generated by Django 2.2.6 on 2020-05-05 09:15

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200505_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, to='books.Category'),
        ),
    ]
