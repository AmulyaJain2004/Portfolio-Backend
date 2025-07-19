from rest_framework import generics
from .models import Project, Message, BlogPost, Skill, Certification, DailyLog, Education, Experience, MainCategory, SubCategory
from .serializers import ProjectSerializer, MessageSerializer, BlogPostSerializer, SkillSerializer, CertificationSerializer, DailyLogSerializer, EducationSerializer, ExperienceSerializer, MainCategorySerializer, SubCategorySerializer
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        # Send email notification
        send_mail(
            subject=f"New Contact Message from {message.name}",
            message=f"Name: {message.name}\nEmail: {message.email}\n\nMessage:\n{message.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFICATION_EMAIL],
            fail_silently=False,
        )

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CertificationListView(generics.ListAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class DailyLogListView(generics.ListAPIView):
    queryset = DailyLog.objects.all().order_by('-date')
    serializer_class = DailyLogSerializer

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all().order_by('-start_year')
    serializer_class = EducationSerializer

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by('-start_date')
    serializer_class = ExperienceSerializer
