from django import contrib
from django.shortcuts import render, redirect
from pytz import timezone
from websurat.models import Surat, Files
from websurat.forms import FormSuratKeluar, UploadFiles
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.conf import settings
from django.http import HttpResponse
import xlwt
import datetime

waktu = datetime.datetime.now(tz=timezone('Asia/Makassar'))
hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
tanggal = waktu.strftime("%d %B %Y")

def home(request):
    surat = Surat.objects.all()
    format = Files.objects.all()

    konteks={
        'surat':len(surat),
        'format':len(format),
        'user': request.user,
        'waktu': f'{hari[int(waktu.strftime("%w"))]}, {tanggal}',
    }
    return render(request, 'home.html', konteks)

# @login_required(login_url=settings.LOGIN_URL)
def surat_keluar(request):

    surat = Surat.objects.all().order_by('-id')
    form = FormSuratKeluar()
    # p = Paginator(surat, 10)

    # page_num = request.GET.get('page', 1)
    print(request.user)

    template_name = None
    if request.user.is_authenticated:
        template_name = 'surat-keluar-admin.html'
    else:
        template_name = 'surat-keluar.html'

    # try:
    #     page = p.page(page_num)
    # except EmptyPage:
    #     page = p.page(1)

    if request.POST:
        form = FormSuratKeluar(request.POST)
        if form.is_valid():

            form.save()
            form = FormSuratKeluar()
            messages.success(request, "Data berhasil disimpan")
        else:
            messages.error(request, 'Nomor surat sudah ada')
        return redirect('surat_keluar')
    else:
        form = FormSuratKeluar()

    konteks={
        # 'surat': page,
        'surat':surat,
        'form':form,
        'menu': 'surat keluar',
        'waktu': f'{hari[int(waktu.strftime("%w"))]}, {tanggal}',
    }

    return render(request, template_name, konteks)

def ubah_surat_keluar(request, id_surat):
    surat = Surat.objects.get(id=id_surat)
    form = FormSuratKeluar(instance=surat)
    
    if request.method == 'POST':
        form = FormSuratKeluar(request.POST or None, instance=surat)
        form.save()
        form = FormSuratKeluar()
        messages.success(request, "Data berhasil diperbaharui")
        return redirect('surat_keluar')

    konteks ={
        'form':form,
        'surat':surat,
        'waktu': f'{hari[int(waktu.strftime("%w"))]}, {tanggal}',
    }
    return render(request, 'ubah-surat.html', konteks) 


def hapus(request, id_surat):
    surat = Surat.objects.filter(id=id_surat)
    surat.delete()
    return  redirect('surat_keluar')

def hapus_format_surat(request, id_format):
    format = Files.objects.filter(id=id_format)
    format.delete()
    return redirect('format_surat')


def surat_masuk(request):
    konteks = {
        'menu': 'surat masuk',
        'waktu': f'{hari[int(waktu.strftime("%w"))]}, {tanggal}',
    }
    return render(request, 'surat-masuk.html', konteks)

def format_surat(request):

    template_name = None
    if request.user.is_authenticated:
        template_name = 'format-surat-admin.html'
    else:
        template_name = 'format-surat.html'

    file = Files.objects.all().order_by('id')
    form = UploadFiles()

    if request.method == 'POST':
        form = UploadFiles(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        form = UploadFiles()
        messages.success(request, "Data berhasil disimpan")
        return redirect('format_surat')
    else:
        form = UploadFiles()
        # messages.error(request, "Data gagal disimpan")

    konteks = {
        'file':file,
        'form':form,
        'menu':'format',
        'waktu': f'{hari[int(waktu.strftime("%w"))]}, {tanggal}',
    }
    return render(request, template_name, konteks)

def loginView(request):
    context = {
		'page_title':'LOGIN',
	}
    user = None

    if request.method == "GET":
        if request.user.is_authenticated:
			# logika untuk user
            return redirect('surat_keluar')
        else:
			# logika untuk anonymous
            return render(request, 'registration/login.html', context)

    if request.method == "POST":
		
        username_login = request.POST['username']
        password_login = request.POST['password']
		
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('surat_keluar')
        else:
            return redirect('masuk')
		
    return render(request, 'registration/login.html', context)

@login_required
def logoutView(request):

	logout(request)
	return redirect ('home')

def cari(request):
    template_name = None
    if request.method == 'POST':
        search = request.POST['search']
        surat = Surat.objects.filter(nomor_surat__contains=search)
        if request.user.is_authenticated:
            template_name = 'surat-keluar-admin.html'
        else:
            template_name = 'surat-keluar.html'
    return render(request, template_name, 
            {'search':search,
              'surat':surat })    
    
def export_surat_keluar_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Backup-' + str(waktu)+'.xls'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Backup')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Tgl Surat', 'Nomor Surat', 'Kode Surat', 'Jenis Surat', 'Tujuan', 'Perihal', 'Mengetahui', 'Arsip', 'Ket']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    
    rows = Surat.objects.all().values_list('tgl_surat', 'nomor_surat', 'kode_surat','jenis_surat', 'tujuan', 'perihal', 'mengetahui', 'arsip','ket')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response

