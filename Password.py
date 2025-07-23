def length(x):
    return len(x) > 8

def upper(x):
    return any(char.isupper() for char in x)

def lower(x):
    return any(char.islower() for char in x)

def special(x):
    return any(not char.isalnum() for char in x)

def common(x):
    popular = [
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "password123",
        "111111", "123123", "admin", "letmein", "welcome",
        "monkey", "1234", "dragon", "sunshine", "master",
        "123321", "654321", "batman", "trustno1", "qwerty123",
        "football", "baseball", "princess", "welcome123", "shadow",
        "superman", "michael", "ninja", "mustang", "charlie",
        "ashley", "bailey", "password1", "000000", "jordan23",
        "harley", "robert", "matthew", "jordan", "hunter",
        "tigger", "hockey", "ranger", "buster", "iloveyou",
        "thomas", "daniel", "hannah", "samsung", "cookie",
        "banana", "qwerty12", "orange", "summer", "flower",
        "computer", "hello", "freedom", "nothing", "pepper",
        "google", "lovely", "access", "696969", "987654321",
        "8675309", "passw0rd", "1q2w3e4r", "1qaz2wsx", "zxcvbnm",
        "starwars", "monster", "martin", "justin", "ginger",
        "killer", "jennifer", "london", "purple", "silver",
        "cheese", "sophie", "security", "123qwe", "default",
        "test", "guest", "pokemon"
    ]
    x = x.lower()
    return any(y in x for y in popular)

def check(x):
    score = 0
    if length(x):
        score += 3     
    if upper(x):
        score += 2     
    if lower(x):
        score += 1
    if special(x):
        score += 2     
    if not common(x):
        score += 1

    if score >= 8:
        return "The password is very strong"
    elif score >= 6:
        return "The password is strong"
    elif score >= 4:
        return "The password is average"
    elif score >= 2:
        return "The password is weak"
    else:
        return "The password is very weak"

password = input("Enter Your Password: ")
print(check(password))
