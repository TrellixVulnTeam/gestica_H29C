# Generated by Django 3.2.4 on 2021-11-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0040_alter_dasexomodel_code_rubrique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dasmatriculeexo',
            name='dasexomodel',
        ),
        migrations.AddField(
            model_name='dasmatriculeexo',
            name='code_rubrique',
            field=models.CharField(max_length=15, null=True, verbose_name='Code Rubrique'),
        ),
    ]