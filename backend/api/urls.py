from django.urls import path
from .views import ProjectListView, MessageCreateView, BlogPostListView, BlogPostDetailView, SkillListView, CertificationListView, DailyLogListView, EducationListView, ExperienceListView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('messages/', MessageCreateView.as_view()),
    path('blog/', BlogPostListView.as_view()),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view()),
    path('skills/', SkillListView.as_view()),
    path('certifications/', CertificationListView.as_view()),
    path('daily-logs/', DailyLogListView.as_view()),
    path('education/', EducationListView.as_view()),
    path('experience/', ExperienceListView.as_view()),
]
