"""
URL configuration for tentpalace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tentpalace import settings
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('login', views.signin, name="login"),

                  path('logout', views.signout, name="logout"),
                  path('show', views.show_customers, name="home"),
                  path('search', views.customers_search, name="search"),
                  path('show/<int:id>', views.details, name="details"),
                  path('customers/delete/<int:customer_id>', views.delete_customer, name="delete"),
                  path('customers/update/<int:customer_id>', views.update_customer, name="update"),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# admin@gmail.com
# admin
# 1234
