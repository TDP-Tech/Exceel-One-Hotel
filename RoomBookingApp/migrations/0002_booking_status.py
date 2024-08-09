# Generated by Django 5.0.2 on 2024-08-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomBookingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('checked_in', 'Checked-In'), ('checked_out', 'Checked-Out'), ('canceled', 'Canceled')], default='pending', max_length=20),
        ),
    ]