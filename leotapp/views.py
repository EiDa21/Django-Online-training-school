from django.shortcuts import render, redirect
from .models import Contact, Register


# Create your views here.
def home(request):
        if request.method == 'POST':
            Name = request.POST.get("Name")
            Email =request.POST.get("Email")
            Message = request.POST.get("Message")
            contacts = Contact(Name = Name,  Email = Email, Message = Message )
            contacts.save()
            # messages.success(request, "Message saved Successfully, thank you! ")

        return render(request, "leotapp/index.html", {})
        

def phonereg(request):
        if request.method == 'POST':
            name = request.POST.get("Name")
            email =request.POST.get("Email")
            phone_number = request.POST.get("Message")
            courses = request.POST.get("courses")
            register = Register(name = name,  email = email, phone_number = phone_number, courses = courses)
            register.save()    
            return redirect("leotapp:home")

