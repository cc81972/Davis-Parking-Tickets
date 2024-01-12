# Generated by Django 4.2.7 on 2023-11-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(verbose_name='Date and Time ticketed')),
            ],
        ),
    ]