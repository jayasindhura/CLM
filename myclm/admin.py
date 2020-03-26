from django.contrib import admin
from .models import Category,Author,Book,Member,Borrow

# Register your models here.
class CategoryList(admin.ModelAdmin):
    list_display = ['category_name']
    list_filter = ['category_name']
    search_fields = ['category_name']
    ordering = ['category_name']

class AuthorList(admin.ModelAdmin):
    list_display = ['Author_name']
    list_filter = ['Author_name']
    search_fields = ['Author_name']
    ordering = ['Author_name']

class BookList(admin.ModelAdmin):
    list_display = ('Book_Title','Book_publisher', 'Book_author_name','Book_category_name')
    list_filter = ('Book_Title','Book_publisher', 'Book_author_name','Book_category_name')
    search_fields = ('Book_Title','Book_publisher', 'Book_author_name','Book_category_name')
    ordering = ['Book_Title']

class MemberList(admin.ModelAdmin):
    list_display = ('Member_NUID','Member_first_name','Member_middle_name', 'Member_last_name','Member_organization','Member_role')
    list_filter = ('Member_NUID','Member_first_name','Member_middle_name', 'Member_last_name','Member_organization','Member_role')
    search_fields = ('Member_NUID','Member_first_name','Member_middle_name', 'Member_last_name','Member_organization','Member_role')
    ordering = ['Member_NUID']

class BorrowList(admin.ModelAdmin):
    list_display = ('Borrow_Member_NUID','Borrow_Book_Name','Borrow_Author_Name','Borrow_Category_Name','Taken_date','Broughtback_date')
    list_filter = ('Borrow_Member_NUID','Borrow_Book_Name','Borrow_Author_Name','Borrow_Category_Name','Taken_date','Broughtback_date')
    search_fields = ('Borrow_Member_NUID','Borrow_Book_Name','Borrow_Author_Name','Borrow_Category_Name','Taken_date','Broughtback_date')
    ordering = ['Borrow_Member_NUID']

admin.site.register(Category,CategoryList)
admin.site.register(Author,AuthorList)
admin.site.register(Book,BookList)
admin.site.register(Member,MemberList)
admin.site.register(Borrow,BorrowList)
