# Generated by Django 5.0.3 on 2024-05-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('id_cliente', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
