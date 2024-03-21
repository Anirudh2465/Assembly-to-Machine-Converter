def convert(i,D):

    if i in D:
        val = D[i]
        return '{0:016b}'.format(val)

    elif i[1:].isnumeric()==True:
        return '{0:016b}'.format(int(i[1:]))
    

