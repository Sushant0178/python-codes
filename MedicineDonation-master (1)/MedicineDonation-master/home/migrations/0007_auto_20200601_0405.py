# Generated by Django 3.0.6 on 2020-05-31 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_donations_accepted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='accepted_by',
            field=models.TextField(max_length=12),
        ),
    ]
