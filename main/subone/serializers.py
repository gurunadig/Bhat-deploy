from rest_framework.serializers import ModelSerializer
from .models import TextEditor, MainBanner,MainBannerResponsive,  Notification, Contact, PrivacyPolicy, Stat, TeacherTestimonial, BranchesCtg, Branch, Instructor, Course, Blog, BlogCtg, TeachingStaff, ManagementStaff,CourseNotification, Success_story, Department, CareerCtg, Career, NumbersData, AchieversBanner,AchieversBannerResponsive, StudentTestimonials, ContactForm, CareersForm, CoursessForm, Video, VidGallery, Image, ImgGallery, NonTeachingStaff, Batches, BatchesCtg, MainCategory, SubCategory, Category, Sections

from rest_framework import serializers

class TextEditorSerializer(ModelSerializer):
    class Meta:
        model = TextEditor
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'

class BannerResponsiveSerializer(ModelSerializer):
    class Meta:
        model = MainBannerResponsive
        fields = '__all__'

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class PrivacyPolicySerializer(ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class StatSerializer(ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class TeacherTestimonialSerializer(ModelSerializer):
    class Meta:
        model = TeacherTestimonial
        fields = '__all__'



class BranchesCtgSerializer(ModelSerializer):
    class Meta:
        model = BranchesCtg
        fields = '__all__'



class BranchSerializer(ModelSerializer):
    branches = BranchesCtgSerializer(many=True, read_only=True)
    class Meta:
        model =  Branch
        fields = '__all__'



class CourseSerializer(ModelSerializer):
    class Meta:
        model =  Course
        fields = '__all__'


class InstructorSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model =  Instructor
        fields = '__all__'


class BlogCtgSerializer(ModelSerializer):
    class Meta:
        model = BlogCtg
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    blogs = BlogCtgSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'


class TeachingStaffSerializer(ModelSerializer):
    class Meta:
        model = TeachingStaff
        fields = '__all__'


class ManagementStaffSerializer(ModelSerializer):
    class Meta:
        model = ManagementStaff
        fields = '__all__'


class NonTeachingStaffSerializer(ModelSerializer):
    class Meta:
        model = NonTeachingStaff
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class Success_storySerializer(ModelSerializer):
    success_story = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Success_story
        fields = '__all__'


class CareerCtgSerializer(ModelSerializer):
    class Meta:
        model = CareerCtg
        fields = '__all__'


class CareerSerializer(ModelSerializer):
    careers = CareerCtgSerializer(many=True, read_only=True)
    class Meta:
        model = Career
        fields = '__all__'




class StudentTestiomoialsSerializer(ModelSerializer):
    class Meta:
        model = StudentTestimonials
        fields = '__all__'



class TheNumbersSerializer(ModelSerializer):
    class Meta:
        model = NumbersData
        fields = '__all__'



class AchieversBannerSerializer(ModelSerializer):
    class Meta:
        model = AchieversBanner
        fields = '__all__'


class AchieversBannerResponsiveSerializer(ModelSerializer):
    class Meta:
        model = AchieversBannerResponsive
        fields = '__all__'

class CourseNotificationSerializer(ModelSerializer): 
    class Meta:
        model = CourseNotification
        fields = '__all__'

class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class CourseFormSerializer(ModelSerializer):
    class Meta:
        model = CoursessForm
        fields = '__all__'

class CareerFormSerializer(ModelSerializer):
    class Meta:
        model = CareersForm
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model =  Image
        fields = '__all__'


class ImgGallerySerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model =  ImgGallery
        fields = '__all__'



class VideoSerializer(ModelSerializer):
    class Meta:
        model =  Video
        fields = '__all__'


class VideoGallerySerializer(ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model =  VidGallery
        fields = '__all__'



class BatchesSerializer(ModelSerializer):
    class Meta:
        model =  Batches
        fields = '__all__'


class BatchesCtgSerializer(ModelSerializer):
    class Meta:
        model =  BatchesCtg
        fields = '__all__'



# class CourseOverviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseOverview
#         fields = ['id', 'text']

# class CourseBatchDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseBatchDetail
#         fields = ['id', 'text', 'batch_img']

# class CourseCurriculumSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseCurriculum
#         fields = ['id', 'text']

# class CourseInstructorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseInstructor
#         fields = ['id', 'name', 'bio', 'img']

# class SubCategorySerializer(serializers.ModelSerializer):
#     courseOverview = CourseOverviewSerializer()
#     courseBatch_details = CourseBatchDetailSerializer()
#     courseCurriculum = CourseCurriculumSerializer()
#     courseInstructor = CourseInstructorSerializer()

#     class Meta:
#         model = SubCategory
#         fields = ['id', 'name', 'courseOverview', 'courseBatch_details', 'courseCurriculum', 'courseInstructor']

# class CategoryLevel2Serializer(serializers.ModelSerializer):
#     subcategories = SubCategorySerializer(many=True)

#     class Meta:
#         model = CategoryLevel2
#         fields = ['id', 'name', 'subcategories']

# class CategoryLevel1Serializer(serializers.ModelSerializer):
#     categories_lvl2 = CategoryLevel2Serializer(many=True)

#     class Meta:
#         model = CategoryLevel1
#         fields = ['id', 'name', 'categories_lvl2']

# class MainCategorySerializer(serializers.ModelSerializer):
#     categories_lvl1 = CategoryLevel1Serializer(many=True)

#     class Meta:
#         model = MainCategory
#         fields = ['id', 'name', 'categories_lvl1']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['id', 'name', 'sub_category', 'title', 'description', 'image']
 
class SubCategorySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
 
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'sections']
 
class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = Category
        fields = ['id', 'name', 'main_category', 'sub_categories']
 
class MainCategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
 
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'categories']