# Generated by Django 2.1.1 on 2018-10-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefundo', '0013_user_details_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track_users',
            name='city',
            field=models.DurationField(default='asdf', max_length=10),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.DurationField(default='asdf', max_length=15),
        ),
    ]