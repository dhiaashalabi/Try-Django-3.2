# Generated by Django 3.2.7 on 2021-09-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='prev_status',
            field=models.CharField(choices=[('p', 'Pending'), ('c', 'Completed'), ('e', 'Expired'), ('a', 'Aborted')], default=None, max_length=1, null=True),
        ),
    ]