# Generated by Django 3.1.3 on 2020-12-16 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='statements_pdf',
            field=models.FileField(upload_to='E:\\New pro2\\banking-system-master\\media'),
        ),
    ]
