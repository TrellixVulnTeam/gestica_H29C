# Generated by Django 3.2.4 on 2021-09-27 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20210927_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxreturn',
            old_name='exercice',
            new_name='situation',
        ),
    ]