#Иерархическая PKI
import RSA

#public_key используется для проверки подписи
#private_key используется для создания подписи дочерних пользователей(RSA)


def signate():
    for dicts in sert:
            for cs_sig in sert:
                 if sert[dicts]['cs'] == sert[cs_sig]['name']:
                     op_key = str(sert[dicts].get('public_key'))                
                     sig = RSA.zash(str(op_key),sert[cs_sig].get('private_key'),sert[cs_sig].get('shared'))
                     sert[dicts].update(signature = sig)
                     print(sert[dicts])


def check_signature(name):
    rez = False
    for dicts in sert:
        if sert[dicts]['name'] == name:
            for cs_sig in sert:
                 if sert[dicts]['cs'] == sert[cs_sig]['name']:
                     op_key = str(sert[dicts].get('public_key'))
                     sig = sert[dicts].get('signature')
                     print(sig)
                     checked_key = RSA.rassh(sig,sert[cs_sig].get('public_key'),sert[cs_sig].get('shared'))
                     if checked_key == op_key:
                         rez = True
                         break
    return rez
                     

def cheсk_whitelist(name):
    rez = False
    for names in whitelist:
        if names == name:
            rez = True
            break
    return rez

def check_pki(name):
    if cheсk_whitelist(name):
        print('Сертификат подлинный')
        return True
    elif check_signature(name):
        for record in sert:
            if sert[record].get('name') == name:
                if check_pki(sert[record].get('cs')):
                    print('Сертификат подлинный')
                    return True
                else:
                    print('Сертификат поддельный')
                    return False
    else:
        print('Сертификат поддельный')
        return False
    
    
    
whitelist = {'Солнце','Млечный путь'}    

    
sert = {}
sert[0] = dict(name = 'Солнце',
               cs = 'Млечный путь',
               public_key =  1242323 ,
               private_key =  6587 ,
               shared = 601723 ,
               signature = 0)
sert[1] = dict(name = 'Земля',
               cs = 'Солнце',
               public_key =  570191 ,
               private_key =  8431 ,
               shared = 157147 ,
               signature = 0)
sert[2] = dict(name = 'Луна',
               cs = 'Земля',
               public_key =  7417531 , 
               private_key = 2611 ,
               shared = 40363 ,
               signature = 0)
sert[3] = dict(name = 'Марс',
               cs = 'Солнце',
               public_key =  9027259 , 
               private_key = 2227 ,
               shared = 55481 ,
               signature = 0)
sert[4] = dict(name = 'Фобос',
               cs = 'Марс',
               public_key = 811859 ,
               private_key = 3611 ,
               shared = 92137,
               signature = 0)
sert[5] = dict(name = 'Деймос',
               cs = 'Марс',
               public_key = 4344641 ,
               private_key = 3785 ,
               shared = 172379 ,
               signature = 1234)
sert[6] = dict(name = 'Венера',
               cs = 'Солнце',
               public_key = 2593441 ,
               private_key = 4321 ,
               shared = 43363 ,
               signature = 0)
sert[7] = dict(name = 'Кеплер-186ф',
               cs = 'Кеплер-186',
               public_key = 5854555 ,
               private_key =  2851 ,
               shared = 50279 ,
               signature = 0)

signate()

for i in sert:
    print('подпись', sert[i].get('name'),': ',sert[i].get('signature'))

for i in sert:
    print('пользователь: ', sert[i].get('name'),'   Центр сертификации: ',sert[i].get('cs'))

print ('Сертификат какого пользователя требуется проверить?')
checked_name = input()
check_pki(checked_name)

