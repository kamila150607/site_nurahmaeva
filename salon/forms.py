from django import forms
from .models import Client, Master, Price, Appointment, Review


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'phone_number', 'birth_date']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (XXX) XXX-XX-XX'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'full_name': 'ФИО',
            'phone_number': 'Номер телефона',
            'birth_date': 'Дата рождения',
        }


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['full_name', 'phone_number', 'specialization']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО мастера'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (XXX) XXX-XX-XX'}),
            'specialization': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'full_name': 'ФИО',
            'phone_number': 'Номер телефона',
            'specialization': 'Специализация',
        }


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['procedure_name', 'price']
        widgets = {
            'procedure_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название услуги'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена в рублях'}),
        }
        labels = {
            'procedure_name': 'Название процедуры',
            'price': 'Цена (руб.)',
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'master', 'service', 'appointment_date', 'status']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'client': 'Клиент',
            'master': 'Мастер',
            'service': 'Услуга',
            'appointment_date': 'Дата и время',
            'status': 'Статус',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['client_name', 'service', 'master', 'rating', 'comment', 'photo']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваш отзыв'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'client_name': 'Ваше имя',
            'service': 'Услуга',
            'master': 'Мастер',
            'rating': 'Оценка',
            'comment': 'Отзыв',
            'photo': 'Фото',
        }