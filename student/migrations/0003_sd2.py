# Generated by Django 4.1.8 on 2023-07-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_std'),
    ]

    operations = [
        migrations.CreateModel(
            name='SD2',
            fields=[
                ('hall_ticket_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('training_type', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
    ]
