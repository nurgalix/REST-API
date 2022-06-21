# Generated by Django 4.0.5 on 2022-06-20 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='boss_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.category'),
        ),
    ]