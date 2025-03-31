import base64
import argparse
import os
var = ''	# To store the final string

banner='''
 _______    ______    ______    ______   __    __ 
/       \  /      \  /      \  /      \ /  |  /  |
$$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$ |  $$ |
$$ |__$$ |$$ ___$$ |$$____$$ |$$ \__$$/ $$ |__$$ |
$$    $$<   /   $$<  /    $$/ $$      \ $$    $$ |
$$$$$$$  | _$$$$$  |/$$$$$$/  $$$$$$$  |$$$$$$$$ |
$$ |__$$ |/  \__$$ |$$ |_____ $$ \__$$ |      $$ |
$$    $$/ $$    $$/ $$       |$$    $$/       $$ |
$$$$$$$/   $$$$$$/  $$$$$$$$/  $$$$$$/        $$/ 
==================================================
Code By : Aniket.N.Bhagwate     ~NullByte007                                                  
==================================================                                                                                                                              
'''

def brute(filename):
	
	f = open(filename,'r')
	f = f.read()
	f = f.replace("\n",'')
	flag=0
	f = f.encode()
	def b32(x):
		global var
		f=base64.b32decode(x)
		var = f
		check(f)		

	def b64(x):
		global var
		f=base64.b64decode(x)
		var = f
		check(f)
	
	def check(f):
		f = f.decode()
		
		# Logic 1
		
		for x in f:
			if x.isupper() or str(x).isdigit() or x=='=' or x==' ':
				flag=32
			else:
				flag=64
				break
		
		"""
		# Logic 2
		for x in f:
			if x.islower():
				flag=64
			else:
				flag=32
		"""	

		if flag==32:
			b32(f)
		elif flag==64:
			b64(f)


	try:
		check(f)
	except:
		print(banner)
		print("\033[30;42m ======================================================================= \033[m")
		print("[*] DECODED STRING  : ==>  \033[30;42;5m {}   \033[m <==".format(var.decode()))
		print("\033[30;42m ======================================================================= \033[m\n")
		os.system("rm temp.txt")


def main():

	parser = argparse.ArgumentParser("A Tool to decrypt multiple layers of Base64 and Base32 Encodings ! \n")
	parser.add_argument('-f','--filename',metavar='',required=True,help='The file containing ')
	args = parser.parse_args()
	os.system("cp " + str(args.filename) + " temp.txt")
	brute("temp.txt")



if __name__=='__main__':

	try:
		main()
		
	except:	
		print("[*] UNABLE TO DECODE DATA; UNIDENTIFIED ENCODING !")	
		
