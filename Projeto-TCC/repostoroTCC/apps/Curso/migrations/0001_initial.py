# Generated by Django 4.1 on 2022-08-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('modalidade', models.CharField(choices=[('B', 'Bacharelado'), ('L', 'Licenciatura'), ('T', 'Tecnologo')], max_length=1)),
            ],
        ),
    ]
