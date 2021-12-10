def linearSearch(my_list, search):
    
    for i in range(0, len(my_list)):
        
        if my_list[i] == search:
            print("pwa geche ", i)
            break
            
    else:
        print("pwa jai nai!!!!!")
    return -1

my_list = [1, 3, 5, 9, 12, 45, 95, 120]
search = int(input())

linearSearch(my_list, search)