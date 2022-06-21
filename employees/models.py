from django.db import models


class Employees(models.Model):
    full_name = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    cat = models.ForeignKey('Category', related_name='employees', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    position = models.CharField(max_length=50)
    boss_id = models.IntegerField(null=True)

    def __str__(self):
        return self.position

