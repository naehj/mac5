# Generated by Django 2.1.5 on 2019-02-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_auto_20190208_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='contactpage.Contact'),
        ),
    ]
