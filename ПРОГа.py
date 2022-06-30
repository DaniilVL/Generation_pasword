import os
sayt=input('Введите адрес сайта: \n')
domen=''
if 'https://' in sayt:
    os.system('start '+ sayt)
elif 'www.' in sayt:
    sayt='https://'+ sayt
    os.system('start '+ sayt)
elif '.com'not in sayt and '.ru' not in sayt:
    domen=input('Введите верхний домен:".ru" or ".com" \n' )
    sayt='https://'+'www.'+sayt+domen
    os.system('start '+ sayt)
else:
    sayt= 'https://'+ sayt
    os.system('start ' + sayt)

