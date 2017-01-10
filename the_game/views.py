from django.views import View
from django.shortcuts import render
from random import randint
from django.http.response import HttpResponse
from the_game.models import Question, Category, GRADE
from the_game.forms import AnswerForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
qqnt =len(Question.objects.all()) # number of all records in questions table
already_asked = list()

def ask():
    id = randint(1, qqnt)
    if id not in already_asked:
        to_ask = Question.objects.get(pk=id)
        #print(to_ask)
        already_asked.append(id)
        print(already_asked)

        qta= {'question': to_ask.query, 'category': to_ask.category, 'answer': to_ask.answer, 'comment': to_ask.comment }
        #print(ctx)
        return qta
    else:
        if len(already_asked) == qqnt:
            out = '''<html>
            <body>
                <h1>Out of questions</h1>
            </body>
        </html>
    '''
            return HttpResponse(out)
        else:
            ask()

# @csrf_exempt
class Stage_One(View):
    count = 0
    def get(self, request):
        form = AnswerForm()
        will_ask = ask()
        #print(will_ask)
        ctx = {'form': form, 'will_ask': will_ask}
        print(ctx)

        return render(request, "game_templates/stage_one.html", ctx)




