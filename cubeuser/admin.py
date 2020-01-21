from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from .models import Cubeuser
# Register your models here.
class CubeuserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        ('用户信息', {'fields': ('sex', 'truename', 'idnum', 'picture', 'emergencyname', 'emergencyphone',
                             'birthday', 'address')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'sex', 'truename', 'idnum', 'emergencyname', 'emergencyphone', 'birthday',
                    'address', )

admin.site.register(Cubeuser, CubeuserAdmin)
