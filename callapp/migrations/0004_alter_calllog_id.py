# Generated by Django 4.1.3 on 2023-02-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callapp', '0003_alter_calllog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calllog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]