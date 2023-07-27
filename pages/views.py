from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from rest_framework import generics, status, viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Reklama, Student, Video, Test, Kurslar, Category, Department, Text, Comment, Subdepartment, \
    Videocomment, Aksiya, Onlinetest, Blog, Blogcomment, Blogtable, Helpvideotable, Help, Helptexttable, Subcategory
from .serializers import RekSerializer, StudentSerializer, VideoSerializer, KurslarSerializer, \
    CategorySerializer, DepartmentSerializer, TextSerializer, CommentSerializer, VideocommentSerializer, \
    SubdepartmentSerializer, CategoryPostSerializer, KurslarPostSerializer, DepartmentPostSerializer, \
    VideoPostSerializer, TestPostSerializer, TextPostSerializer, \
    VideoCommentPostSerializer, CommentPostSerializer, StudentPostSerializer, Aksiyaserializer, \
    Onlinetestserializer, Blogserializer, Blogcommentserializer, Blogtableserializer, Helpserializer, \
    Helpvideotableserializer, Helptexttableserializer, Aksiyapostserializer, \
    Reklamapostserializer, SubcategorySerializer, SubcategoryPostSerializer, SubDepartmentPostSerializer, \
    TestSerializer, OnlineTestPostSerializer, AksiyaPostSerializer, BlogtablePostSerializer, BlogPostSerializer, \
    HelpPostSerializer, HelpVideoTablePostSerializer, HelpTextTablePostSerializer

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny, ])
def reklamaview(request, id):
    queryset = Reklama.objects.get(id=id)
    serializer = RekSerializer(queryset)
    return Response(serializer.data)


# RekPostView

class ReklamaPostView(generics.ListCreateAPIView):
    queryset = Reklama.objects.all()
    serializer_class = Reklamapostserializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        rekpost = Reklama.objects.create(
            text=data['text'],
            photo=data['photo'],
            body=data['body'],

        )
        return Response(status=status.HTTP_201_CREATED)


# GET Student view

@api_view(['GET'])
@permission_classes([AllowAny, ])
def studentview(request, id):
    queryset = Student.objects.get(id=id)
    serializer = StudentSerializer(queryset)
    return Response(serializer.data)


# POST Student view

class StudentPostView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPostSerializer


# GET  Subcategory view

@api_view(['GET'])
@permission_classes([AllowAny, ])
def subcategoryview(request, id):
    queryset = Subcategory.objects.get(id=id)
    serializer = SubcategorySerializer(queryset)
    return Response(serializer.data)


# POST Subcategory view
class SubcategoryPostView(generics.CreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryPostSerializer


# GET Category view


@api_view(['GET'])
@permission_classes([AllowAny, ])
def categoryview(request, id):
    queryset = Category.objects.filter(title=id)
    serializer = CategorySerializer(queryset, many=True)
    subcategory = Subcategory.objects.filter(photo=id)
    subcategoryserializer = SubcategorySerializer(subcategory, many=True)

    context = {
        'title': serializer.data,
        'subcategory': subcategoryserializer.data,
    }

    return Response(context, status=status.HTTP_201_CREATED)


# POST CategoryPostView
class CategoryPostView(generics.UpdateAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategoryPostSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        rekpost = Category.objects.create(
        title=data['title'],
        # subcategory_id=self.kwargs['id'],

        )
        return Response(status=status.HTTP_201_CREATED)

class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    model= Category
    serializer_class = CategoryPostSerializer
    queryset = Category.objects.all()



    # def update(self, request, *args, **kwargs):
    #     context = Category.objects.get(id=self.kwargs.get("id"))
    #     response = super().update(request, *args, **kwargs)
    #     response.data = {'success': True, 'data': response.data}
    #     return super().update(context, request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def category_update(self, request, *args, **kwargs):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset)

    context = Category.objects.get(id=self.kwargs.get("id"))
    response = super().update(request, *args, **kwargs)
    response.data = {'success': True, 'data': response.data}
    return super().update(context, request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kurslarview(request, id):
    queryset = Kurslar.objects.get(id=id)
    serializer = KurslarSerializer(queryset)
    return Response(serializer.data)




# GET Kurslar view


# POST KUrslar view

class KurslarPostView(generics.ListCreateAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KurslarPostSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        context = Kurslar.objects.create(
            coursename=data['coursename'],
            teachername=data['teachername'],
            photo=data['photo'],
            about=data[' about'],
            category_id=self.kwargs['id'],

        )
        return Response(status=status.HTTP_201_CREATED)


# GET departmentview
@api_view(['GET'])
@permission_classes([AllowAny, ])
def departmentview(request, id):
    queryset = Department.objects.get(id=id)
    serializer = DepartmentSerializer(queryset)
    return Response(serializer.data)


# POST DepartmentPostView


class DepartmentPostView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPostSerializer


# GET Subdepartment view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def subdepartmentview(request, id):
    queryset = Subdepartment.objects.get(id=id)
    serializer = SubdepartmentSerializer(queryset)
    return Response(serializer.data)


# POST SUbdepartment
class SubDepartmentPostView(generics.CreateAPIView):
    queryset = Subdepartment.objects.all()
    serializer_class = SubDepartmentPostSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        context = Subdepartment.objects.create(
            title=data['title'],

        )
        return Response(status=status.HTTP_201_CREATED)


# TextView

@api_view(['GET'])
@permission_classes([AllowAny, ])
def textview(request, id):
    queryset = Text.objects.get(id=id)
    serializer = TextSerializer(queryset)
    return Response(serializer.data)


# Post TextPostview

class TextPostView(generics.CreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextPostSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST
        context = Text.objects.create(
            title=data['title'],
            text=data['text'],
            subdepartment_id=self.kwargs['id'],

        )
        return Response(status=status.HTTP_201_CREATED)


# GET Videopost view


@api_view(['GET'])
@permission_classes([AllowAny, ])
def videoview(request, id):
    queryset = Video.objects.get(id=id)
    serializer = VideoSerializer(queryset)
    return Response(serializer.data)


# POST Video view
class VideoPostView(generics.CreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoPostSerializer


# GET Test view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def testview(request, id):
    queryset = Test.objects.get(id=id)
    serializer = TestSerializer(queryset)
    return Response(serializer.data)


# POST

class TestPostView(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestPostSerializer


# GET Test view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def commentview(request, id):
    queryset = Comment.objects.get(id=id)
    serializer = CommentSerializer(queryset)
    return Response(serializer.data)


class CommentPostView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentPostSerializer


# GET Test view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def videocommentview(request, id):
    queryset = Videocomment.objects.get(id=id)
    serializer = VideocommentSerializer(queryset)
    return Response(serializer.data)


class VideoCommentPostView(generics.CreateAPIView):
    queryset = Videocomment.objects.all()
    serializer_class = VideoCommentPostSerializer


# GET Onlintest  view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def onlinetestview(request, id):
    queryset = Onlinetest.objects.get(id=id)
    serializer = Onlinetestserializer(queryset)
    return Response(serializer.data)



class OnlineTestPostView(generics.CreateAPIView):
    queryset = Onlinetest.objects.all()
    serializer_class = OnlineTestPostSerializer



# GET Onlintest  view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def aksiyaview(request, id):
    queryset = Aksiya.objects.get(id=id)
    serializer = Aksiyaserializer(queryset)
    return Response(serializer.data)



class AksiyaPostView(generics.CreateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaPostSerializer





# GET Onlintest  view
@api_view(['GET'])
@permission_classes([AllowAny, ])
def blogtableview(request, id):
    queryset = Blogtable.objects.get(id=id)
    serializer = Blogtableserializer(queryset)
    return Response(serializer.data)



class BlogTablePostView(generics.CreateAPIView):
    queryset = Blogtable.objects.all()
    serializer = BlogtablePostSerializer




@api_view(['GET'])
@permission_classes([AllowAny, ])
def blogview(request, id):
    queryset = Blog.objects.get(id=id)
    serializer = Blogserializer(queryset)
    return Response(serializer.data)



class BlogPostView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogPostSerializer



@api_view(['GET'])
@permission_classes([AllowAny, ])
def blogcommentview(request, id):
    queryset = Blogcomment.objects.get(id=id)
    serializer = Blogcommentserializer(queryset)
    return Response(serializer.data)




class BlogCommentPostView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =BlogPostSerializer





@api_view(['GET'])
@permission_classes([AllowAny, ])
def helpview(request, id):
    queryset = Help.objects.get(id=id)
    serializer = Helpserializer(queryset)
    return Response(serializer.data)




class HelpPostView(generics.CreateAPIView):
    queryset = Help.objects.all()
    serializer_class =HelpPostSerializer

@api_view(['GET'])
@permission_classes([AllowAny, ])
def helpvideotableview(request, id):
    queryset = HelpHelpvideotable.objects.get(id=id)
    serializer = Helpvideotableserializer(queryset)
    return Response(serializer.data)




class HelpVideoTablePostView(generics.CreateAPIView):
    queryset = Help.objects.all()
    serializer_class =HelpVideoTablePostSerializer




@api_view(['GET'])
@permission_classes([AllowAny, ])
def helptexttableview(request, id):
    queryset = Helptexttable.objects.get(id=id)
    serializer = Helptexttableserializer(queryset)
    return Response(serializer.data)




class HelpTextTablePostView(generics.CreateAPIView):
    queryset = Help.objects.all()
    serializer_class =HelpTextTablePostSerializer

class CategoryView(generics.RetrieveAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KurslarSerializer


class VideoCommentView(generics.ListCreateAPIView):
    queryset = Videocomment.objects.all()
    serializer_class = VideocommentSerializer


class All(generics.ListCreateAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KurslarSerializer

    def list(self, request, *args, **kwargs):
        course = Kurslar.objects.all()
        video = Video.objects.all()
        reklama = Reklama.objects.all()
        test = Test.objects.all()
        student = Student.objects.all()
        title = Category.objects.all()
        context = {
            'reklama': RekSerializer(reklama, many=True).data,
            'student': student.count(),
            'video': video.count(),
            'kurslar': course.count(),
            'test': test.count(),
            'title': title.values(),

        }
        return Response(context)


class AllSubDepartView(generics.RetrieveAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KurslarSerializer


@api_view(['GET'])
@permission_classes([AllowAny, ])
def allsubdepartview(request, id):
    video = Video.objects.filter(subdepartment_id=id)
    serializer = VideoSerializer(video, many=True)
    text = Text.objects.filter(subdepartment_id=id)
    textserializer = TextSerializer(text, many=True)
    test = Test.objects.filter(name_id=id)
    testserializer = TestSerializer(test, many=True)
    vcomment = Videocomment.objects.filter(subdepart_id=id)
    vcommentserializer = VideocommentSerializer(vcomment, many=True)
    context = {
        'video': serializer.data,
        'text': textserializer.data,
        'test': testserializer.data,
        'vcomment': vcommentserializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)


class AllDepartmentView(generics.RetrieveAPIView):
    queryset = Subdepartment.objects.all()
    serializer_class = SubdepartmentSerializer


@api_view(['GET'])
@permission_classes([AllowAny, ])
def alldepartview(request, id):
    video = Video.objects.filter(subdepartment_id=id)
    serializer = VideoSerializer(video, many=True)
    about = Subdepartment.objects.filter(department_id=id)
    aboutserializer = SubdepartmentSerializer(about, many=True)
    text = Text.objects.filter(subdepartment_id=id)
    textserializer = TextSerializer(text, many=True)
    subdepartment = Subdepartment.objects.filter(department_id=id)
    subdepartmentserializer = SubdepartmentSerializer(subdepartment, many=True)
    context = {
        'texts': text.count(),
        'video': serializer.data,
        'about': aboutserializer.data,
        'darslar': subdepartmentserializer.data
    }
    return Response(context, status=status.HTTP_200_OK)


class AllKurslarView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


@api_view(['GET'])
@permission_classes([AllowAny, ])
def allkurslarview(request, id):
    department = Department.objects.filter(kurslar_id=id)
    departmentserializer = DepartmentSerializer(department, many=True)
    comment = Comment.objects.filter(kurslar_id=id)
    commentserializer = CommentSerializer(comment, many=True)
    context = {
        'department': departmentserializer.data,
        'comment': commentserializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)


class AllCategoryView(generics.RetrieveAPIView):
    queryset = Kurslar.objects.all()
    serializer_class = KurslarSerializer




@api_view(['GET'])
@permission_classes([AllowAny, ])
def allcategoryview(request, id):
    kurslar = Kurslar.objects.filter(category_id=id)
    kurslarserializer = KurslarSerializer(kurslar, many=True)
    context = {
        'kurslar': kurslarserializer.data,
    }
    return Response(context, status=status.HTTP_200_OK)


# SubdepartmentPost




















class CommentPost(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentPostSerializer

    def post(self, request, *args, **kwargs):
        data = request.POST

        test = Comment.objects.create(
            title=data['title'],
            student_id=self.kwargs['id'],
            kurslar_id=self.kwargs['id'],

        )
        return Response(status=status.HTTP_201_CREATED)


class LoginUserView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"Message": 'Incorrect authentication details', 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)
        access = str(AccessToken.for_user(user))
        return Response({"Message": 'Authentication method is correct', 'access': access, 'success': True},
                        status=status.HTTP_200_OK)


class SubCategoryView(generics.GenericAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def post(self, request, id):
        data = request.POST
        subcategory = Subcategory.objects.create(
            title=data['title'],
            photo=data['photo'],

        )
        return Response(subcategory, status=status.HTTP_201_CREATED)


# Regstrasa Post Teacher aand Student


class RegstrationsView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        if request.data['status'] == 'teacher':
            return Response('Hello ')

        return Response('Have are you ')


# AksiyaView yaratamiz

class AksiyaView(generics.ListCreateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = Aksiyaserializer


# OnlinetestView yaratamiz


class OnlinetestView(generics.ListCreateAPIView):
    queryset = Onlinetest.objects.all()
    serializer_class = Onlinetestserializer


# BlogView yaratamiz


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = Blogserializer


# BlogcommentView yaratamiz


class BlogcommentView(generics.ListCreateAPIView):
    queryset = Blogcomment.objects.all()
    serializer_class = Blogcommentserializer


class BlogctableView(generics.ListCreateAPIView):
    queryset = Blogtable.objects.all()
    serializer_class = Blogtableserializer


# HelpView yaratamiz


class HelpView(generics.ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = Helpserializer


# HelpVideoTableView yaratamiz

class HelpVideoTableView(generics.ListCreateAPIView):
    queryset = Helpvideotable.objects.all()
    serializer_class = Helpvideotableserializer


# Helptexttable yaratamiz

class HelpTextTableView(generics.ListCreateAPIView):
    queryset = Helptexttable.objects.all()
    serializer_class = Helptexttableserializer


# POST Online test




@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Onlinetest.objects.create(
        title=data['title'],
        photo=data['photo'],
        link=data['link'],
    )

    return Response(online, status=status.HTTP_200_OK)


class AksiyaPostView(generics.CreateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = Aksiyapostserializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Aksiya.objects.create(
        text=data['text'],
    )

    return Response(online, status=status.HTTP_200_OK)


class BlogTablePostView(generics.CreateAPIView):
    queryset = Blogtable.objects.all()
    serializer_class = Blogtableserializer










@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Blog.objects.create(
        text=data['text'],
        photo=data['photo'],

    )

    return Response(online, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Blogcomment.objects.create(
        title=data['title'],
        comment=data['comment'],

    )

    return Response(online, status=status.HTTP_200_OK)





@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Help.objects.create(
        title=data['title'],

    )

    return Response(online, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Helpvideotable.objects.create(
        title=data['title'],
        video=data['video'],

    )

    return Response(online, status=status.HTTP_200_OK)





@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    data = request.POST

    online = Helptexttable.objects.create(
        title=data['title'],
        text=data['text'],

    )

    return Response(online, status=status.HTTP_200_OK)


class ReklamaPostView(generics.CreateAPIView):
    queryset = Reklama.objects.all()
    serializer_class = Reklamapostserializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def reklamapost(request):
    data = request.POST

    online = Reklama.objects.create(
        title=data['title'],
        photo=data['photo'],
    )
    return Response(online, status=status.HTTP_200_OK)


# Login view
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
