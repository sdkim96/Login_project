# Generated by Django 4.2.1 on 2023-05-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_busdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('label', models.IntegerField()),
                ('x_coord', models.FloatField()),
                ('y_coord', models.FloatField()),
            ],
        ),
    ]
