from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.





class Reklama(models.Model):
    text = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='uploads/')
    body = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.text





class Student(models.Model):
    STATUS = (
        ('student','STUDENT'),
        ('teacher', 'TEACHER'),
    )
    status = models.CharField(max_length=50,blank=True, null=True, choices=STATUS)
    username = models.CharField(max_length=50)
    login = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=10,blank=True, null=True)
    age = models.IntegerField()
    science= models.CharField(max_length=50)
    aboutme =models.TextField(blank=True, null=True)




    def __str__(self):
        return self.username




class Subcategory(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    photo = models.ImageField(upload_to='image/', blank=True, null=True)


    def __str__(self):
        return self.title








class Category(models.Model):
    title = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.title






class Kurslar(models.Model):
    coursename = models.CharField(max_length=100, blank=True, null=True)
    teachername = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='image', blank=True, null=True)
    about = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.coursename



class Department(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    kurslar = models.ForeignKey(Kurslar, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Subdepartment(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    subdepartment =models.ForeignKey(Subdepartment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Video(models.Model):
    title = models.CharField(max_length=50,  blank=True, null=True)
    video = models.FileField(upload_to='uploads/')
    subdepartment = models.ForeignKey(Subdepartment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Test(models.Model):
    title = models.CharField(max_length=50)
    test = models.TextField()
    name = models.ForeignKey(Subdepartment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Comment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kurslar = models.ForeignKey(Kurslar, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title





class Videocomment(models.Model):
    text = models.TextField()
    subdepart = models.ForeignKey(Subdepartment, on_delete=models.CASCADE, blank=True, null=True, )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text


# OnlineTest Sahifasi uchun model yaratamiz


class Onlinetest(models.Model):
    title = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='image', blank=True, null=True)
    onlinetest =models.ForeignKey(Subdepartment, on_delete=models.CASCADE,blank=True,null=True)
    onlinereklama = models.ForeignKey(Reklama,on_delete=models.CASCADE,blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title



# Aksiya nomi ilova yaratamiz

class Aksiya(models.Model):
    text= models.TextField()
    aksiya = models.ForeignKey(Onlinetest, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text
#Blogtable deb nomlangan model yaratamiz

class Blogtable(models.Model):
    title =models.CharField(max_length=100,blank = True, null=True)
    blogtable = models.ForeignKey(Aksiya, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title


# Blog deb nomlangan sahifa yaratamiz

class Blog(models.Model):

    text = models.TextField()
    photo = models.ImageField(upload_to='image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blogtable, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.text


#BLogcomment  yaratamiz


class Blogcomment(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=350,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    blogcomment = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return self.title


#Help model yaratamiz


class Help(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    helpes = models.ForeignKey(Blogcomment, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.title


#Helpvideotable yaratamiz


class Helpvideotable(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    video = models.FileField(upload_to='uploads/')
    helpvideotable = models.ForeignKey(Help,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.title


# Helptexttable yaratamiz


class Helptexttable(models.Model):
    title = models.CharField(max_length=100, blank=True,null=True)
    text = models.TextField()
    helptext = models.ForeignKey(Help, on_delete=models.CASCADE,blank=True,null=True)


































