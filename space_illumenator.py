def space_illumenator(usr_input):
    result = []
    for letter in usr_input:
        if letter != " ":
            result.append(letter)

        else:
            if len(result) == 0 or result[-1] == " ":
                continue
            else:
                result.append(letter)

    return result


sample_list = ["Hello    this is Ayman",
               "   Spaces Are First",
               "Spaces at the end          ",
               "Here     we   have    multiple    spaces spread",
               "NoSpacesAtAll",
               "Very elegant sentence with one space in between two words!"
               ]

for sample in sample_list:
    print(space_illumenator(sample))