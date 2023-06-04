# Generated by Django 4.2.1 on 2023-06-02 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id_events', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('date_creation', models.DateTimeField()),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
