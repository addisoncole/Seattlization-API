# Generated by Django 2.0.9 on 2019-01-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seattlizationAPI', '0024_homelesscount_number_sheltered_in_seattle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingmarket',
            name='month',
            field=models.IntegerField(null=True),
        ),
    ]
