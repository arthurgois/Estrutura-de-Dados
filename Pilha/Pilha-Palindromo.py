frase = str(input()).strip().lower()
frase = frase.split()
frase = ''.join(frase)
frase = frase.replace(',','')

rev = frase[::-1]

if frase == rev:
    print("True")
else:
    print("False")