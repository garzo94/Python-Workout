def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')): # if line does not start with # or space then:
                user_info = line.split(':') # convert the line into a list separated by ":"
                users[user_info[0]] = int(user_info[2]) # add user as key and id as value to users dictionary
    return users