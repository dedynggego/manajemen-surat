from django.contrib import admin
from django.urls import path
from websurat.views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('surat-keluar/', surat_keluar, name='surat_keluar'),
    path('surat-masuk/', surat_masuk, name='surat_masuk'),
    path('format-surat/', format_surat, name='format_surat'),
    path('surat-keluar/ubah/<int:id_surat>', ubah_surat_keluar, name='ubah_surat'),
    path('surat-keluar/hapus/<int:id_surat>', hapus, name='hapus_surat'),
    path('format-surat/hapus-format/<int:id_format>', hapus_format_surat, name='hapus_format'),
    path('masuk/', loginView, name="masuk"),
    path('keluar/', logoutView, name='keluar'),
    path('cari/', cari, name='cari'),
    path('export-surat-keluar/', export_surat_keluar_xls, name='export_surat_keluar_xls'),
]
