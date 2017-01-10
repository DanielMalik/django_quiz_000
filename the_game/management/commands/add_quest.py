from django.core.management import BaseCommand
from django.utils import timezone
from the_game.models import Question, Category


def add_question():
    Question.objects.update_or_create(query='pytanie pytanie pytanie 3', answer='odp3',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 4', answer='odp4',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 5', answer='odp5',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 6', answer='odp6',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 7', answer='odp7',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 8', answer='odp8',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)
    Question.objects.update_or_create(query='pytanie pytanie pytanie 9', answer='odp9',
                                      comment='comment comment comment',
                                      category=Category.objects.get(pk=1), grade=0)





class Command(BaseCommand):
    help = 'Initialize database'

    def add_arguments(self, parser):
        parser.add_argument('--add-q',
                            action='store_true',
                            dest='add-bands',
                            default=False,
                            help='Insert band data')


    def handle(self, *args, **options):
        start = timezone.now()


        add_question()


        end = timezone.now()
        print(end - start)

