# Generated by Django 4.0.4 on 2022-06-01 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0009_pokemon_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprite',
            name='front_default',
            field=models.CharField(max_length=300, null=True),
        ),
    ]