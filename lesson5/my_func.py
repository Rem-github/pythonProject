def cut_space(str):
    lis = [word for word in str.split(' ') if word != '']
    return lis

def create_dict(user_list):
    dict = {}
    for s in user_list:
        list_tmp = cut_space(s)
        try:
            dict[list_tmp[0]] = int(list_tmp[1])
        except ValueError:
            pass
    return dict