# Generated by Django 4.1.3 on 2023-02-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calllog',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]