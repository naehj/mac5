# Generated by Django 2.1.5 on 2019-02-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0006_auto_20190213_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='neighbourhood',
            field=models.CharField(max_length=500, verbose_name='CEP *'),
        ),
    ]
