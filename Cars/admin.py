from django.contrib import admin

from .models import RentalCar, Car



@admin.register(RentalCar)
class RentalCarAdmin(admin.ModelAdmin):
    list_display = ('rental_company_name', 'rental_company_address', 'rental_company_phone', 'rental_company_cnpj')



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_maker', 'car_model', 'car_year', 'car_mileage', 'car_daily_price', 'car_rental', 'car_color', 'car_image')

