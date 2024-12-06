from django.shortcuts import render, redirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return render(request, "website/contact.html", {"form": form})
        else:
            messages.error(
                request, "There was an error sending your message. Please try again."
            )
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = NewsletterForm()

    return render(request, "website/newsletter.html", {"form": form})
