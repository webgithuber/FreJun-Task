# Generated by Django 4.1.3 on 2023-02-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callapp', '0007_alter_calllog_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calllog',
            old_name='submitted_time',
            new_name='calling_time',
        ),
    ]
