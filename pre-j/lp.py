login, password = [input() for _ in range(2)]
print(bool(len(login) > 4 and len(password) > 8 and not login == password))