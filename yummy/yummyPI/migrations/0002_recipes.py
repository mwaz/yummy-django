# Generated by Django 2.0 on 2018-01-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummyPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=256)),
                ('recipe_ingredients', models.CharField(max_length=256)),
                ('recipe_methods', models.CharField(max_length=256)),
            ],
        ),
    ]