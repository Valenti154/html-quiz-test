full_name = input("Įveskite savo pilną vardą: ")
space_index = full_name.find(" ")
first_name = full_name[:space_index]
first_name_upper = first_name.upper()
greeting = f"Labas,{first_name.upper()}, sveiki atvykę!"
print(greeting)

