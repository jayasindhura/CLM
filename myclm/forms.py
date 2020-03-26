from django import forms
from .models import Member,Borrow,Book
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email__iexact=email).first()
        if user:
            if user.is_staff:
                user_role = "Staff"

            else:
                user_role = "Member"
            raise forms.ValidationError(
                "{} with this email already exists, use another email.".format(
                    user_role
                )
            )
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError("Password should be minimum 6 characters long")

        if password != self.data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
        return password

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('Member_NUID','Member_first_name','Member_middle_name', 'Member_last_name','Member_organization','Member_role','Member_email', 'Member_address', 'Member_city', 'Member_state', 'Member_zipcode', 'Member_phone')

class BorrowForm(forms.ModelForm):
   class Meta:
       model = Borrow
       fields = ('Borrow_Member_NUID', 'Borrow_Book_Name', 'Borrow_Author_Name', 'Borrow_Category_Name', 'Taken_date', 'Broughtback_date' )

class BookForm(forms.ModelForm):
   class Meta:
       model = Book
       fields = ('Book_Title', 'Book_ISBN', 'Book_publisher', 'Book_author_name', 'Book_category_name')