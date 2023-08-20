from django.shortcuts import render
from .models import *
from myportfolio.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    hero = Hero.objects.first()
    roles = hero.get_roles()
    aboutme = Aboutme.objects.get(hero=hero)
    skills = Skill.objects.filter(hero=hero)
    resumes = Resume.objects.filter(hero=hero)
    projects=Project.objects.all()

    context = {'hero':hero, 'roles':roles, 'aboutme':aboutme, 'skills':skills, 'resumes':resumes, 'projects':projects}

    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = "New email"
        recipient = "techhyinfo@yopmail.com","np03cs4s220196@heraldcollege.edu.np"

        html_content = render_to_string('portfolio/email.html',{'name':name,'description':message,'mail':email})
        email=EmailMessage(
               subject,
               html_content,
               EMAIL_HOST_USER,
               recipient
        )

        email.fail_silently=False
        if email!=None:
            email.send()

        contact = Contact(
            name=name,
            email=email,
            message=message
        )
        contact.save()

    return render(request, "portfolio/index.html",context)

def aboutme(request):
    return render(request,"portfolio/about.html")

