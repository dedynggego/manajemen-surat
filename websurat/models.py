from django.db import models
from websurat.waktu import *
# Create your models here.


class Surat(models.Model):

    pilihan = (
        ('/D/ATIDP/', 'Direktur'),
        ('/WD/ATIDP/', 'Wakil Direktur'),
        ('/TMS/ATIDP/', 'Mesin Otomotif'),
        ('/TSP/ATIDP/', 'Teknik Sipil'),
        ('/ELK/ATIDP/', 'Teknik Elektronika'),
        ('/AKD/ATIDP/', 'Akademik'),
        ('/KMS/ATIDP/', 'Kemahasiswaan'),
        ('/LPM/ATIDP/', 'LPM'),
        ('/LPPM/ATIDP/', 'LPPM'),
        ('/SR.PR/ATIDP/', 'Sarana Prasarana'),
        ('/KJS/ATIDP/', 'Kerja Sama'),
        ('/SDM/ATIDP/', 'Sumber Daya Manusia'),
        ('/ADM/ATIDP/', 'Administrasi Umum'),
        ('/PMB/ATIDP/', 'PMB'),
    )

    bulan = (
        ('I/'+str(waktu.year), 'I'),
        ('II/'+str(waktu.year), 'II'),
        ('III/'+str(waktu.year), 'III'),
        ('IV/'+str(waktu.year), 'IV'),
        ('V/'+str(waktu.year), 'V'),
        ('VI/'+str(waktu.year), 'VI'),
        ('VII/'+str(waktu.year), 'VII'),
        ('VIII/'+str(waktu.year), 'VIII'),
        ('IX/'+str(waktu.year), 'IX'),
        ('X/'+str(waktu.year), 'X'),
        ('XI/'+str(waktu.year), 'XI'),
        ('XII/'+str(waktu.year), 'XII'),

    )

    # nomor surat: 31/D/ATIDP/II/2022

    tgl_surat = models.CharField(max_length=50, null=True, blank=True)
    nomor_surat = models.CharField(max_length=4, null=True, unique=True)
    kode_surat = models.CharField(max_length=50, null=True, choices=pilihan)
    bulan_surat = models.CharField(max_length=50, null=True, choices=bulan)
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
    pdf = models.FileField(upload_to='doc')

    def __str__(self):
        return self.filename

    # def delete(self, *args, **kwargs):
    #     self.pdf.delete()
    #     super().delete(*args, **kwargs)
