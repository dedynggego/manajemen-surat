
from django.contrib import admin
from websurat.models import Surat, Files 

# Register your models here.
class SuratAdmin(admin.ModelAdmin):
    list_display = ['tgl_surat', 'nomor_surat', 'jenis_surat', 'tujuan', 'perihal', 'mengetahui', 'arsip', 'ket']
    search_field = ['tgl_surat', 'nomor_surat', 'jenis_surat', 'tujuan', 'perihal']
    list_filter = ('jenis_surat',)
    list_per_page = 10

class FormatSuratAdmin(admin.ModelAdmin):
    list_display = ['filename', 'pdf']
    search_field = ['filename', 'pdf']
    

admin.site.register(Surat, SuratAdmin)
admin.site.register(Files, FormatSuratAdmin)
