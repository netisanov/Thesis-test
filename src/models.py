from django.db import models


class Employee(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/employees/photos', null=True, blank=True)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(decimal_places=2, max_digits=12)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='employees')

    # Я бы выделил позиции в отдельную модель, но зависит от требований бизнеса
    position = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', ]),
        ]

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.surname}'


class Department(models.Model):
    title = models.CharField(max_length=50)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='manager')

    def __str__(self):
        return self.title
