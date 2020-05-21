# Generated by Django 2.2.12 on 2020-05-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_domain_hsts_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhook',
            name='url',
            field=models.URLField(help_text='URL to send the webhook to', max_length=600),
        ),
    ]