# Generated by Django 2.0.9 on 2019-01-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seattlizationAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homelesscount',
            name='emergency_shelter',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='homelesscount',
            name='transitional_housing',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='homelesscount',
            name='unsheltered',
            field=models.IntegerField(null=True),
        ),
    ]
