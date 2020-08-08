from django.contrib import admin
from .models import Worker

# Register your models here.
@admin.register(Worker) #เหมือนเอาฟังก์ชันนี้มาครอบ จะเรียกอันนี้ก่อน
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'is_availble',
        'primary_phone',
        'secondary_phone',
    )
    list_filter = (
        'is_availble',
    )
