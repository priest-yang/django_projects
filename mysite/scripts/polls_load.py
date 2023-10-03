import csv  # https://docs.python.org/3/library/csv.html

from polls.models import Question, Choice
from django.utils import timezone

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:

        print(row)
        if len(row) < 2: continue
        q = Question(question_text=row[0], pub_date=timezone.now())
        q.save()

        for i in range(1, len(row)):
            c = Choice(question=q, choice_text=row[i], votes=0)
            c.save()
        
        
        

        # Make a new Question and save it

        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it

    print("=== Load Complete")