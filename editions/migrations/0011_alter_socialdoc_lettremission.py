# Generated by Django 3.2.4 on 2021-11-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordres', '0008_alter_lettremissionlink_lettremission'),
        ('editions', '0010_stc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialdoc',
            name='lettremission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ordres.lettremission', verbose_name='Lettre de Mission'),
        ),
    ]