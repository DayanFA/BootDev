def merge(dict1, dict2):
    output = {}

    for item in dict1:
        output[item] = dict1[item]
    for item in dict2:
        output[item] = dict2[item]

    return dict(output)
