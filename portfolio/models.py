from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()


    def get_roles(self):
        return self.roles.split(',')

    def __str__(self):
        return self.name
    
class Aboutme(models.Model):
    hero = models.OneToOneField(Hero, null=True, on_delete=models.CASCADE)
    email = models.EmailField()
    job = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"About Me for {self.hero.name}"
    
class Skill(models.Model):
    hero = models.ManyToManyField(Hero)
    skillname = models.CharField(max_length=100)
    level = models.IntegerField()
    def __str__(self):
        return f"{self.skillname}"
    
class Resume(models.Model):
    hero = models.ManyToManyField(Hero)
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.title}"

class Project(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    cover_image = models.FileField(upload_to='project-image')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name
