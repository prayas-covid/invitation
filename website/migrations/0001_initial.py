# Generated by Django 3.2.3 on 2021-06-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('rollNo', models.CharField(max_length=9)),
                ('coming', models.CharField(max_length=20)),
            ],
        ),
    ]