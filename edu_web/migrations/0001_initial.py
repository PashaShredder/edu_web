# Generated by Django 4.1.3 on 2022-11-21 14:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('phone_number', models.CharField(help_text='Формат ввода номера +7', max_length=16, validators=[django.core.validators.RegexValidator('^\\+?7?\\d{9,15}$', 'Номер телефона необходимо вводить в формате «+7------». Допускается до 15 цифр')])),
                ('mail_address', models.EmailField(blank=True, max_length=254)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='curator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dir', models.CharField(max_length=150, verbose_name='Направление')),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Direction', to='edu_web.curator')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dis', models.CharField(max_length=150)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline', to='edu_web.direction')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('num_groups', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]*$', 'Разрешены только буквенно-цифровые символы')])),
                ('max_number_students', models.IntegerField(default=20, help_text='Количество студентов в группе не может быть меньше 1-го и больше 20-ти', validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='edu_web.curator')),
                ('disciplines', models.ManyToManyField(related_name='groups', to='edu_web.discipline', verbose_name='Изучаемые дисциплины')),
            ],
        ),
        migrations.CreateModel(
            name='MyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=150, verbose_name='Имя отчёта')),
                ('datatime_created', models.DateTimeField(auto_now_add=True)),
                ('rep_status', models.IntegerField(choices=[(0, 'not_started'), (1, 'during'), (2, 'done')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='None', max_length=1, verbose_name='Пол')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='edu_web.groups')),
            ],
        ),
    ]
