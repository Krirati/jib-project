from django.contrib import admin
from .models import Certificate

# Register your models here.
@admin.register(Certificate) #เหมือนเอาฟังก์ชันนี้มาครอบ จะเรียกอันนี้ก่อน
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'issued_by',
    )
