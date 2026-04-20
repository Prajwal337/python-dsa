import streamlit as st
st.title("password checker")

st.write("check your password strength")

password = st.text_input("Enter your password", type="password") 


def has_min_length(password, min_len=8):
    return len(password) >= min_len

if password:
    if has_min_length(password):
        st.success("Password meets minimum length requirement.")
    else:
        st.error("Password does not meet minimum length requirement.")

def has_uppercase(password):
        return any(c.isupper() for c in password)

if password:
    if has_uppercase(password):
        st.success("Password contains uppercase letters.")  
    else:
        st.error("Password does not contain uppercase letters.")

def has_lowercase(password):
        return any(c.islower() for c in password)
if password:    
     if has_lowercase(password):
        st.success("Password contains lowercase letters.")
     else:      
      st.error("Password does not contain lowercase letters.")   
def has_digit(password):
        return any(c.isdigit() for c in password)   
if password:
    if has_digit(password):
        st.success("Password contains digits.")
    else:
        st.error("Password does not contain digits.")

def has_special_char(password, specials="!@#$%^&*"):        
        return any(c in specials for c in password)
if password:
    if has_special_char(password):
        st.success("Password contains special characters.")
    else:
        st.error("Password does not contain special characters.")
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

if st.button("Evaluate Password"):
    result = analyze_password(password)
    st.write(result)

