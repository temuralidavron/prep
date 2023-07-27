from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CategoryView, All, \
    categoryview, subdepartmentview, \
    allsubdepartview, alldepartview, allkurslarview, allcategoryview, CategoryPostView, \
    KurslarPostView, DepartmentPostView, SubDepartmentPostView, \
    CommentPost, RegstrationsView, AksiyaView, OnlinetestView, BlogView, BlogcommentView, BlogctableView, \
    HelpTextTableView, HelpVideoTableView, HelpView, OnlineTestPostView, AksiyaPostView, BlogPostView, \
    BlogCommentPostView, HelpPostView, HelpVideoTablePostView, HelpTextTablePostView, ReklamaPostView, \
    LoginUserView, register, reklamaview, studentview, subcategoryview, SubcategoryPostView, \
    categoryview, kurslarview, departmentview, textview, VideoPostView, testview, TestPostView, commentview, \
    CommentPostView, videocommentview, VideoCommentPostView, onlinetestview, aksiyaview, BlogTablePostView, \
    blogtableview, blogview, blogcommentview, helpview, helpvideotableview, helptexttableview, CategoryUpdateView, \
    category_update
from pages.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('loginuserview', LoginUserView.as_view()),
    path('register/<int:id>', register),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("reklama", ReklamaView.as_view()),
    path("reklamaview/<int:id>",reklamaview),
    path("reklamapostview/<int:id>", ReklamaPostView.as_view()),
    path("studentview/<int:id>", studentview),
    path("subcategoryview/<int:id>",subcategoryview),
    path("subcategorpostview/<int:id>", SubcategoryPostView.as_view()),
    path("categoryview/<int:id>", categoryview),
    path("cpostview/<int:pk>", CategoryPostView.as_view()),
    path("kurslarview/<int:id>", kurslarview),
    path("kurslarpostview/<int:id>", KurslarPostView.as_view()),
    path("departmentview/<int:id>", departmentview),
    path("departmentpostview", DepartmentPostView.as_view()),
    path("subdepartmentview/<int:id>", subdepartmentview),
    path("subdepartmentpostview/<int:id>", SubDepartmentPostView.as_view()),
    path("textview/<int:id>",textview),
    path("testview/<int:id>", testview),
    path("testpostview/<int:id>", TestPostView.as_view()),
    path("commentview/<int:id>", commentview),
    path("commentpostview/<int:id>/", CommentPostView.as_view()),
    path("videocommentview/<int:id>", videocommentview),
    path("videopostview", VideoPostView.as_view()),
    # path("kurslar", KurslarView.as_view()),
    path("subdepartment/<int:id>", subdepartmentview),
    path("videocommentpostview/<int:id>", VideoCommentPostView.as_view()),
    path("onlinetestview/<int:id>", onlinetestview),
    path("onlinetestpostview/<int:id>", OnlineTestPostView.as_view()),
    path("aksiyaview/<int:id>", aksiyaview),
    path("aksiyapostview/<int:id>", AksiyaPostView.as_view()),
    path("blogtableview/<int:id>", blogtableview),
    path("blogtablepostview/<int:id>", BlogTablePostView.as_view()),
    path("blogview/<int:id>", blogview),
    path("blogpostview/<int:pk>", BlogPostView.as_view()),
    path("blogcommentview/<int:id>", blogcommentview),
    path("blogcommentpostview/<int:id>", BlogCommentPostView.as_view()),
    path("videocomment",  videocommentview),#ishlamayapdi

    path("helpview/<int:id>",helpview),
    path("helppostview/<int:id>",HelpPostView.as_view()),
    path("helpvideotableview/<int:id>",helpvideotableview),
    path("helptexttableview/<int:id>",helptexttableview),
    path("helptexttablepostview/<int:id>",HelpTextTablePostView.as_view()),
    path("helpvideotablepostview/<int:id>",HelpVideoTablePostView.as_view()),
    path("kurslarpostview/<int:id>",KurslarPostView.as_view()),
    path("departmentpostview/<int:id>",DepartmentPostView.as_view()),
    path("subdepartmentpostview/<int:id>",SubDepartmentPostView.as_view()),
    path("categoryupdateview/<int:pk>", CategoryUpdateView.as_view()),
    # path("category_update/<int:id>", category_update),

    path("commentpost/<int:id>", CommentPost.as_view()),
    path("allcategoryview/<int:id>", allcategoryview),
    path("allsubdepart/<int:id>", allsubdepartview),
    path("alldepartment/<int:id>", alldepartview),
    path("allkurslarview/<int:id>", allkurslarview),
    path("regstrationsview/<int:id>", RegstrationsView.as_view()),
    path("aksiyaview/<int:id>", AksiyaView.as_view()),
    path("onlinetestview/<int:id>", OnlinetestView.as_view()),
    path("blogctableview/<int:id>", BlogctableView.as_view()),
    path("blogview/<int:id>",BlogView.as_view()),
    path("blogcommentview/<int:id>", BlogcommentView.as_view()),
    path("HelpView/<int:id>", HelpView.as_view()),
    path("helpvideotableview/<int:id>", HelpVideoTableView.as_view()),
    path("helptexttableview/<int:id>", HelpTextTableView.as_view()),
    path("onlinetestpostview/<int:id>", OnlineTestPostView.as_view()),
    path("aksiyapostview/<int:id>", AksiyaPostView.as_view()),
    path("blogcommentpostview/<int:id>", BlogCommentPostView.as_view()),
    path("helppostview/<int:id>",  HelpPostView.as_view()),
    path("helpvideotablepostview/<int:id>", HelpVideoTablePostView.as_view()),
    path("helptexttablepostview/<int:id>", HelpTextTablePostView.as_view()),

    path('all', All.as_view()),


]







