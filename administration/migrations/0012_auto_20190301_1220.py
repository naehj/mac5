# Generated by Django 2.1.5 on 2019-03-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0011_auto_20190301_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sobrenome *'),
        ),
    ]
