# Generated by Django 5.0.6 on 2024-07-04 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0008_alter_chaicertificate_certificate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
