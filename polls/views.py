from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from .forms import CommentForm  # NEW

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # NEW: provide empty comment form on GET detail page
    form = CommentForm()
    return render(request, "polls/detail.html", {"question": question, "form": form})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice.", "form": CommentForm()},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# NEW anonymous comment submission
def post_comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            question.comments.create(text=form.cleaned_data["text"])
            return redirect("polls:detail", question_id=question.id)  # PRG pattern
    else:
        form = CommentForm()
    return render(request, "polls/detail.html", {"question": question, "form": form})