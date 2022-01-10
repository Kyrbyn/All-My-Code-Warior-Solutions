def friend(x):
    trueFriends = []
    for friend in x:
        if len(friend) == 4:
            trueFriends.append(friend)
    return(trueFriends)

friend(["John", "Me", "Jonathan", "Boys", "Girls"])