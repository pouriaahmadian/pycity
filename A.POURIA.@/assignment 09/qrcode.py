import segn
micro_qrcode = segn.make('hi there\nI am pouria\nmy email:pouriaahmadian76@gmail.com', error='q')
micro_qrcode.save('qrcode.png', scale=4, dark='steelblue', data_dark='purple')