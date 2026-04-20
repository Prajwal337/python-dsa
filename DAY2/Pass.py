def has_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_lowercase(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special_char(password, specials="!@#$%^&*"):
    return any(c in specials for c in password)

def analyze_password(password):
    score = 0
    failed_checks = []
    
    if has_min_length(password):
        score += 1
    else:
        failed_checks.append("Length")
        
    if has_uppercase(password):
        score += 1
    else:
        failed_checks.append("Uppercase")
        
    if has_lowercase(password):
        score += 1
    else:
        failed_checks.append("Lowercase")
        
    if has_digit(password):
        score += 1
    else:
        failed_checks.append("Digit")
        
    if has_special_char(password):
        score += 1
    else:
        failed_checks.append("Special character")
        
    if score <= 2:
        strength_label = "Weak "
    elif score == 3:
        strength_label = "Medium"
    elif score == 4:
        strength_label = "Strong"
    elif score == 5:
        strength_label = "Very Strong"
        
    return (strength_label, score, failed_checks)

if __name__ == "__main__":
    pwd = input("Enter a password to evaluate: ")
    result = analyze_password(pwd)
    print(result)
