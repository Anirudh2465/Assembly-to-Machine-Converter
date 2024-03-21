def remove_lines(L):
    new = []

    for line in L:
        if not line.strip().startswith("//"):
            if line!='\n':
                new.append(line)
    

    for i in range(len(new)):
        new[i] = new[i].partition("//")[0].strip()
    
    return new

