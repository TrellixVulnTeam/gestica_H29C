# Generated by Django 3.2.4 on 2021-10-23 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20211023_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaremeIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impot', models.IntegerField(choices=[(0, 'IS'), (1, 'IR'), (2, 'CSS')], default=0, verbose_name='Impôt')),
                ('plancher', models.FloatField(default=0, verbose_name='Plancher')),
                ('plafond', models.FloatField(default=0, verbose_name='Plafond')),
                ('taux', models.FloatField(default=0, verbose_name='Taux')),
                ('montant_a_deduire', models.FloatField(default=0, verbose_name='Montant à Déduire')),
                ('a_partir_du', models.DateField(blank=True, null=True, verbose_name='A Partir de :')),
                ('jusqu_au', models.DateField(blank=True, null=True, verbose_name="Jusqu'au :")),
                ('taux_specifique', models.BooleanField(default=False, verbose_name='Taux Spécifique?')),
            ],
        ),
        migrations.CreateModel(
            name='ImpotSociete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pourcentage', models.FloatField(default=0, verbose_name='Pourcentage')),
                ('benefice', models.IntegerField(choices=[(0, 'Progressif Normal'), (1, 'Progressif Plafoné'), (2, 'Proportionnel'), (3, 'Exonéré')], default=0, verbose_name='Bénéfice')),
                ('base', models.FloatField(default=0, verbose_name="Base de l'Impôt ")),
                ('taux', models.FloatField(default=0, verbose_name="Taux de l'Impôt")),
                ('deduction', models.FloatField(default=0, verbose_name='Montant à Déduire')),
                ('amount', models.FloatField(default=0, verbose_name="Montant de l'Impôt")),
                ('auto_genre', models.BooleanField(default=False, verbose_name='Compte Auto-Généré ?')),
                ('ordre', models.IntegerField(null=True, verbose_name='Ordre')),
                ('situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.situation', verbose_name='Exercice')),
            ],
        ),
    ]