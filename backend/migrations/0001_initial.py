# Generated by Django 5.1.2 on 2024-10-26 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicoEspecialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('idade', models.PositiveIntegerField()),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=50, null=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('rg', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('nome_responsavel', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone_responsavel', models.CharField(blank=True, max_length=20, null=True)),
                ('grau_parentesco', models.CharField(blank=True, max_length=100, null=True)),
                ('doencas_cronicas', models.TextField(blank=True, null=True)),
                ('alergias', models.TextField(blank=True, null=True)),
                ('medicamentos', models.TextField(blank=True, null=True)),
                ('cirurgias', models.TextField(blank=True, null=True)),
                ('historico_internacoes', models.TextField(blank=True, null=True)),
                ('vacinas', models.TextField(blank=True, null=True)),
                ('exames', models.TextField(blank=True, null=True)),
                ('condicoes_cognitivas', models.TextField(blank=True, null=True)),
                ('alteracoes_humor', models.TextField(blank=True, null=True)),
                ('comportamento_social', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('crm', models.CharField(max_length=10)),
                ('data_de_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('especialidades', models.ManyToManyField(to='backend.medicoespecialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateField(auto_now_add=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('tratamento_recomendado', models.TextField(blank=True, null=True)),
                ('exames_solicitados', models.TextField(blank=True, null=True)),
                ('medicamentos_prescritos', models.TextField(blank=True, null=True)),
                ('encaminhamentos', models.TextField(blank=True, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.paciente')),
            ],
        ),
    ]
