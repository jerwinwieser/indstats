# Generated by Django 4.1.4 on 2022-12-16 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_application_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='submitdate',
            new_name='submit_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='updated_at',
        ),
    ]
