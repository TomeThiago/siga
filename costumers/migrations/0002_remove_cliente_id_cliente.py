# Generated by Django 5.0.3 on 2024-05-25 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costumers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id_cliente',
        ),
    ]
