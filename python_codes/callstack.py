def chicken():
    return egg()
def egg():
    return chicken()

print (chicken())
