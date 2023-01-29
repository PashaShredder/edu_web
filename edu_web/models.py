from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

NUMBER_REGEX = RegexValidator(r'^[a-zA-Z0-9]*$', 'Разрешены только буквенно-цифровые символы')
PHONE_REGEX = RegexValidator(r'^\+?7?\d{9,15}$', "Номер телефона необходимо вводить в формате "
                                                 "«+3------». Допускается до 15 цифр")


class Curator(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
    )
    middle_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Отчество',
    )
    phone_number = models.CharField(
        max_length=16,
        blank=False,
        null=False,
        validators=[PHONE_REGEX],
        help_text='Формат ввода номера +3',
        verbose_name='Телефон куратора'

    )
    mail_address = models.EmailField(
        blank=True,
        verbose_name='Электронная почта куратора'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='curatoruser',
        blank=True,
        verbose_name='Пользователь'
    )
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Direction(models.Model):
    name_dir = models.CharField(
        max_length=150,
        verbose_name='Направление подготовки',
    )
    curator = models.ForeignKey(
        Curator,
        related_name='curatordirections',
        on_delete=models.CASCADE,
        verbose_name='Куратор направления',
    )

    def __str__(self):
        return f'{self.name_dir}'


class Groups(models.Model):
    group_name = models.CharField(
        max_length=150,
        verbose_name='Шыфр группы',
    )
    group_number = models.CharField(
        max_length=15,
        validators=[NUMBER_REGEX],
        verbose_name='№ группы'
    )
    max_number_students = models.IntegerField(
        default=20,
        validators=[MaxValueValidator(20), MinValueValidator(1)],
        help_text='Количество студентов в группе '
                  'не может быть меньше 1-го и больше 20-ти',
        verbose_name='Максимальное наполнение группы'
    )

    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='group',
        verbose_name='Изучаемые дисциплины',
    )



    def __str__(self):
        return self.group_name



class Students(models.Model):
    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
    ]
    first_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
    )
    middle_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Отчество',
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        verbose_name='Пол',
    )
    group = models.ForeignKey(
        Groups,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Группа студента'
    )

    class Meta:
        ordering = ['first_name', ]
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Discipline(models.Model):
    name_dis = models.CharField(
        max_length=150,
        verbose_name='Название дисциплины'
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='directiondisciplines',
        verbose_name='Направление подготовки'

    )

    def __str__(self):
        return f'{self.name_dis}'


