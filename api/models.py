from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    tech_stack = models.CharField(max_length=200, null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    featured = models.BooleanField(default=False, help_text='Mark as featured to show on the home page')

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    cover_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True, help_text='Optional external link (e.g. LinkedIn article)')

    def __str__(self):
        return self.title

class MainCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='skills')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, related_name='skills', null=True, blank=True)
    doc_link = models.URLField(blank=True, null=True)
    icon_url = models.URLField(blank=True, null=True)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='beginner')

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_obtained = models.DateField()
    credential_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class DailyLog(models.Model):
    date = models.DateField()
    activities = models.TextField()
    new_things_tried = models.TextField()
    improvement = models.TextField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date}: {self.activities[:30]}..."

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} at {self.organization}"