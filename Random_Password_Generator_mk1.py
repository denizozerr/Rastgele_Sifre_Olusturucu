
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&','*', '+','.','?']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

noktasiz=''
for rastgele_harf in range(nr_letters):
    rastgele_harf = random.choice(letters)
    noktasiz += rastgele_harf

for rastgele_sembol in range(nr_symbols):
    rastgele_sembol = random.choice(symbols)
    noktasiz += rastgele_sembol

for rastgele_sayi in range(nr_numbers):
    rastgele_sayi = random.choice(numbers)
    noktasiz += rastgele_sayi
son=''
for karistirici in range(len(noktasiz)):
    karistirici = random.choice(noktasiz)
    son+= karistirici
print(son)