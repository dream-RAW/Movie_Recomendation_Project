# Generated by Django 2.0 on 2019-03-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0005_auto_20190305_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='MovieID',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
