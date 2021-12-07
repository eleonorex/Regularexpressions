import re, regex

with open("./flats.txt", "r") as file:
    spisok = file.readlines()

rooms = []
metro = []
phone_numbers = []
price = []
address = []
for line in spisok:
    rooms.extend(re.findall(r"\d[ -]комн", line))

    metro.extend(re.findall(r"([мМ]\.[А-Я][а-яА-Я]*|[А-Я][а-яА-Я]*\s[мМ]\.)", line))

    phone_numbers.extend(re.findall(r"[0-9]{3}[ .-]?[0-9]{2}[ .-]?[0-9]{2}", line))

    price.extend(re.findall(r"((?:[0-9][0-9,.\s]*)[\s,.]?\s?(?:тыс\.?)?\s?(?:\$|дол))", line))

    address.extend(re.findall(
        r"((?:(?:ул|пер)[.\s]+[а-яА-Я\s.]+|[а-яА-Я\s.]+\s(?:ул|пер).?\s?)[,\s.]+(?:дом|д.)?\s?(?:\d+[\d\/]*(?!\sкв.м)(?=[\s,;.]))?|[а-яА-Я\s.]+\s?(?:ул|пер)?.?[,\s.]+(?:дом|д)[\s,.]?\d+[\d\/]*)",
        line))

print(rooms)
print(metro)
print(phone_numbers)
print(price)
print(address)
