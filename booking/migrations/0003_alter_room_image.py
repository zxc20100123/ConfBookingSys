# Generated by Django 4.0.6 on 2022-07-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_room_location_alter_employee_employeeid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(upload_to='static/media'),
        ),
    ]