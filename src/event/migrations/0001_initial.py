# Generated by Django 2.2.4 on 2019-08-10 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_attendees', models.IntegerField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('schedule', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('invited_users', models.ManyToManyField(blank=True, related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('registered_users', models.ManyToManyField(blank=True, related_name='registered', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
