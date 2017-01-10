from django.db import models

# Create your models here.
GRADE = (
    (0, 'easy'),
    (1, 'normal'),
    (2, 'hard'),
    (3, 'unfair')
)

class Question(models.Model):
    query = models.TextField(max_length=512)
    answer = models.CharField(max_length=128,)
    comment = models.TextField(max_length=512, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    grade = models.IntegerField(choices=GRADE, default=0)

    def __str__(self):
        return self.query[0:30]

class Category(models.Model):
    cat_name = models.CharField(max_length=128,)

    def __str__(self):
        return self.cat_name