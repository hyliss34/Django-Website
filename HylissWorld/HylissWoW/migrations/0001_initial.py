# Generated by Django 2.0.3 on 2018-03-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100)),
                ('serveur', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=10)),
                ('local', models.CharField(max_length=10)),
                ('head', models.CharField(max_length=100)),
            ],
        ),
    ]
