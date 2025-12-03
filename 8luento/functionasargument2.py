from my_validators import validate_number

def calculate_sum(a, b):
    return float(a) + float(b)

def calculate_difference(a, b):
    return float(a) - float(b)


def execute_my_function(function_to_execute):
    print("Anna kaksi numeroa, joihin operaatio kohdistetaan.")

    a = input("Anna ensimmäinen tekijä? ")
    validate_number(a)

    b = input("Anna toinen tekijä? ")
    validate_number(b)

    # suoritetaan argumenttina saatu funktio
    result = function_to_execute(a, b)
    return result


def main():
    i_want_to = input("Mitä haluat tehdä? [summa, erotus] ")

    if i_want_to == "summa":
        my_function = calculate_sum
    elif i_want_to == "erotus":
        my_function = calculate_difference
    else:
        print(f"Annoit väärän arvon [{i_want_to}].")
        return

    try:
        # execute_my_function on korkeampi asteen funktio,
        # koska se saa argumenttina toisen funktion
        result = execute_my_function(my_function)
        print(f"Tulos on {result}")
    except Exception as e:
        print(f"Lasku epäonnistui: {e}")



if __name__ == "__main__":
    main()
