# Generated by Django 2.1.5 on 2019-03-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicespage', '0014_auto_20190212_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(blank=True, choices=[('Serviços de Contabilidade', 'Serviços de Contabilidade'), ('Conciliação Bancária', 'Conciliação Bancária'), ('Meios de Pagamento', 'Meios de Pagamento'), ('Automação Comercial', 'Automação Comercial'), ('Seguros', 'Seguros'), ('Telefonia', 'Telefonia')], max_length=500, null=True, verbose_name='Category of the service *'),
        ),
    ]
