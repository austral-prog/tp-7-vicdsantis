def enumerate_list(strs):
    result = []
    count = 0 
    for string in strs:
        if string: 
            result.append(f"{count}. {string}")
            count += 1
    return result
def enumerate_backwards(strs):
    result = []
    count = 0  
    for string in strs:
        if string: 
            reversed_string = string[::-1]
            result.append(f"{count}. {reversed_string}")
            count += 1
    return result
