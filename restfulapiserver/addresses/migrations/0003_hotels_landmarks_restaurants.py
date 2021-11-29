# Generated by Django 3.2.5 on 2021-10-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_image_myimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('english_rating', models.CharField(default='', max_length=255)),
                ('english_name', models.CharField(default='', max_length=255)),
                ('english_address', models.CharField(default='', max_length=255)),
                ('picture_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Landmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('english_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('represent', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('english_name', models.CharField(default='', max_length=255)),
                ('english_represent', models.CharField(default='', max_length=255)),
                ('english_address', models.CharField(default='', max_length=255)),
                ('picture_name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]