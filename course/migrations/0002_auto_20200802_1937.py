# Generated by Django 3.0.8 on 2020-08-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(blank=True, choices=[('FULL-TIME', 'FULL-TIME'), ('WEEKEND', 'Weekend')], max_length=100, null=True),
        ),
    ]
