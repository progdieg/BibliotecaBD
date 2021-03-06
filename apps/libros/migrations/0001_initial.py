# Generated by Django 4.0.4 on 2022-06-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=120, verbose_name='Título')),
                ('núm_pag', models.SmallIntegerField(verbose_name='Número de Página')),
                ('editorial', models.CharField(max_length=50, verbose_name='Editorial')),
                ('isbn', models.CharField(max_length=50, verbose_name='ISBN')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
            ],
        ),
    ]
