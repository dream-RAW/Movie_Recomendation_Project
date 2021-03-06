# Generated by Django 2.0 on 2019-03-04 07:47

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_remove_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='TypeOfUser',
            field=models.CharField(choices=[('Avid user', 'Avid user'), ('Once in a week', 'Once in a week'), ('few times in month', 'few times in month')], default='few times in month', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='age_group',
            field=models.CharField(choices=[('18-30', '18-30'), ('31-41', '31-41'), ('42-55', '42-55'), ('55 above', '55 above')], default='18-30', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Horror', 'Horror'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('War', 'War'), ('Crime', 'Crime'), ('Mystery', 'Mystery'), ('Documentary', 'Documentary'), ('Fantasy', 'Fantasy'), ('Musical', 'Musical')], default='Comedy', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='hobbies',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
