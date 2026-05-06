from django import template

register = template.Library()

@register.filter
def get_status_color(status):
    """Возвращает цвет для статуса записи"""
    colors = {
        'pending': '#ff9800',     # оранжевый
        'confirmed': '#4caf50',   # зеленый
        'completed': '#2196f3',   # синий
        'cancelled': '#f44336',   # красный
    }
    return colors.get(status, '#999')

@register.filter
def get_status_text(status):
    """Возвращает текст статуса на русском"""
    texts = {
        'pending': 'Ожидает подтверждения',
        'confirmed': 'Подтверждена',
        'completed': 'Выполнена',
        'cancelled': 'Отменена',
    }
    return texts.get(status, status)