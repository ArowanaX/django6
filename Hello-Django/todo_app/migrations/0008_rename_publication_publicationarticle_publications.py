# Generated by Django 3.2.9 on 2021-12-17 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_auto_20211217_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicationarticle',
            old_name='Publication',
            new_name='publications',
        ),
    ]
