from django.db import models



class Quiz(models.Model):
    Question=models.CharField(max_length=200)
    op1     =models.CharField(max_length=200)
    op2     =models.CharField(max_length=200)
    op3     =models.CharField(max_length=200)
    op4     =models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    Answer  =models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Question