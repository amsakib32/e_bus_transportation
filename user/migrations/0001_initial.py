# Generated by Django 3.1.1 on 2021-03-08 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Smsticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.IntegerField()),
                ('is_send', models.BooleanField(default=False)),
                ('Ticket_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Of_Birth', models.DateField(null=True)),
                ('contact', models.IntegerField()),
                ('n_id', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customercare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complain', models.TextField(max_length=1000)),
                ('Options', models.CharField(choices=[('Complain against Driver', 'Complain against Driver'), ('Complain against BUS Service', 'Complain against Bus Service'), ('Complain against Booking System', 'Complain against Booking System'), ('Facing other Problem', 'Facing other Problem')], default='Facing other Problem', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
