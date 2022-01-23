import re
regex = r"[0-9]{16}|(([0-9]{4}\S){3}[0-9]{4})|(-([0-9]{4}\S){3}[0-9]{4})(.)\1{4}"
tarjetas = ['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
for example in tarjetas:
    if re.match(regex, example):
        print("Valid".format(tarjeta_example=example))
    else:
        print("Invalid".format(tarjeta_example=example))