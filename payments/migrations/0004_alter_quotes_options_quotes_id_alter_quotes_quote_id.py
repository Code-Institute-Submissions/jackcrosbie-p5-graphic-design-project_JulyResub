# Generated by Django 4.0.4 on 2022-05-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_remove_quotes_id_quotes_quote_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotes',
            options={'verbose_name_plural': 'Quotes'},
        ),
        migrations.AddField(
            model_name='quotes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotes',
            name='quote_id',
            field=models.CharField(default='', editable=False, max_length=32),
        ),
    ]
