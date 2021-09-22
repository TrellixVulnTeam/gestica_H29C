# Generated by Django 3.2.4 on 2021-09-20 17:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ordres', '0007_lettremission_nothosted'),
        ('tasks', '0007_alter_benefititem_frequency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('code_account', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Code Post / Compte')),
                ('name_account', models.CharField(max_length=50, verbose_name='Libellé du Compte')),
                ('sens', models.IntegerField(choices=[(0, 'Débit'), (1, 'Crédit')], verbose_name='Sens')),
                ('account_lower', models.IntegerField(verbose_name='Compte Inférieure')),
                ('account_upper', models.IntegerField(verbose_name='Compte Supérieure')),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exercice', models.CharField(max_length=4, unique=True, verbose_name='Exercice')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_start', models.DateField(verbose_name='Date début')),
                ('date_closing', models.DateField(verbose_name='Date clôture')),
                ('Numbre_month', models.IntegerField(verbose_name='Nombre de mois')),
                ('date_declaration', models.DateField(verbose_name='Date limite déclaration')),
                ('date_ago', models.DateField(verbose_name='Date limite AGO')),
                ('exercice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.exercice', verbose_name='Exercice')),
                ('lettremission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ordres.lettremission', verbose_name='Lettre de Mission')),
            ],
        ),
        migrations.CreateModel(
            name='DataAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Amount', models.FloatField(default=0, verbose_name='Montant')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.account', verbose_name='Post / Compte')),
                ('exercice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.situation', verbose_name='Exercice')),
            ],
        ),
    ]