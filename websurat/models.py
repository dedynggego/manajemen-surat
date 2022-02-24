from django.db import models
from websurat.waktu import *
# Create your models here.
class Surat(models.Model):
    
    pilihan = (
        ('/D/ATIDP/'+bulan+'/'+str(waktu.year), 'Direktur'),
        ('/WD/ATIDP/'+bulan+'/'+str(waktu.year), 'Wakil Direktur'),
        ('/TMS/ATIDP/'+bulan+'/'+str(waktu.year), 'Mesin Otomotif'),
        ('/TSP/ATIDP/'+bulan+'/'+str(waktu.year), 'Teknik Sipil'),
        ('/W', 'Elektronika?'),
    )
 
    #nomor surat: 31/D/ATIDP/II/2022

    tgl_surat = models.CharField(max_length=50, null=True, blank=True)
    nomor_surat = models.CharField(max_length=4, null=True, unique=True)
    kode_surat = models.CharField(max_length=50,null=True, choices=pilihan)
    jenis_surat = models.CharField(max_length=50, null=True, blank=True)
    tujuan = models.CharField(max_length=50, null=True, blank=True)
    perihal = models.CharField(max_length=200, null=True, blank=True)
    mengetahui = models.CharField(max_length=50, null=True, blank=True)
    arsip = models.CharField(max_length=50, null=True, blank=True)
    ket = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.tgl_surat

class Files(models.Model):
    filename = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='static/doc/')

    def __str__(self):
        return self.filename

    # def delete(self, *args, **kwargs):
    #     self.pdf.delete()
    #     super().delete(*args, **kwargs) 
    



