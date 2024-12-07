disketa = 1.44
pages = 100
strk = 50
sym = 25
bytes_sym = 4

# Найдем доступный объем дискеты в байтах
all_bytes = (disketa * 1024)*1024

# Кол-во байт для символов в одной строке
bytes_strk = sym * bytes_sym

# Кол-во байт на одну страницу
bytes_pages = bytes_strk * strk

# Кол-во байт на одну книгу
bytes_book = bytes_pages * pages

# Кол-во книг, которые можно поместить на дискету в 1,44 Мб
books = all_bytes/bytes_book
print("Количество книг, помещающихся на дискету:", round(books))
