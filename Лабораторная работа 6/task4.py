import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with(open(filename, "r")) as f:
        list_alpha = f.readlines()
        list_alpha = [line.replace(new_line, '') for line in list_alpha]

    list_beta = [val.split(delimiter) for val in list_alpha]
    list_omega = list_beta[0]
    list_dict = []
    for string in list_beta[1:]:
        dict_ = {list_omega[element]: string[element] for element in range(len(list_omega))}
        list_dict.append(dict_)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
