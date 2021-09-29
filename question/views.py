from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'question/index.html', context)


def detail(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    choice_form = ChoiceForm()

    choices = question.choice_set.all()

    total_1 = choices.filter(pick=1).count()
    total_2 = choices.filter(pick=2).count()
    total_sum = total_1 + total_2

    if total_sum != 0:
        percent_1 = round(total_1 / total_sum * 100, 2)
        percent_2 = round(total_2 / total_sum * 100, 2)
    else:
        percent_1, percent_2 = 0, 0

    context = {
        'question': question,
        'choice_form': choice_form,
        'percent_1': percent_1,
        'percent_2': percent_2,
    }

    return render(request, 'question/detail.html', context)


@login_required
def create(request):

    # 1. user request GET for input datas(request form)
    # 6. user request POST after inputted not corrext datas
    # 12. user request POST after inputted correct datas

    # 7 & 13. if request is POST
    if request.method == 'POST':
        # 8 & 14. make form instance with inputted data
        form = QuestionForm(request.POST)

        # 9 & 15. check datas are right
        if form.is_valid():
            # 16. if datas are correct, save datas to DB
            form.save()

            # 17. redirect main index page
            return redirect('question:index')
    # 2. if request is GET
    else:
        # 3. save empty ModelForm to variable(form) for return to user
        form = QuestionForm()

    # 4. set dict for return form
    # 10. if datas are not right, return form filled correct inputted datas
    context = {
        'form': form,
    }

    # 5. return form.html
    # 11. return form.html
    return render(request, 'question/form.html', context)


def update(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            form.save()

            return redirect('question:detail', question_id)
    else:
        form = QuestionForm(instance=question)

    context = {
        'form': form,
    }

    return render(request, 'question/form.html', context)


def delete(request, question_id):

    if request.method == 'POST':
        get_object_or_404(Question, id=question_id).delete()

        return redirect('question:index')
    else:

        return redirect('question:detail', question_id)


@require_POST
def choice_create(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    choice_form = ChoiceForm(request.POST)

    if choice_form.is_valid():

        choice = choice_form.save(commit=False)
        choice.question = question
        choice.save()

    return redirect('question:detail', question_id)


@require_POST
def choice_delete(request, question_id, choice_id):

    get_object_or_404(Choice, id=choice_id).delete()

    return redirect('question:detail', question_id)
