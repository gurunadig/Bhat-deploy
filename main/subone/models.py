from django.db import models
from django_summernote.fields import SummernoteTextField
from tinymce.models import HTMLField


class TextEditor(models.Model):
    desc = SummernoteTextField()

    def __str__(self):
        return self.desc 

#Banner Model
class MainBanner(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default="400-200.png", null=False, blank=True, upload_to='img_uploads/')
    description = models.TextField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True) 
    button_text = models.TextField()
    hyperLink = models.TextField(default="paste-link") 


    def __str__(self):
        return self.hyperLink 
    

#Banner Model
class MainBannerResponsive(models.Model):
    image = models.ImageField(default="400-200.png", null=False, blank=True, upload_to='img_uploads/')
    button_text = models.TextField()
    hyperLink = models.TextField(default="paste-link") 

    def __str__(self):
        return self.hyperLink 



#Notification Model
class Notification(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    description = models.TextField()
    hyperLink = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.title



#Contact Us Model
class Contact(models.Model):
    banner_image = models.ImageField(default="400-200.png", null=False, blank=True)
    email_id = models.EmailField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    location_url = models.TextField()
    location_image = models.ImageField(default="400-200.png", null=False, blank=True)
    
    def __str__(self):
        return self.phone_number


#Privacy Policy Model
class PrivacyPolicy(models.Model):
    banner_image = models.ImageField(default="400-200.png", null=False, blank=True)
    content = HTMLField()
    
    def __str__(self):
        return self.content



#Stats Model
class Stat(models.Model):
    number_of_students = models.PositiveIntegerField(blank=True, null=True)
    number_of_years = models.PositiveIntegerField(blank=True, null=True)
    number_of_teachers = models.PositiveIntegerField(blank=True, null=True)



#TeacherTestimonial Model
class TeacherTestimonial(models.Model):
    teacher_name = models.CharField(max_length=200, blank=True, null=True)
    testimonials_url = models.TextField()
    
    def __str__(self):
        return self.teacher_name




#Branch Category
class BranchesCtg(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title



#Branches
class Branch(models.Model):
    desc = models.TextField()
    number = models.IntegerField()
    address = models.CharField(max_length=300, blank=True, null=True)
    location_url =models.TextField()
    map_image = models.ImageField(default="400-200.png", null=False, blank=True)
    branch_ctg = models.ForeignKey(BranchesCtg, on_delete=models.CASCADE, related_name='branches')


    
    def __str__(self):
        return self.address


#Instructor
class Instructor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name



#ContactForm
class ContactForm(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email =  models.EmailField(max_length=200, blank=False, null=False)
    phoneNumber =  models.PositiveIntegerField(blank=False, null=False)
    message =  models.TextField(max_length=200, blank=False, null=False)
    
    def __str__(self):
        return self.name
    


class CoursessForm(models.Model):
    i_am = models.CharField(max_length=100, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    email =  models.EmailField(max_length=200, blank=False, null=False)
    phoneNumber =  models.PositiveIntegerField(blank=False, null=False)
    message =  models.TextField(max_length=200, blank=False, null=False)
    cat = models.CharField(max_length=100, blank=False, null=False)
    cour = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.name


class CareersForm(models.Model):
    file= models.FileField(upload_to= 'uploads/', blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    phone =  models.PositiveIntegerField(blank=False, null=False)
    email =  models.EmailField(max_length=200, blank=False, null=False)
    address =  models.TextField( blank=False, null=False)
    residentaddress1 =  models.TextField( blank=False, null=False)
    residentaddress2 = models.TextField( blank=False, null=False)
    job_title = models.CharField(max_length=100, blank=False, null=False)
    course_value = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.name

#Course
class Course(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return self.title
    
# courseNotification
class CourseNotification(models.Model):
    title = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title


#Blog Category
class BlogCtg(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title


#Blog 
class Blog(models.Model):
    desc = HTMLField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    blog_image = models.ImageField(default="400-200.png", null=False, blank=True)
    blog_ctg = models.ForeignKey(BlogCtg, on_delete=models.CASCADE, related_name='blogs')
   
    def __str__(self):
        return self.title


# management staff
class ManagementStaff(models.Model):
    management_image = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title


# teaching staff
class TeachingStaff(models.Model):
    staff_image = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title


#non-teaching staff
class NonTeachingStaff(models.Model):
    nonteaching_image = models.ImageField(default="400-200.png", null=False, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    
    def __str__(self):
        return self.title


#Instructor
class Department(models.Model):
    dept_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.dept_name



#Course
class Success_story(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    rank = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField()
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='success_story')

    def __str__(self):
        return self.name


#career Category
class CareerCtg(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title


#Career 
class Career(models.Model):
    title = models.CharField(max_length=200)
    job_desc = models.TextField()
    eligibility = models.TextField()
    no_of_openings =  models.CharField(max_length=50, blank=True, null=True)
    career_ctg = models.ForeignKey(CareerCtg, on_delete=models.CASCADE, related_name='careers')
    
    def __str__(self):
        return self.title


#AchieversBannerResponsive
class AchieversBannerResponsive(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="400-200.png", null=False, blank=True)

    def __str__(self):
        return self.title


#AchieversBanner
class AchieversBanner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="400-200.png", null=False, blank=True)

    def __str__(self):
        return self.title


#Numbers
class NumbersData(models.Model):
    text_value = models.CharField(max_length=200, blank=True, null=True)
    numbers = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.text_value)



#StudentTestimonials
class StudentTestimonials(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    class_of =  models.CharField(max_length=200, blank=True, null=True)
    testimonial =  models.TextField(blank=True, null=True)
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    
    def __str__(self):
        return self.name



class ImgGallery(models.Model):
    branch = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.branch



class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(default="400-200.png", null=False, blank=True)
    img_url = models.TextField()
    imggallery = models.ForeignKey(ImgGallery, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return self.title



class VidGallery(models.Model):
    branch = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.branch

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    vid_url = models.TextField()
    vidgallery = models.ForeignKey(VidGallery, on_delete=models.CASCADE, related_name='videos')
    
    def __str__(self):
        return self.title


#Branch Category
class BatchesCtg(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title


#Branches
class Batches(models.Model):
    batch_label = models.CharField(max_length=300, blank=True, null=True)
    batch_image = models.ImageField(default="400-200.png", null=False, blank=True)
    class_name = models.CharField(max_length=300, null=False, blank=True)
    day = models.CharField(max_length=300, blank=True, null=True)
    class_schedule =models.CharField(max_length=100, blank=True, null=True)
    course_fee = models.IntegerField(null=True, blank=True)
    class_desc = HTMLField()
    batches_ctg = models.ForeignKey(BatchesCtg, on_delete=models.CASCADE, related_name='batches')
    
    def __str__(self):
        return self.batch_label
    


class MainCategory(models.Model):
    name = models.CharField(max_length=255)
 
    def __str__(self):
        return self.name
 
class Category(models.Model):
    name = models.CharField(max_length=255)
    main_category = models.ForeignKey(MainCategory, related_name='categories', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
 
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
 
class Sections(models.Model):
    SECTION_TYPES = [
        ('Overview', 'Overview'),
        ('Batches', 'Batches'),
        ('Curriculum', 'Curriculum'),
        ('Instructor', 'Instructor')
    ]
   
    name = models.CharField(max_length=255, choices=SECTION_TYPES)
    sub_category = models.ForeignKey(SubCategory, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(default="400-200.png", upload_to='img_uploads/')
 
    def __str__(self):
        return f"{self.get_name_display()} - {self.sub_category.name}"