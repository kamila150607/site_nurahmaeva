from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Count
from .models import Client, Master, Price, Appointment, Service, Review
from .forms import ClientForm, MasterForm, PriceForm, AppointmentForm, ReviewForm


def index(request):
    total_appointments = Appointment.objects.count()
    pending_appointments = Appointment.objects.filter(status='pending').count()
    completed_appointments = Appointment.objects.filter(status='completed').count()
    total_clients = Client.objects.count()
    total_masters = Master.objects.count()
    
    recent_appointments = Appointment.objects.select_related('client', 'master', 'service').order_by('-appointment_date')[:5]
    
    popular_services = Price.objects.annotate(
        appointments_count=Count('appointments')
    ).order_by('-appointments_count')[:3]
    
    context = {
        'total_appointments': total_appointments,
        'pending_appointments': pending_appointments,
        'completed_appointments': completed_appointments,
        'total_clients': total_clients,
        'total_masters': total_masters,
        'recent_appointments': recent_appointments,
        'popular_services': popular_services,
    }
    return render(request, 'salon/index.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'salon/client_list.html'
    context_object_name = 'clients'
    ordering = ['full_name']


class ClientDetailView(DetailView):
    model = Client
    template_name = 'salon/client_detail.html'
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = self.object.appointments.select_related('master', 'service').all()
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'salon/client_form.html'
    success_url = reverse_lazy('client_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✅ Клиент успешно добавлен!')
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'salon/client_form.html'
    success_url = reverse_lazy('client_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✏️ Данные клиента успешно обновлены!')
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'salon/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '🗑️ Клиент успешно удален!')
        return super().delete(request, *args, **kwargs)


class MasterListView(ListView):
    model = Master
    template_name = 'salon/master_list.html'
    context_object_name = 'masters'
    ordering = ['full_name']


class MasterDetailView(DetailView):
    model = Master
    template_name = 'salon/master_detail.html'
    context_object_name = 'master'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = self.object.appointments.select_related('client', 'service').all()
        return context


class MasterCreateView(CreateView):
    model = Master
    form_class = MasterForm
    template_name = 'salon/master_form.html'
    success_url = reverse_lazy('master_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✅ Мастер успешно добавлен!')
        return super().form_valid(form)


class MasterUpdateView(UpdateView):
    model = Master
    form_class = MasterForm
    template_name = 'salon/master_form.html'
    success_url = reverse_lazy('master_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✏️ Данные мастера успешно обновлены!')
        return super().form_valid(form)


class MasterDeleteView(DeleteView):
    model = Master
    template_name = 'salon/master_confirm_delete.html'
    success_url = reverse_lazy('master_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '🗑️ Мастер успешно удален!')
        return super().delete(request, *args, **kwargs)


class PriceListView(ListView):
    model = Price
    template_name = 'salon/price_list.html'
    context_object_name = 'services'
    ordering = ['procedure_name']


class PriceDetailView(DetailView):
    model = Price
    template_name = 'salon/price_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = self.object.appointments.select_related('client', 'master').all()
        return context


class PriceCreateView(CreateView):
    model = Price
    form_class = PriceForm
    template_name = 'salon/price_form.html'
    success_url = reverse_lazy('price_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✅ Услуга успешно добавлена!')
        return super().form_valid(form)


class PriceUpdateView(UpdateView):
    model = Price
    form_class = PriceForm
    template_name = 'salon/price_form.html'
    success_url = reverse_lazy('price_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✏️ Услуга успешно обновлена!')
        return super().form_valid(form)


class PriceDeleteView(DeleteView):
    model = Price
    template_name = 'salon/price_confirm_delete.html'
    success_url = reverse_lazy('price_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '🗑️ Услуга успешно удалена!')
        return super().delete(request, *args, **kwargs)


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'salon/appointment_list.html'
    context_object_name = 'appointments'
    ordering = ['-appointment_date']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset.select_related('client', 'master', 'service')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = [
            ('all', 'Все'),
            ('pending', 'Ожидает'),
            ('confirmed', 'Подтверждена'),
            ('completed', 'Выполнена'),
            ('cancelled', 'Отменена'),
        ]
        context['current_status'] = self.request.GET.get('status', 'all')
        return context


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'salon/appointment_detail.html'
    context_object_name = 'appointment'


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'salon/appointment_form.html'
    success_url = reverse_lazy('appointment_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✅ Запись успешно создана!')
        return super().form_valid(form)


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'salon/appointment_form.html'
    success_url = reverse_lazy('appointment_list')
    
    def form_valid(self, form):
        messages.success(self.request, '✏️ Запись успешно обновлена!')
        return super().form_valid(form)


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'salon/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '🗑️ Запись успешно удалена!')
        return super().delete(request, *args, **kwargs)


def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'salon/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    masters = Master.objects.all()
    reviews = Review.objects.filter(is_approved=True, service=service)[:5]
    return render(request, 'salon/service_detail.html', {
        'service': service,
        'masters': masters,
        'reviews': reviews,
    })


def review_list(request):
    reviews = Review.objects.filter(is_approved=True)
    return render(request, 'salon/review_list.html', {'reviews': reviews})


def add_review(request, service_id=None):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        initial = {}
        if service_id:
            initial['service'] = service_id
        form = ReviewForm(initial=initial)
    return render(request, 'salon/review_form.html', {'form': form})