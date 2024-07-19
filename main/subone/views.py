from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .models import TextEditor, MainBanner, MainBannerResponsive,Notification, Contact, PrivacyPolicy, Stat, TeacherTestimonial, Branch, BranchesCtg, Course , Instructor, Blog, BlogCtg,TeachingStaff, Department, Success_story, Career, CareerCtg, NumbersData, StudentTestimonials, AchieversBanner, AchieversBannerResponsive,CourseNotification, CareersForm, CoursessForm, ContactForm, Video, VidGallery, Image, ImgGallery, ManagementStaff, NonTeachingStaff, Batches, BatchesCtg, MainCategory
from .serializers import TextEditorSerializer, BannerSerializer, BannerResponsiveSerializer, NotificationSerializer, ContactSerializer, PrivacyPolicySerializer, StatSerializer, TeacherTestimonialSerializer, BranchesCtgSerializer, BranchSerializer, CourseSerializer, InstructorSerializer, BlogCtgSerializer,CourseNotificationSerializer, BlogSerializer, TeachingStaffSerializer, DepartmentSerializer, Success_storySerializer, CareerCtgSerializer, CareerSerializer,ManagementStaffSerializer, NonTeachingStaffSerializer,TheNumbersSerializer, AchieversBannerSerializer,AchieversBannerResponsiveSerializer, StudentTestiomoialsSerializer, ContactFormSerializer, CareerFormSerializer, CourseFormSerializer, ImageSerializer, ImgGallerySerializer, VideoSerializer, VideoGallerySerializer, BatchesSerializer, BatchesCtgSerializer, MainCategorySerializer


def home(request):
    banners = MainBanner.objects.all()
    notifications = Notification.objects.all()
    context = {'banners':banners, 'notifications':notifications}
    return render(request, 'home.html', context)    


@api_view(['GET'])
def TextEditor_api(request):
    banners = TextEditor.objects.all()
    serializer = TextEditorSerializer(banners, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Banners_api(request):
    banners = MainBanner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def BannersResponsive_api(request):
    banner = MainBannerResponsive.objects.all()
    serializer = BannerResponsiveSerializer(banner, many=True)
    return Response(serializer.data)  


@api_view(['GET'])
def Notification_api(request):
    notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Contact_api(request):
    contactus = Contact.objects.all()
    serializer = ContactSerializer(contactus, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def PrivacyPolicy_api(request):
    content = PrivacyPolicy.objects.all()
    serializer = PrivacyPolicySerializer(content, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Stat_api(request):
    stat = Stat.objects.all()
    serializer = StatSerializer(stat, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def TeacherTestimonial_api(request):
    testimonial = TeacherTestimonial.objects.all()
    serializer = TeacherTestimonialSerializer(testimonial, many=True)
    return Response(serializer.data)   



@api_view(['GET'])
def Branches_api(request):
    branches = Branch.objects.all()
    serializer = BranchSerializer(branches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Branches_detail_api(request, id):
    branches = BranchesCtg.objects.get(id=id)
    serializer = BranchesCtgSerializer(branches)
    return Response(serializer.data)  

    
@api_view(['GET'])
def BranchesCatg_api(request):
    branchctg = BranchesCtg.objects.all()
    serializer = BranchesCtgSerializer(branchctg, many=True)
    return Response(serializer.data)   


@api_view(['GET', 'POST'])
def Course_api(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)   



@api_view(['GET', 'POST'])
def Instructor_api(request):
    instructor = Instructor.objects.all()
    serializer = InstructorSerializer(instructor, many=True)
    return Response(serializer.data)   


@api_view(['GET'])
def Blog_api(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BlogCatg_api(request):
    blogctg = BlogCtg.objects.all()
    serializer = BlogCtgSerializer(blogctg, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Blog_detail_api(request, id):
    blog = Blog.objects.get(id=id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['GET'])
def TeachingStaff_api(request):
    staffs = TeachingStaff.objects.all()
    serializer = TeachingStaffSerializer(staffs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ManagementStaff_api(request):
    staffs = ManagementStaff.objects.all()
    serializer = ManagementStaffSerializer(staffs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def NonTeachingStaff_api(request):
    staffs = NonTeachingStaff.objects.all()
    serializer = NonTeachingStaffSerializer(staffs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Department_api(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Success_story_api(request):
    success_stories = Success_story.objects.all()
    serializer = Success_storySerializer(success_stories, many=True)
    return Response(serializer.data)


@api_view(['GET'])    
def Career_api(request):
    careers = Career.objects.all()
    serializer = CareerSerializer(careers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Career_Detail_api(request, id):
    careers = Career.objects.get(id=id)
    serializer = CareerSerializer(careers)
    return Response(serializer.data)

@api_view(['GET'])
def CareerCatg_api(request):
    careerctg = CareerCtg.objects.all()
    serializer = CareerCtgSerializer(careerctg, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def TheNumbers_api(request):
    numbers = NumbersData.objects.all()
    serializer = TheNumbersSerializer(numbers, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def AchieversBanner_api(request):
    banners = AchieversBanner.objects.all()
    serializer = AchieversBannerSerializer(banners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def AchieversBannerResponsive_api(request):
    banners = AchieversBannerResponsive.objects.all()
    serializer = AchieversBannerResponsiveSerializer(banners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CourseNotification_api(request):
    banners = CourseNotification.objects.all()
    serializer = CourseNotificationSerializer(banners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def StudentTestimonails_api(request):
    testimonials = StudentTestimonials.objects.all()
    serializer = StudentTestiomoialsSerializer(testimonials, many=True)
    return Response(serializer.data)



# Post Method
@api_view(['GET','POST'])
def ContactForm_Create(request):
    if request.method == "GET":
        formdata = ContactForm.objects.all()
        serializer = ContactFormSerializer(formdata, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# Post Method
@api_view(['GET','POST'])
def CourseForm_Create(request):
    if request.method == "GET":
        formdata = CoursessForm.objects.all()
        serializer = CourseFormSerializer(formdata, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CourseFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


# Post Method
@api_view(['GET','POST'])
def CareerForm_Create(request):
    if request.method == "GET":
        formdata = CareersForm.objects.all()
        serializer = CareerFormSerializer(formdata, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CareerFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def Image_api(request):
    img = Image.objects.all()
    serializer = ImageSerializer(img, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ImgGallery_api(request):
    gallery = ImgGallery.objects.all()
    serializer = ImgGallerySerializer(gallery, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def Video_api(request):
    video = Video.objects.all()
    serializer = VideoSerializer(video, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def VidGallery_api(request):
    vgallery = VidGallery.objects.all()
    serializer = VideoGallerySerializer(vgallery, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def Batches_api(request):
    batches = Batches.objects.all()
    serializer = BatchesSerializer(batches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Batches_detail_api(request, id):
    batches = Batches.objects.get(id=id)
    serializer = BatchesCtgSerializer(batches)
    return Response(serializer.data)  

    
@api_view(['GET'])
def BatchesCtg_api(request):
    batchctg = BatchesCtg.objects.all()
    serializer = BatchesCtgSerializer(batchctg, many=True)
    return Response(serializer.data)   

@api_view(['GET'])
def MainCategory_api(request):
    main_category = MainCategory.objects.all()
    serializer = MainCategorySerializer(main_category, many=True)
    return Response(serializer.data)   