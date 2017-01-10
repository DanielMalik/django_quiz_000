from django.contrib import admin
from the_game.models import Question, Category

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( "query", "category", "grade", "query", "comment", "answer")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("cat_name", )