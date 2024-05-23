# Generated by Django 5.0.6 on 2024-05-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recordatorio',
            fields=[
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
