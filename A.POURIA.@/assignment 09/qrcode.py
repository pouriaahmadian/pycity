import segno
micro_qrcode = segno.make('hi there\nI am pouria\nmy email:pouriaahmadian76@gmail.com', error='q')
micro_qrcode.save('qrcode.png', scale=4, dark='steelblue', data_dark='red')
# حل شد 