cover_type = input("What type of cover does the book have?\n")

if(cover_type == 'soft'):
    boolean = input("Is the book perfect-bound?\n")
    if(boolean == 'yes'):
        print("Soft cover, perfect bound books are very popular\n!")
    else:
        print("Soft covers with coils or stitches are great for short books\n")
if(cover_type == 'hard'):
    print("Books with hard covers can be more expensive!\n")