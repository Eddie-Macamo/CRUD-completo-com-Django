# Generated by Django 5.1.1 on 2025-01-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('bairro', models.CharField(max_length=30)),
                ('numero_celular', models.CharField(max_length=15)),
                ('estado_civil', models.CharField(max_length=20)),
            ],
        ),
    ]
