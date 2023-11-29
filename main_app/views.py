from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.app_forms import CustomerForm, LoginForm
from main_app.models import Customer


# Create your views here.
@login_required  # decorators
@permission_required('main_app.add_student')
def customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User saved successfully")
            return redirect("home")
    else:
        form = CustomerForm()

    return render(request, "customers.html", {"form": form})


@login_required
@permission_required('main_app.view_customer')
def show_customers(request, ):
    data = Customer.objects.all()  # select * FROM customers
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    return render(request, "display.html", {"customers": data})


@login_required
def details(request, id):
    student = Customer.objects.get(pk=id)
    return render(request, "details.html", {"customer": student})


@login_required
@permission_required('main_app.delete_customer')  # <your app name>, <action>, <model>
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    messages.info(request, f"Student {customer.first_name} was deleted successfully")
    return redirect("show")


@login_required
def customers_search(request, ):
    search = request.GET["search"]
    data = Customer.objects.filter(Q(first_name__icontains=search)
                                  | Q(last_name__icontains=search)
                                  | Q(email__contains=search)
                                  )

    if search.isnumeric():
        score = int(search)
        data = Customer.objects.filter(kcpe_score=score)

        paginator = Paginator(data, 10)
        page_number = request.GET.get("page")
        data = paginator.get_page(page_number)

    return render(request, "display.html", {"customers": data})


# elastic search


@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated customer {customer.first_name}")
            return redirect("details", customer_id)

    else:
        form = CustomerForm(instance=customer)
        return render(request, "update.html", {"form": form})


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Signed in successfully")
                return redirect('home')
        messages.error(request, "Invalid username or password")
        return render(request, "login.html", {"form": form})


def signout(request):
    messages.success(request, "You have logged out!")
    logout(request)  # will kill all the sessions and cookies
    return redirect('login')

# editor user 123456 will have all the powers
# desk one user 123456 oly see and edit but not delete a student
# hr user 123456 just see

# Groups of users; editor group, desk one group and hr group


