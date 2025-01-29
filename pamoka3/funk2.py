email = input("Iveskit el.pasto adresa: ")
def validate_email(email):

    if email.count("@") != 1:
        return False
   
    local_part, domain = email.split("@")
  
    if "." not in domain:
        return False
    
    if not local_part or not domain:
        return False
    return True

if validate_email(email):
    print("El. pašto adresas yra galiojantis.")
else:
    print("El. pašto adresas nėra galiojantis.")