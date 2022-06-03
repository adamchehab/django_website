from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note


def index(request):
    context = {
        "title": "Main page",
    }
    return render(request, "main/index.html", context)


def notes(request):
    # NOTE - this is list
    # all/order by
    # notes = Note.objects.order_by("-id")[:1]
    notes = Note.objects.order_by("id")
    context = {
        "title": "Notes",
        "notes": notes,
    }
    return render(request, "main/notes.html", context)


def add_note(request):
    error = ""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes")
        else:
            error = "Invalid form"

    form = NoteForm()
    context = {
        "form": form,
        "error": error,
        "title": "Add note",
    }
    return render(request, "main/add.html", context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, "main/about.html", context)


# Q admin panel Question
def empty(request):
    return None
