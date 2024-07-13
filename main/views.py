from django.shortcuts import render, redirect
from .models import Message, TopBooks
from django.contrib import messages


# bosh sahifa
def index(request):

    books = TopBooks.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Message.objects.create(name=name, email=email, message=message)
        messages.success(request, "Xabar muvaffaqiyatli yuborildi")
        return redirect("index")

    context = {
        "books": books,
    }
    return render(request=request, template_name="index.html", context=context)
