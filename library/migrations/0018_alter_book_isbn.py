# Generated by Django 4.2.5 on 2023-09-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_issuedbook_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.URLField(),
        ),
    ]
