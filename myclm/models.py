from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, UserManager
from myclm.utils import ROLES


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    role = models.CharField(choices=ROLES, max_length=50)
    is_staff = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name if full_name else self.email

    @property
    def full_name(self):
        return self.get_full_name()


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.category_name)

class Author(models.Model):
    Author_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Author_name)

class Book(models.Model):
    Book_Title = models.CharField(max_length=100)
    Book_ISBN = models.CharField(max_length=100)
    Book_publisher = models.CharField(max_length=100)
    Book_author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default='', blank=True, null=True)
    Book_category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default='', blank=True, null=True)
    #Book_count = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Book_Title)

class Member(models.Model):
    Member_NUID = models.CharField(max_length=100)
    Member_first_name = models.CharField(max_length=100)
    Member_middle_name = models.CharField(max_length=100, blank=True)
    Member_last_name = models.CharField(max_length=100)
    Member_organization = models.CharField(max_length=100)
    Member_role = models.CharField(max_length=100)
    Member_email = models.EmailField(max_length=100)
    Member_address = models.CharField(max_length=200)
    Member_city = models.CharField(max_length=50)
    Member_state = models.CharField(max_length=50)
    Member_zipcode = models.CharField(max_length=10)
    Member_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Member_NUID)



class Borrow(models.Model):
    Borrow_Member_NUID = models.ForeignKey(Member, on_delete=models.CASCADE, default='', blank=True, null=True)
    Borrow_Book_Name = models.ForeignKey(Book, on_delete=models.CASCADE, default='', blank=True, null=True)
    Borrow_Author_Name = models.ForeignKey(Author, on_delete=models.CASCADE, default='', blank=True, null=True)
    Borrow_Category_Name = models.ForeignKey(Category, on_delete=models.CASCADE, default='', blank=True, null=True)
    Taken_date = models.DateTimeField(default=timezone.now)
    Broughtback_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Borrow_Member_NUID)


