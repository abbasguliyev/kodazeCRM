import django_filters

from account.models import (
    Customer,
    CustomerNote,
    EmployeeStatus,
    Region,
)
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.models import Permission, Group

class PermissionFilter(django_filters.FilterSet):
    class Meta:
        model = Permission
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'content_type': ['exact'],
            'codename': ['exact', 'icontains']
        }

class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'permissions': ['exact', 'icontains']
        }

class UserFilter(django_filters.FilterSet):
    date_of_birth = django_filters.DateFilter(field_name='date_of_birth', input_formats=["%d-%m-%Y"])
    start_date_of_work = django_filters.DateFilter(field_name='start_date_of_work', input_formats=["%d-%m-%Y"])
    start_date_of_work__gte = django_filters.DateFilter(field_name='start_date_of_work', lookup_expr='gte', input_formats=["%d-%m-%Y"])
    start_date_of_work__lte = django_filters.DateFilter(field_name='start_date_of_work', lookup_expr='lte', input_formats=["%d-%m-%Y"])
    
    dismissal_date = django_filters.DateFilter(field_name='dismissal_date', input_formats=["%d-%m-%Y"])
    dismissal_date__gte = django_filters.DateFilter(field_name='dismissal_date', lookup_expr='gte', input_formats=["%d-%m-%Y"])
    dismissal_date__lte = django_filters.DateFilter(field_name='dismissal_date', lookup_expr='lte', input_formats=["%d-%m-%Y"])
    
    fullname = django_filters.CharFilter(method="fullname")
    supervisor_fullname = django_filters.CharFilter(method="supervisor__fullname")
    
    class Meta:
        model = User
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'phone_number_1': ['exact', 'icontains'],
            'phone_number_2': ['exact', 'icontains'],
            'position__name': ['exact', 'icontains'],
            'position': ['exact'],
            'is_superuser': ['exact'],

            'company__name': ['exact', 'icontains'],
            'office__name': ['exact', 'icontains'],
            'department__name': ['exact', 'icontains'],
            'team__name': ['exact', 'icontains'],
            'supervisor': ['exact'],
            'is_active': ['exact'],
            'employee_status__status_name': ['exact', 'icontains'],
        }

class EmployeeStatusFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeeStatus
        fields = {
            'status_name': ['exact', 'icontains'],
        }

class RegionFilter(django_filters.FilterSet):
    class Meta:
        model = Region
        fields = {
            'region_name': ['exact', 'icontains'],
        }

class CustomerFilter(django_filters.FilterSet):
    fullname = django_filters.CharFilter(method="fullname")
    executor_fullname = django_filters.CharFilter(method="executor__fullname")
    
    class Meta:
        model = Customer
        fields = {
            'phone_number_1': ['exact', 'icontains'],
            'phone_number_2': ['exact', 'icontains'],
            'phone_number_3': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'order_count': ['exact', 'gte', 'lte'],
            'is_active': ['exact'],
            'address': ['exact', 'icontains'],
            'executor': ['exact'],
            'region__region_name': ['exact', 'icontains'],
        }

class CustomerNoteFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', input_formats=["%d-%m-%Y"])
    date__gte = django_filters.DateFilter(field_name='date', lookup_expr='gte', input_formats=["%d-%m-%Y"])
    date__lte = django_filters.DateFilter(field_name='date', lookup_expr='lte', input_formats=["%d-%m-%Y"])
    customer_fullname = django_filters.CharFilter(method="customer__fullname")
    
    class Meta:
        model = CustomerNote
        fields = {
            'customer': ['exact'],
            'customer__phone_number_1': ['exact', 'icontains'],
            'customer__phone_number_2': ['exact', 'icontains'],
            'customer__phone_number_3': ['exact', 'icontains'],
            'customer__email': ['exact', 'icontains'],
            'customer__region__region_name': ['exact', 'icontains'],
            'customer__region': ['exact'],
            'note': ['exact', 'icontains'],
        }