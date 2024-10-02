from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class CatBreed(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название породы', unique=True)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=150, unique=False, verbose_name='Кличка')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Хозяин')
    breed = models.ForeignKey('CatBreed', verbose_name='Порода', on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст в месяцах', null=False)
    color = models.CharField(verbose_name='Цвет', null=False, max_length=30)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return str(self.name) + ' ' + str(self.age)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey('Cat', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, 'Bad'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'),
                                          (5, 'Excellent')], default=3, verbose_name='Оценка')

    def average_rate(self):
        raise ValueError("The average_rate attribute is only accessible if the queryset is annotated")


