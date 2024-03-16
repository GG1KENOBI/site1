# Generated by Django 2.2 on 2024-03-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
