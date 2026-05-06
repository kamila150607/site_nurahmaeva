from django.db import models
from django.urls import reverse


class Client(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    birth_date = models.DateField(verbose_name='Дата рождения')
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Master(models.Model):
    SPECIALIZATION_CHOICES = [
        ('manicure', 'Маникюр'),
        ('pedicure', 'Педикюр'),
        ('both', 'Маникюр и педикюр'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    specialization = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES, verbose_name='Специализация')
    
    def __str__(self):
        return f"{self.full_name} ({self.get_specialization_display()})"
    
    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Price(models.Model):
    procedure_name = models.CharField(max_length=100, verbose_name='Название процедуры')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    
    def __str__(self):
        return f"{self.procedure_name} - {self.price} руб."
    
    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайс'


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждена'),
        ('completed', 'Выполнена'),
        ('cancelled', 'Отменена'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='appointments', verbose_name='Клиент')
    master = models.ForeignKey(Master, on_delete=models.PROTECT, related_name='appointments', verbose_name='Мастер')
    service = models.ForeignKey(Price, on_delete=models.PROTECT, related_name='appointments', verbose_name='Услуга')
    appointment_date = models.DateTimeField(verbose_name='Дата записи')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return f"Запись {self.client.full_name} к {self.master.full_name} на {self.appointment_date}"
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-appointment_date']


class Service(models.Model):
    """Модель услуги"""
    name = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    duration = models.IntegerField('Длительность (мин)', default=60)
    image = models.CharField('Фото услуги', max_length=500, blank=True, null=True)
    is_active = models.BooleanField('Активна', default=True)
    order = models.IntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.price} ₽"

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])


class Review(models.Model):
    """Модель отзыва"""
    RATING_CHOICES = [
        (1, '★ 1'),
        (2, '★ 2'),
        (3, '★ 3'),
        (4, '★ 4'),
        (5, '★ 5'),
    ]

    client_name = models.CharField('Имя клиента', max_length=100)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Услуга')
    master = models.ForeignKey(Master, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Мастер')
    rating = models.IntegerField('Оценка', choices=RATING_CHOICES, default=5)
    comment = models.TextField('Текст отзыва')
    photo = models.CharField('Фото', max_length=500, blank=True, null=True)
    is_approved = models.BooleanField('Одобрено', default=True)
    created_at = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.rating}★"