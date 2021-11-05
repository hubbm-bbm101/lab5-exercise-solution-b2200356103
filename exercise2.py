def my_exmpl2(email=input("give me an email address:")):
    at = False
    dot = False
    for i in email:
        if i == "@":
            at = True
        if i == ".":
            dot = True
    if at == True and dot == True:
        return True
    else:
        return False

my_exmpl2()
