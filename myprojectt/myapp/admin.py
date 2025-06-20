from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'amount', 'download_pdf_link')

    def download_pdf_link(self, obj):
        url = reverse('generate_package_pdf', args=[obj.pk])
        return format_html('<a class="button" href="{}" target="_blank">Download PDF</a>', url)

    download_pdf_link.short_description = 'Download PDF'

admin.site.register(Package, PackageAdmin)
