# Generated by Django 5.0.4 on 2024-05-04 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_remove_usuarioscomcamposadicionais_type_professional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='professional',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='agenda.profissional'),
        ),
    ]
