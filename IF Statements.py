is_female = True
is_tall = True

if is_female:
    print("You are a female")
else:
    print("You are not a female")

if is_female or is_tall:
    print("You are a female or tall or both")
else:
    print("You are neither female nor tall")

if is_female and is_tall:
    print("You are a tall female")
else:
    print("You are either not female or not tall or both")

if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are not female but tall")
else:
    print("You are not a female and not tall ")