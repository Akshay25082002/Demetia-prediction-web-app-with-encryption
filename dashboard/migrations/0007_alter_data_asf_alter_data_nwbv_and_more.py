# Generated by Django 4.2.9 on 2024-01-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_height_data_asf_remove_data_age_data_educ_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ASF',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nWBV',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.PositiveIntegerField(choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]
