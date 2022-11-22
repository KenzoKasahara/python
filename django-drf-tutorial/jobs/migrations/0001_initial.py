# Generated by Django 2.2.28 on 2022-11-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_email', models.EmailField(max_length=254)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('sarary', models.PositiveIntegerField()),
                ('prefectures', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
