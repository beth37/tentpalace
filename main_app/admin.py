from django.contrib import admin

from main_app.models import Customer


# Register your models here.
admin.site.site_header = "St Anthony High School"




class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone"]
    search_fields = ["first_name", "last_name", "phone"]
    list_filter = ["email"]


admin.site.register(Customer, CustomerAdmin)




