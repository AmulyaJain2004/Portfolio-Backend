from django.contrib import admin
from .models import Project, Message, BlogPost, Skill, Certification, DailyLog, Education, Experience, MainCategory, SubCategory

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category', 'subcategory', 'proficiency')
    search_fields = ('name',)
    list_filter = ('main_category', 'subcategory', 'proficiency')
    raw_id_fields = ('main_category', 'subcategory')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'demo_link', 'featured')
    search_fields = ('title', 'tech_stack')
    list_filter = ('tech_stack', 'featured')
    ordering = ('title',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_published', 'link')
    search_fields = ('title', 'content')
    list_filter = ('is_published',)
    ordering = ('-published_at',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date_obtained')
    search_fields = ('name', 'issuer')
    list_filter = ('issuer',)
    ordering = ('-date_obtained',)

@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'activities')
    search_fields = ('activities', 'notes')
    ordering = ('-date',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')
    search_fields = ('degree', 'institution')
    list_filter = ('institution',)
    ordering = ('-start_year',)
    fieldsets = (
        (None, {'fields': ('degree', 'institution')}),
        ('Years', {'fields': ('start_year', 'end_year')}),
        ('Description', {'fields': ('description',)}),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date')
    search_fields = ('title', 'organization')
    list_filter = ('organization',)
    ordering = ('-start_date',)
    fieldsets = (
        (None, {'fields': ('title', 'organization')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
        ('Description', {'fields': ('description',)}),
    )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-created_at',)