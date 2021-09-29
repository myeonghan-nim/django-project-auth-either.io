from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from .forms import QuestionForm, ChoiceForm
from .models import Question, Choice


def index(request):
    context = {
        'questions': Question.objects.all(),
    }
    return render(request, 'question/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
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
        'choice_form': ChoiceForm(),
        'percent_1': percent_1,
        'percent_2': percent_2,
    }

    return render(request, 'question/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question:index')
    else:
        form = QuestionForm()

    context = {
        'form': form,
    }

    return render(request, 'question/form.html', context)


@login_required
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


@login_required
def delete(request, question_id):
    if request.method == 'POST':
        get_object_or_404(Question, id=question_id).delete()
        return redirect('question:index')
    else:
        return redirect('question:detail', question_id)


@login_required
@require_POST
def choice_create(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choice_form = ChoiceForm(request.POST)

    if choice_form.is_valid():
        choice = choice_form.save(commit=False)
        choice.question = question
        choice.save()

    return redirect('question:detail', question_id)


@login_required
@require_POST
def choice_delete(request, question_id, choice_id):
    get_object_or_404(Choice, id=choice_id).delete()
    return redirect('question:detail', question_id)
