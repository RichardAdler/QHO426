#Open file for reading
f = open("song.txt")
#Print full content
#print(f.read())
#Print a line
#print(f.readline())
#print(f.readline())
#Grabing content of a txt file and return it as a list
lista = f.readlines()
print(lista)
f.close()

g = open("song.txt", "a")
#g.write("\nAnd it's everlasting, infinite\n")
g.writelines(["It goes on and on, you can't measure it\n", "Can't quench your love"])
g.close()