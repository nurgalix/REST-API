# Generated by Django 4.0.5 on 2022-06-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_category_boss_id_employees_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='mentor',
        ),
    ]