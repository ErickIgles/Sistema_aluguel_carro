from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
import uuid
from datetime import datetime
from stdimage.models import StdImageField


def validate_year(year):

    year_now = datetime.now().year

    if year > year_now:
        raise  ValidationError('Ano inválido!')
    return year

    
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'  
   
    return filename



class RentalCar(models.Model):
   
    rental_company_name = models.CharField('Nome da locadora', max_length=140)
    rental_company_address = models.CharField('Endereço', max_length=140)
    rental_company_phone = models.CharField('Telefone', max_length=15)
    rental_company_cnpj = models.CharField('CNPJ', max_length=18, unique=True)

   
    class Meta:
        verbose_name = 'Locadora'
        verbose_name_plural = 'Locadoras'


    def __str__(self):
        return f'{self.rental_company_name}'


class Car(models.Model):
    """
        car_maker - Fabricante
        car_model - Modelo
        car_year - Ano de Fabricação
        car_mileage - Kilometragem
        car_daily_price - Valor da diária
        car_rental - Locadora
        car_color - Cor do carro
    """

    car_maker = models.CharField('Fabricante', max_length=140)
    car_model = models.CharField('Modelo', max_length=140)
    car_year = models.IntegerField('Ano', validators=[validate_year])
    car_mileage = models.IntegerField('Kilometragem')
    car_daily_price = models.DecimalField('Valor diário', max_digits=8, decimal_places=2)
    car_rental = models.ForeignKey(RentalCar, on_delete=models.CASCADE, verbose_name='Locadora')
    car_color = models.CharField('Cor', max_length=140)
    car_image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':400, 'height':480, 'crop':True}})


    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    
    def __str__(self):
        return f'{self.car_model} {self.car_maker}'

