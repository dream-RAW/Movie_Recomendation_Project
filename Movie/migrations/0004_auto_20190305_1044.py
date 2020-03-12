# Generated by Django 2.0 on 2019-03-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0003_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='MovieGenre',
            field=models.CharField(choices=[('Action', 'action'), ('Comedy', 'comedy'), ('Romance', 'romance'), ('Thriller', 'thriller'), ('Horror', 'Horror')], default='Comedy', max_length=100),
        ),
    ]
