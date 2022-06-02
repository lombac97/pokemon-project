# Generated by Django 4.0.4 on 2022-06-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('regions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='locations', to='places.region')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('pokemon_count', models.BigIntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='areas', to='places.location')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
    ]
