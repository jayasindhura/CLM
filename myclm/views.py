from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse, HttpResponseRedirect, reverse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from myclm.access_decorators_mixins import member_access_required, staff_access_required

# Create your views here.
def staffSignup(request):
    if request.method == "GET":
        return render(request, "myclm/staff_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_staff=True, role='staff'
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("myclm:homepage",))
        else:
            return render(
                request, "myclm/staff_signup.html", {"errors": form.errors}
            )


def memberSignup(request):
    if request.method == "GET":
        return render(request, "myclm/member_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_member=True, role="member",
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("myclm:homepage",))
        else:
            return render(
                request, "myclm/member_signup.html", {"errors": form.errors}
            )


def memberLogin(request):
    if request.method == "GET":
        return render(request, "myclm/member_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "myclm/member_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_member:
                    login(request, user)
                    return HttpResponseRedirect(reverse("myclm:home_member",))
                elif user.is_active and user.is_member is False:
                    return render(
                        request,
                        "myclm/member_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Mentor"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "myclm/member_login.html", {"errors": form.errors})


def staffLogin(request):
    if request.method == "GET":
        return render(request, "myclm/staff_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "myclm/staff_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect(reverse("myclm:homepage",))
                elif user.is_active and user.is_member is False:
                    return render(
                        request,
                        "myclm/staff_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Staff"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "myclm/staff_login.html", {"errors": form.errors})


def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'GET':
        return render(request, "myclm/password_change_form.html", {"form": form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(
                request, "myclm/password_change_done.html", {}
            )
        return render(
            request, "myclm/password_change_form.html", {"errors": form.errors}
        )



def homepage(request):
    print('yessss')
    # return HttpResponse("test myclm")
    return render(request, "myclm/landing_page.html", {})
    #return render(request, "myclm/home_member.html", {})

# Create your views here.
now = timezone.now()
def home(request):
   return render(request, 'myclm/home.html',
                 {'myclm': home})

def home_member(request):
   return render(request, 'myclm/home_member.html',
                 {'myclm': home_member})

def user_logout(request):
    logout(request)
    return redirect(reverse("myclm:homepage"))


def member_list(request):
    member = Member.objects.filter(created_date__lte=timezone.now())
    return render(request, 'myclm/member_list.html',
                 {'members': member})


def member_edit(request, pk):
   member = get_object_or_404(Member, pk=pk)
   if request.method == "POST":
       # update
       form = MemberForm(request.POST, instance=member)
       if form.is_valid():
           member = form.save(commit=False)
           member.updated_date = timezone.now()
           member.save()
           member = Member.objects.filter(created_date__lte=timezone.now())
           return render(request, 'myclm/member_list.html',
                         {'members': member})
   else:
        # edit
       form = MemberForm(instance=member)
   return render(request, 'myclm/member_edit.html', {'form': form})


def member_delete(request, pk):
   member = get_object_or_404(Member, pk=pk)
   member.delete()
   return redirect('myclm:member_list')


def borrow_list(request):
   borrows = Borrow.objects.filter(created_date__lte=timezone.now())
   return render(request, 'myclm/borrow_list.html', {'borrows': borrows})

def borrow_new(request):
   if request.method == "POST":
       form = BorrowForm(request.POST)
       if form.is_valid():
           borrow = form.save(commit=False)
           borrow.created_date = timezone.now()
           borrow.save()
           borrows = Borrow.objects.filter(created_date__lte=timezone.now())
           return render(request, 'myclm/borrow_list.html',
                         {'borrows': borrows})
   else:
       form = BorrowForm()
       # print("Else")
   return render(request, 'myclm/borrow_new.html', {'form': form})


def borrow_edit(request, pk):
   borrow = get_object_or_404(Borrow, pk=pk)
   if request.method == "POST":
       form = BorrowForm(request.POST, instance=borrow)
       if form.is_valid():
           borrow = form.save()
           # service.customer = service.id
           borrow.updated_date = timezone.now()
           borrow.save()
           borrows = Borrow.objects.filter(created_date__lte=timezone.now())
           return render(request, 'myclm/borrow_list.html', {'borrows': borrows})
   else:
       # print("else")
       form = BorrowForm(instance=borrow)
   return render(request, 'myclm/borrow_edit.html', {'form': form})


def borrow_delete(request, pk):
   borrow = get_object_or_404(Borrow, pk=pk)
   borrow.delete()
   return redirect('myclm:borrow_list')

def book_list(request):
   books = Book.objects.filter(created_date__lte=timezone.now())
   return render(request, 'myclm/book_list.html', {'books': books})



def book_new(request):
   if request.method == "POST":
       form = BookForm(request.POST)
       if form.is_valid():
           book = form.save(commit=False)
           book.created_date = timezone.now()
           book.save()
           books = Book.objects.filter(created_date__lte=timezone.now())
           return render(request, 'myclm/book_list.html',
                         {'books': books})
   else:
       form = BookForm()
       # print("Else")
   return render(request, 'myclm/book_new.html', {'form': form})


def book_edit(request, pk):
   book = get_object_or_404(Book, pk=pk)
   if request.method == "POST":
       form = BookForm(request.POST, instance=book)
       if form.is_valid():
           book = form.save()
           # service.customer = service.id
           book.updated_date = timezone.now()
           book.save()
           books = Book.objects.filter(created_date__lte=timezone.now())
           return render(request, 'myclm/book_list.html', {'books': books})
   else:
       # print("else")
       form = BookForm(instance=book)
   return render(request, 'myclm/book_edit.html', {'form': form})


def book_delete(request, pk):
   customer = get_object_or_404(book, pk=pk)
   customer.delete()
   return redirect('myclm:book_list')


