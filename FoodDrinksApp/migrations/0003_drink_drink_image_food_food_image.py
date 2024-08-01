# Generated by Django 5.0.2 on 2024-08-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDrinksApp', '0002_alter_drink_drink_price_alter_food_food_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='drink_image',
            field=models.ImageField(blank=True, null=True, upload_to='drink_images/'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to='food_images/'),
        ),
    ]
