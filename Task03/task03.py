# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/Кодированиедлинсерий
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

def encode_string(imp_string: str) -> str:
    encoded_string = ""
    i = 0
    while (i <= len(imp_string)-1):
        counter = 1
        character = imp_string[i]
        j = i
        while (j < len(imp_string)-1): 
                if (imp_string[j] == imp_string[j + 1]): 
                    counter += 1
                    j += 1
                else: break
        encoded_string = encoded_string + str(counter) + character
        i = j + 1
    return encoded_string

def decode_string(imp_string: str) -> str:
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(imp_string) - 1):
        idx_counter = int(imp_string[i])
        character = imp_string[i + 1]
        for j in range(idx_counter):
            decoded_message = decoded_message + character
            j = j + 1
        i = i + 2
    return decoded_message

text_string = "WWJJJHDDDDDPPGRRR"
print(f"Исходная строка: {text_string}")
en_text = encode_string(text_string)
print(f"Закодированная строка: {en_text}")
dec_text = decode_string(en_text)
print(f"Декодированная строка: {dec_text}")