# Generated by Django 2.1.5 on 2019-02-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFields',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500, verbose_name='Your Name *')),
                ('email', models.EmailField(max_length=254, verbose_name='Your Email Address *')),
                ('phonenumber', models.PositiveIntegerField(blank=True, verbose_name='Your Phone Number (optional)')),
                ('website', models.URLField(blank=True, verbose_name='Your Web Site (optional)')),
                ('message', models.TextField(verbose_name='Your Message *')),
            ],
        ),
    ]
