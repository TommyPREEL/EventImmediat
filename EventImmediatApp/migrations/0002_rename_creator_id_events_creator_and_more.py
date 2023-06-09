# Generated by Django 4.2.1 on 2023-06-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventImmediatApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.AlterField(
            model_name='events',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='date_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='date_start',
            field=models.DateField(),
        ),
    ]
