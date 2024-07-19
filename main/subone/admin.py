from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TextEditor, MainBanner,MainBannerResponsive, CourseNotification,Notification, Contact, PrivacyPolicy,ManagementStaff, Stat, TeacherTestimonial, BranchesCtg, Branch, Course, Instructor, BlogCtg, Blog, TeachingStaff,NonTeachingStaff, Success_story, Department, CareerCtg, Career, AchieversBanner,AchieversBannerResponsive, NumbersData, StudentTestimonials, ContactForm, CoursessForm, CareersForm, Image, ImgGallery, Video, VidGallery, Batches, BatchesCtg, MainCategory, SubCategory, Category, Sections
# Register your models here.
from tinymce.widgets import TinyMCE
from django.db import models

class TinyMCEAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
	}

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(TextEditor, PostAdmin)
admin.site.register(MainBanner)
admin.site.register(MainBannerResponsive)
admin.site.register(Notification)
admin.site.register(Contact)
admin.site.register(PrivacyPolicy, TinyMCEAdmin)
admin.site.register(Stat)
admin.site.register(TeacherTestimonial)
admin.site.register(Branch)
admin.site.register(BranchesCtg)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Blog, TinyMCEAdmin)
admin.site.register(BlogCtg)
admin.site.register(TeachingStaff)
admin.site.register(Department)
admin.site.register(Success_story)
admin.site.register(Career)
admin.site.register(CareerCtg)
admin.site.register(AchieversBanner)
admin.site.register(AchieversBannerResponsive)
admin.site.register(StudentTestimonials)
admin.site.register(NumbersData)
admin.site.register(ContactForm)
admin.site.register(CoursessForm)
admin.site.register(CareersForm)
admin.site.register(ImgGallery)
admin.site.register(Image)
admin.site.register(VidGallery)
admin.site.register(Video)
admin.site.register(ManagementStaff)
admin.site.register(NonTeachingStaff)
admin.site.register(BatchesCtg)
admin.site.register(Batches, TinyMCEAdmin)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sections, TinyMCEAdmin)
admin.site.register(CourseNotification)
# #Course
