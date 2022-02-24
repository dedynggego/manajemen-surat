import datetime
from pytz import timezone

waktu = datetime.datetime.now(tz=timezone('Asia/Makassar'))

if waktu.strftime("%m") == '01':
    bulan = 'I'
elif waktu.strftime("%m") == '02':
    bulan = 'II'
elif waktu.strftime("%m") == '03':
    bulan = 'III'
elif waktu.strftime("%m") == '04':
    bulan = 'IV'
elif waktu.strftime("%m") == '05':
    bulan = 'V'
elif waktu.strftime("%m") == '06':
    bulan = 'VI'
elif waktu.strftime("%m") == '07':
    bulan = 'VII'
elif waktu.strftime("%m") == '08':
    bulan = 'VIII'
elif waktu.strftime("%m") == '09':
    bulan = 'IX'
elif waktu.strftime("%m") == '10':
    bulan = 'X'
elif waktu.strftime("%m") == '11':
    bulan = 'XI'
else:
    bulan = 'XII'
