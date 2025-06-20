#Morse 2
import re

def decode_bits(bits):
    bits = bits.strip('0')  # Elimina ceros innecesarios al principio y al final
    if not bits:
        return ''
    
    # Encuentra las secuencias de 1s y 0s
    chunks = re.findall(r'(1+|0+)', bits)
    unit = min(len(chunk) for chunk in chunks)  # Duración mínima como unidad de tiempo
    
    # Decodifica usando la unidad
    bits = bits.replace('1' * 3 * unit, '-')
    bits = bits.replace('1' * unit, '.')
    bits = bits.replace('0' * 7 * unit, '   ')
    bits = bits.replace('0' * 3 * unit, ' ')
    bits = bits.replace('0' * unit, '')
    
    return bits

def decode_morse(morse_code):
    words = morse_code.strip().split('   ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE[char] for char in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)