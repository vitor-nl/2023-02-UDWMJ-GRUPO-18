# Generated by Django 4.1 on 2023-11-30 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=255)),
                ('datanasc', models.DateField()),
                ('genero', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='attendant.pessoa')),
                ('especialidade', models.CharField(max_length=100)),
            ],
            bases=('attendant.pessoa',),
        ),
    ]
