print('Hello World')
print(sorted('Oliver'))
print(sorted('🥚🐔'))

print('____________________________________________')

print(26)       # Zeige 26 in Dezimalzahlen an
print(bin(26))  # Zeige 26 in Binärzahlen an (das '0b' davor ist nur ein Marker für binär)

print(oct(26)) # Oktalzahlen
print(hex(26)) # Hexadezimalzahlen

print('____________________________________________')

print('A')              # Zeige das A an
print(ord('A'))         # Zeige die ASCII/UTF-8-Zahl von A an

print()                 # Gib eine Leerzeile aus (nur für bessere Lesbarkeit)

print('Ä')              # s.o. nur für Ä
print(ord('Ä'))

print('____________________________________________')

print('A')          # Zeige ein A an
print('\u0308')     # Zeige das Umlautzeichen am Code-Point \u0308 an
print('A\u0308')    # Zeige die Kombination beider Zeichen an
print()
print(ord('A'))
print(ord('\u0308'))
print()
print(hex(ord('\u0308'))) # Zeige das Umlautzeichen in hexadezimal an, was dann 308 ist (mit dem Hexadezimal-Marker 0x)

print('____________________________________________')

print(len('Ä'))         # Das Ä mit der Tastatur getippt
print(len('Ä'))         # Das vom Output oben rauskopierte Ä
print(len('A\u0308'))   # Die Kombination wie oben

print('____________________________________________')

print("ä")
print(ord("ä"))
print(bin(ord('ä'))) # funktioniert das?

print('____________________________________________')

b = bytes('ä', encoding='UTF-8')    # wir speichern das Ergebnis der bytes()-Funktion in der Variable b
print(b)                            # b anzeigen (hexadezimal)

print([bin(byte) for byte in b])    # jedes Byte in b in binär umgewandelt anzeigen

print('____________________________________________')

print('😁')                                                     # Zeige Zeichen an
print(ord('😁'))                                                # Zeige Unicode-Code-Point an
print(len('😁'))                                                # Länge des Zeichens
print([bin(byte) for byte in bytes('😁', encoding='UTF-8')])    # Byte-Sequenz in UTF-8^

print('____________________________________________')

print('🐔')                                                     # Zeige Zeichen an
print(ord('🐔'))                                                # Zeige Unicode-Code-Point an
print(len('🐔'))                                                # Länge des Zeichens
print([bin(byte) for byte in bytes('🐔', encoding='UTF-8')])    # Byte-Sequenz in UTF-8

print('____________________________________________')

print('🥚')                                                     # Zeige Zeichen an
print(ord('🥚'))                                                # Zeige Unicode-Code-Point an
print(len('🥚'))                                                # Länge des Zeichens
print([bin(byte) for byte in bytes('🥚', encoding='UTF-8')])    # Byte-Sequenz in UTF-8

print('____________________________________________')

print(ord('🐔') < ord('🥚'))

print('____________________________________________')

print('🥺', len('🥺')) # Emoji und die Länge des Emojis anzeigen
print('👨🏼', len('👨🏼'))
print('🤷', len('🤷'))
print('🤷‍♀️', len('🤷‍♀️'))
print('🤷🏼‍♀️', len('🤷🏼‍♀️'))

print('____________________________________________')

# Familien

print('👪', len('👪'))
print('👩‍👦', len('👩‍👦'))
print('👨‍👨‍👦‍👦', len('👨‍👨‍👦‍👦'))
print('👨‍👩‍👧‍👦', len('👨‍👩‍👧‍👦'))
print('👨🏾‍👩🏼‍👧🏽‍👦🏿', len('👨🏾‍👩🏼‍👧🏽‍👦🏿'))

print('____________________________________________')