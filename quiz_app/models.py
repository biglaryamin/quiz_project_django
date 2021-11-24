from django.db import models


class Category(models.Model):
    Title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Title


class Quiz(models.Model):
    Question=models.TextField(max_length=200)
    op1     =models.CharField(max_length=200)
    op2     =models.CharField(max_length=200)
    op3     =models.CharField(max_length=200)
    op4     =models.CharField(max_length=200)
    Category=models.ManyToManyField(Category)
    Answer  =models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Question

