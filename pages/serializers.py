from rest_framework import serializers
from rest_framework import permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Reklama, Student, Video, Test, Kurslar, Category, Text, Department, Comment, Subdepartment, \
    Videocomment, Aksiya, Onlinetest, Blog, Blogcomment, Blogtable, Help, Helpvideotable, Helptexttable, Subcategory

#GET uchun serializer yaratamiz
class RekSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reklama
        fields = '__all__'

#POST serializer

class Reklamapostserializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'


#GET Student qilish uchun serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

#POST  Student uchun serializer yaratamiz

class StudentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'




# GET Subcategory view

class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    # id = serializers.ReadOnlyField()


    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'photo', 'category')

        def get_category(self, obj):
            category = Category.objects.filter(subcategory=obj)
            return CategorySerializer(category, many=True).data


#POST Subcategory serializer
class SubcategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('title', 'photo')



#GET CategorySerializer

class CategorySerializer(serializers.ModelSerializer):
    kurslar =serializers.SerializerMethodField()


    class Meta:
        model = Category
        fields = ('id', 'title', 'kurslar')


#POST Categoryserializer
class CategoryPostSerializer(serializers.ModelSerializer):
    # kurslar =serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'




# GET kurslar

class KurslarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class KurslarPostSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()



    def get_video(self, obj):
        video =Video.objects.filter(subdepartment__department__kurslar=obj)
        return video.count()

    def get_text(self,obj):
        text = Text.objects.filter(text=obj)
        return text.count()


    class Meta:
        model = Kurslar
        fields = ['id','teachername', 'video', 'text', 'department']

    def get_department(self,obj):
        department = Department.objects.filter(kurslar=obj)
        return DepartmentSerializer(department, many=True).data






    def get_kurslar(self,obj):
        kurslar = Kurslar.objects.filter(category=obj)
        return KurslarSerializer(kurslar, many=True).data


# GET DepartmentSerializer

class DepartmentSerializer(serializers.ModelSerializer):
    subdepartment = serializers.SerializerMethodField()



    class Meta:
        model = Department
        fields = ('id', 'title', 'subdepartment')
    def get_subdepartment(self,obj):
        subdepartment = Subdepartment.objects.filter(department=obj)
        return SubdepartmentSerializer(subdepartment, many=True).data




class DepartmentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class SubdepartmentSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()
    videocomment = serializers.SerializerMethodField()
    test =serializers.SerializerMethodField()
    onlinetest =serializers.SerializerMethodField()


    def get_test(self,obj):
        test = Test.objects.filter(name=obj)
        return TextSerializer(test, many=True).data



    def get_video(self, obj):
        video= Video.objects.filter(subdepartment_id=obj.id)
        return VideoSerializer(video, many=True).data

    def get_text(self, obj):
        text=Text.objects.filter(subdepartment_id=obj.id)
        return TextSerializer(text, many=True).data


    def get_videocomment(self, obj):
        videocomment = Videocomment.objects.filter(subdepart=obj)
        return VideocommentSerializer(videocomment, many=True).data


    def get_onlinetest(self,obj):
        onlinetest = Onlinetest.objects.filter(onlinetest=obj)
        return Onlinetestserializer(onlinetest, many=True).data



    class Meta:
        model = Subdepartment
        fields = ('id', 'text', 'video','videocomment', 'test', 'onlinetest')


#POST

class SubDepartmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdepartment
        fields = '__all__'






#GET Textserializer
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'




# POST TextPostSerializer
class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

#GET VideoSerializer
# VideoPostSerializer

class  VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'




# VideoPostSerializer

class  VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

# GET Testserialier
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'

class  TestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


#GET Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# POST Comment
class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class VideocommentSerializer(serializers.ModelSerializer):
    # videourl = serializers.CharField(source='video.video')
    class Meta:
        model = Videocomment
        fields = '__all__'


class VideoCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videocomment
        fields='__all__'



class Onlinetestserializer(serializers.ModelSerializer):

    aksiya = serializers.SerializerMethodField()


    def get_aksiya(self,obj):
        aksiya = Aksiya.objects.filter(aksiya=obj)
        return Aksiyaserializer(aksiya, many=True).data




    class Meta:
        model = Onlinetest
        fields = ('title', 'photo','onlinetest', 'link', 'aksiya')


class OnlineTestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onlinetest
        fields = '__all__'

# AksiyaSerializerni yaratamiz
class Aksiyaserializer(serializers.ModelSerializer):


    blogtable = serializers.SerializerMethodField()


    def get_blogtable(self,obj):
        blogtable = Blogtable.objects.filter(blogtable=obj)
        return Blogtableserializer(blogtable, many=True).data

    class Meta:
        model = Aksiya
        fields = ('text', 'blogtable',)


class AksiyaPostSerializer(serializers.ModelSerializer):
 class Meta:
        model = Aksiya
        fields = '__all__'


class Blogtableserializer(serializers.ModelSerializer):

    blog = serializers.SerializerMethodField()


    def get_blog(self,obj):
        blog = Blog.objects.filter(blog=obj)
        return Blogserializer(blog, many=True).data



    class Meta:
        model = Blogtable
        fields = ('title','blog')


class BlogtablePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogtable
        fields ='__all__'


#Blogserializer yaratamiz


class Blogserializer(serializers.ModelSerializer):


    blogcomment =serializers.SerializerMethodField()


    def get_blogcomment(self,obj):
        blogcomment = Blogcomment.objects.filter(blogcomment=obj)
        return Blogcommentserializer(blogcomment, many=True).data


    class Meta:
        model = Blog
        fields = ('text', 'photo', 'blogcomment')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



# Blogcommentserializer yaratamiz

class Blogcommentserializer(serializers.ModelSerializer):

    class Meta :
        model = Blogcomment
        fields = '__all__'


class BlogCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogcomment
        fields = '__all__'






# Helpserializer yaratamiz

class Helpserializer(serializers.ModelSerializer):

    class Meta:
        model = Help
        fields = '__all__'

class HelpPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Help
        fields = '__all__'

#Helpvideotableserializer yaratamiz

class Helpvideotableserializer(serializers.ModelSerializer):
    class Meta:
        model = Helpvideotable
        fields = '__all__'



class HelpVideoTablePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helpvideotable
        fields = '__all__'

#Helptextserializer yaratamiz

class Helptexttableserializer(serializers.ModelSerializer):
    class Meta:
        model = Helptexttable
        fields = '__all__'


class HelpTextTablePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helptexttable
        fields = '__all__'



class Onlinetestpostserializer(serializers.ModelSerializer):
    class Meta:
        model = Onlinetest
        fields = '__all__'

class Aksiyapostserializer(serializers.ModelSerializer):
    class Meta:
        model = Aksiya
        fields = '__all__'







#Login uchun
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token


#class LoginUserSerializer(serializers.ModelSerializer):


