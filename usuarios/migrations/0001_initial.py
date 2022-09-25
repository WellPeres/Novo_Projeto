# Generated by Django 4.1.1 on 2022-09-25 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('computadores', '0002_alter_maquinas_status'),
        ('monitores', '0002_monitor_marca_monitor2_monitor_modelo2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrato', models.CharField(choices=[('CLT', 'CLT'), ('PJ', 'Pessoa Juridica'), ('EST', 'Estágiario')], default='CLT', max_length=3)),
                ('computador', models.CharField(choices=[('PCP', 'Desktop'), ('NOT', 'Notebook'), ('PTC', 'Particular')], default='PCP', max_length=3)),
                ('nome', models.CharField(max_length=50)),
                ('user_login', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('setor', models.CharField(max_length=30)),
                ('equipamento_em_uso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='computadores.maquinas', verbose_name='Equipamento')),
                ('monitor_em_uso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='Monitor_Estoque', to='monitores.monitor', verbose_name='Monitores')),
            ],
        ),
    ]