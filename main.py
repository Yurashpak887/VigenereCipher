class VigenereCipher:
    def __init__(self, alphabet=None, dictionary=None):
        # ініціалізуємо атрибути класу: алфавіт, словник типових слів мови та ключ
        # якщо алфавіт або словник не задані, вони приймають значення за замовчуванням
        self.alphabet = alphabet or 'abcdefghijklmnopqrstuvwxyz'
        self.dictionary = dictionary or set()
        self.key = None

    def set_key(self, key):
        self.key = key

    def is_valid_key(self, key):
        # перевіряємо, чи ключ складається тільки зі слів, які є в словнику
        return all(c in self.dictionary for c in key)

    def encrypt(self, plaintext):
        # шифруємо повідомлення з використанням ключа
        ciphertext = ''
        key_index = 0
        for c in plaintext:
            if c in self.alphabet:
                # визначаємо зсув за допомогою позиції літери в ключі
                shift = self.alphabet.index(self.key[key_index])
                # шифруємо літеру за допомогою зсуву
                ciphertext += self.alphabet[(self.alphabet.index(c) + shift) % len(self.alphabet)]
                # переходимо до наступної літери в ключі
                key_index = (key_index + 1) % len(self.key)
            else:
                # якщо символ не є літерою, додаємо його без змін
                ciphertext += c
        return ciphertext

    def decrypt(self, ciphertext):
        # дешифруємо повідомлення з використанням ключа
        plaintext = ''
        key_index = 0
        for c in ciphertext:
            if c in self.alphabet:
                # визначаємо зсув за допомогою позиції літери в ключі
                shift = self.alphabet.index(self.key[key_index])
                # дешифруємо літеру за допомогою зсуву
                plaintext += self.alphabet[(self.alphabet.index(c) - shift) % len(self.alphabet)]
                # переходимо до наступної літери в ключі
                key_index = (key_index + 1) % len(self.key)
            else:
                # якщо символ не є літерою, додаємо його без змін
                plaintext += c
        return plaintext


# створюємо об'єкт шифрувальника
cipher = VigenereCipher(alphabet='abcdefghijklmnopqrstuvwxyz', dictionary={'hello', 'world', 'python'})

# встановлюємо ключ
cipher.set_key('hello')

# шифруємо повідомлення
ciphertext = cipher.encrypt('hello world')
print(ciphertext)  # 'bmnnp wxndl'

# дешифруємо повідомлення
plaintext = cipher.decrypt(ciphertext)
print(plaintext)  # 'hello world'
