# Generated by Django 4.0.4 on 2022-05-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='project_type',
            field=models.CharField(choices=[('custom', 'Custom'), ('website design', 'Website Design'), ('Maintenance', 'Maintenace'), ('Urgent Repair', 'Urgent Repair')], default='custom', max_length=20),
        ),
    ]
