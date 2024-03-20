# Generated by Django 4.1 on 2022-08-24 22:52

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Orientador', '0001_initial'),
        ('Autor', '0001_initial'),
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano_documento', models.IntegerField(verbose_name='Ano da Publicação do Documento')),
                ('resumo', models.TextField()),
                ('arquivo_documento', models.FileField(upload_to='arquivos/')),
                ('palavras_chave', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autor.autor')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Curso.curso')),
                ('orientador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orientador.orientador')),
            ],
        ),
    ]
