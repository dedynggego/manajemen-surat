# Generated by Django 3.2.9 on 2022-03-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websurat', '0009_auto_20220207_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='kode_surat',
            field=models.CharField(choices=[('/D/ATIDP/III/2022', 'Direktur'), ('/WD/ATIDP/III/2022', 'Wakil Direktur'), ('/TMS/ATIDP/III/2022', 'Mesin Otomotif'), ('/TSP/ATIDP/III/2022', 'Teknik Sipil'), ('/ELK/ATIDP/III/2022', 'Teknik Elektronika'), ('/AKD/ATIDP/III/2022', 'Akademik'), ('/KMS/ATIDP/III/2022', 'Kemahasiswaan'), ('/LPM/ATIDP/III/2022', 'LPM'), ('/LPPM/ATIDP/III/2022', 'LPPM'), ('/SR.PR/ATIDP/III/2022', 'Sarana Prasarana'), ('/KJS/ATIDP/III/2022', 'Kerja Sama'), ('/SDM/ATIDP/III/2022', 'Sumber Daya Manusia'), ('/ADM/ATIDP/III/2022', 'Administrasi Umum'), ('/PMB/ATIDP/III/2022', 'PMB')], max_length=50, null=True),
        ),
    ]