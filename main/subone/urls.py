from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # API ROUTES starts here 
    path('TextEditor_api', views.TextEditor_api, name='TextEditor_api'),
    path('Banners_api', views.Banners_api, name='Banners_api'),
    path('BannersResponsive_api', views.BannersResponsive_api, name='BannersResponsive_api'),
    path('Notification_api', views.Notification_api, name='Notification_api'),
    path('Contact_api', views.Contact_api, name='Contact_api'),
    path('PrivacyPolicy_api', views.PrivacyPolicy_api, name='PrivacyPolicy_api'),
    path('Stat_api', views.Stat_api, name='Stat_api'),
    path('TeacherTestimonial_api', views.TeacherTestimonial_api, name='TeacherTestimonial_api'),
    path('Branches_api', views.Branches_api, name='Branches_api'),
    path('BranchesCatg_api', views.BranchesCatg_api, name='BranchesCatg_api'),
    path('Branches_api/<int:id>/', views.Branches_detail_api, name='Branches_detail_api'),
    path('Course_api', views.Course_api, name='Course_api'),
    path('Instructor_api', views.Instructor_api, name='Instructor_api'),
    path('Blog_api', views.Blog_api, name='Blog_api'),
    path('BlogCatg_api', views.BlogCatg_api, name='BlogCatg_api'),
    path('TeachingStaff_api', views.TeachingStaff_api, name='TeachingStaff_api'),
    path('ManagementStaff_api', views.ManagementStaff_api, name='ManagementStaff_api'),
    path('NonTeachingStaff_api', views.NonTeachingStaff_api, name='NonTeachingStaff_api'),
    path('Department_api', views.Department_api, name='Department_api'),
    path('Blog_api/<int:id>/', views.Blog_detail_api, name='Blog_detail_api'),
    path('Success_story_api', views.Success_story_api, name='Success_story_api'),
    path('Career_api', views.Career_api, name='Career_api'),
    path('CareerCatg_api', views.CareerCatg_api, name='CareerCatg_api'),
    path('Career_api/<int:id>/', views.Career_Detail_api, name='Career_Detail_api'),
    path('TheNumbers_api', views.TheNumbers_api, name='TheNumbers_api'),
    path('AchieversBanner_api', views.AchieversBanner_api, name='AchieversBanner_api'),
    path('AchieversBannerResponsive_api', views.AchieversBannerResponsive_api, name='AchieversBannerResponsive_api'),
    path('CourseNotification_api', views.CourseNotification_api, name='CourseNotification_api'),
    path('StudentTestimonails_api', views.StudentTestimonails_api, name='StudentTestimonails_api'),
    path('ContactForm_Create', views.ContactForm_Create, name='ContactForm_Create'),
    path('CourseForm_Create', views.CourseForm_Create, name='CourseForm_Create'),
    path('CareerForm_Create', views.CareerForm_Create, name='CareerForm_Create'),
    path('Image_api', views.Image_api, name='Image_api'),
    path('ImgGallery_api', views.ImgGallery_api, name='ImgGallery_api'),
    path('Video_api', views.Video_api, name='Video_api'),
    path('VidGallery_api', views.VidGallery_api, name='VidGallery_api'),

    path('Batches_api', views.Batches_api, name='Batches_api'),
    path('BatchesCtg_api', views.BatchesCtg_api, name='BatchesCtg_api'),
    path('Batches_detail_api/<int:id>/', views.Batches_detail_api, name='Batches_detail_api'),

    path('MainCategory_api', views.MainCategory_api, name='MainCategory_api'),
]

