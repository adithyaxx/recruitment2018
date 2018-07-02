import gmpy

p=109959879917114177372722336861203345095333253382752104822919650394398987786677
q=90561430319086504851038952437046741869520660419185636067263109892865601959751
e=65537
c=4502850522123443758723560360296881776932356646069345906178238562865940870942939896446764319588885177791496343618588029123008885269278099884365040931304772
n = p * q
phi = (p-1) * (q-1)
d = gmpy.invert(e, phi)
m = hex(pow(c,d,n))[2:]
print m