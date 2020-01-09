import numpy as np
import matplotlib.pyplot as plt 
def specifying_coordinates_ships(player, length): # a function for specifying the co-ordinates + directions of all ships
    coordinate_x = 0
    coordinate_y = 0
    direc = -1
    if(player=="0"): # "0" : computer
        coordinate_x = np.random.randint(0, 10)
        coordinate_y = np.random.randint(0, 10)
        direc = np.random.randint(0, 4)
    
    if(player=="1"): # "1" : user
        ch_coordinates_allowed=False
        ch_direction_allowed=False
        
        while((ch_coordinates_allowed==False) or (ch_direction_allowed==False)):
            if(length==5):
                coordinate_x = int(input("Enter the x-coordinate of Carrier, size = 5, from [0, 9] "))
                coordinate_y = int(input("Enter the y-coordinate of Carrier, size = 5, from [0, 9] "))
                direc = int(input("Enter the direction from [0, 3] (0:U, 1:D, 2:L, 3:R)"))
            elif(length==4):
                coordinate_x = int(input("Enter the x-coordinate of Battleship, size = 4 from [0, 9] " ))
                coordinate_y = int(input("Enter the y-coordinate of Battleship, size = 4 from [0, 9] " ))
                direc = int(input("Enter the direction from [0, 3] (0:U, 1:D, 2:L, 3:R)"))
            elif(length==3.1):
                coordinate_x = int(input("Enter the x-coordinate of Cruiser, size = 3 from [0, 9] "))
                coordinate_y = int(input("Enter the y-coordinate of Cruiser, size = 3 from [0, 9] "))    
                direc = int(input("Enter the direction from [0, 3] (0:U, 1:D, 2:L, 3:R)"))
            elif(length==3.2):
                coordinate_x = int(input("Enter the x-coordinate of Submarine, size = 3 from [0, 9] "))
                coordinate_y = int(input("Enter the y-coordinate of Submarine, size = 3 from [0, 9] "))    
                direc = int(input("Enter the direction from [0, 3] (0:U, 1:D, 2:L, 3:R)"))
            else:
                coordinate_x = int(input("Enter the x-coordinate of Destroyer, size = 2 from [0, 9] "))
                coordinate_y = int(input("Enter the y-coordinate of Destroyer, size = 2 from [0, 9] ")) 
                direc = int(input("Enter the direction from [0, 3] (0:U, 1:D, 2:L, 3:R)")) # U = up, D = down, L = left, and R = right
            if(((0<=coordinate_x) and (coordinate_x<=9)) and ((0<=coordinate_y) and (coordinate_y<=9))): 
                 ch_coordinates_allowed=True
                 if((0<=direc) and (direc<=3)): 
                     ch_direction_allowed=True
                
                 else:
                     print("chosen direction not allowed")
                     ch_direction_allowed=False
            else:
                print("chosen coordinates not allowed")
                #ch_coordinates_allowed=False
                
          
    if((player!="0") and (player!="1")):
          print("GHOST")
         
    return(coordinate_x, coordinate_y, direc)   

def last_point_val(direc, coordinate_x, coordinate_y, length): # a function to calculate the co-ordinates of the last block of ships 
    if(direc==0): #"Up"
        last_point = (coordinate_x - int(length) + 1)
    elif(direc==1):  #"down"
        last_point = (coordinate_x + int(length) - 1)
    elif(direc==2):   #"Left"
        last_point = (coordinate_y - int(length) + 1)
    else:    #"right"
        last_point = (coordinate_y + int(length) - 1)
         
    return(last_point)     

def putting_ships(User, length, matrix, colors): # a function to put ships for both user and the computer
    ch_last_point = False
    choice_overlap = False
    
    while((ch_last_point==False) or (choice_overlap==False)): 
        coordinate_x, coordinate_y, direc = specifying_coordinates_ships(User, length)
        last_point = last_point_val(direc, coordinate_x, coordinate_y, length)
        if((0<=last_point) and (last_point<=9)): # checking that ships are within the board
            ch_last_point = True
            choice_overlap = True
            if(direc==0): # "Up"
                if(length==5):
                    for j in range(last_point, coordinate_x + 1):
                        matrix[j][coordinate_y] = length
                        list_coordinate_x.append(j)
                        list_coordinate_y.append(coordinate_y)
                        list_colors.append(colors)
                        
                if(length < 5): 
                    for j in range(last_point, coordinate_x + 1):
                        if(matrix[j][coordinate_y]!=0):
                            choice_overlap=False
                            print("Overlap, choose another position") # checking whether there is an overlap
                                    
                    if(choice_overlap!=False):
                        
                        for j in range(last_point, coordinate_x + 1):
                            matrix[j][coordinate_y] = length
                            list_coordinate_x.append(j)
                            list_coordinate_y.append(coordinate_y)
                            list_colors.append(colors)
                                
                        
            elif(direc==1): #"Down"
                 
                 if(length==5):
                     for j in range(coordinate_x, (last_point + 1)):
                             matrix[j][coordinate_y] = length
                             list_coordinate_x.append(j)
                             list_coordinate_y.append(coordinate_y)
                             list_colors.append(colors)
                     
                 if(length<5):
                    
                     for j in range(coordinate_x, (last_point + 1)):
                         if(matrix[j][coordinate_y]!=0):
                             print("Overlap, choose another position") #print("Overlap")
                             choice_overlap=False
                       
                     if(choice_overlap!=False):
                    
                         for j in range(coordinate_x, (last_point + 1)):
                             matrix[j][coordinate_y] = length
                             list_coordinate_x.append(j)
                             list_coordinate_y.append(coordinate_y)
                             list_colors.append(colors)     
            elif(direc==2): #left
            
                if(length==5):
                    for j in range(last_point, coordinate_y + 1):
                            matrix[coordinate_x][j] = length  
                            list_coordinate_y.append(j)
                            list_coordinate_x.append(coordinate_x)
                            list_colors.append(colors)
                if(length<5):
                
                    for j in range(last_point, coordinate_y + 1):
                        if(matrix[coordinate_x][j]!=0):
                            print("Overlap, choose another position")
                            choice_overlap = False
                        
                    if(choice_overlap!=False):
                      
                        for j in range(last_point, coordinate_y + 1):
                            matrix[coordinate_x][j] = length  
                            list_coordinate_y.append(j)
                            list_coordinate_x.append(coordinate_x)
                            list_colors.append(colors)
            else:  #right
            
                if(length==5):
                    for j in range(coordinate_y, (last_point + 1)):
                        matrix[coordinate_x][j]=length 
                        list_coordinate_y.append(j)
                        list_coordinate_x.append(coordinate_x)
                        list_colors.append(colors)
                if(length<5): 
                
                    for j in range(coordinate_y, (last_point + 1)):
                        if(matrix[coordinate_x][j]!=0): #3
                            print("Overlap, choose another position")
                            choice_overlap = False
                        
                    if(choice_overlap!=False):
                      
                        for j in range(coordinate_y, (last_point + 1)):
                            matrix[coordinate_x][j]=length 
                            list_coordinate_y.append(j)
                            list_coordinate_x.append(coordinate_x)
                            list_colors.append(colors)
            
        else:
             ch_last_point=False
             print("Outside grid, choose another position")
            
            
    return(matrix, list_coordinate_x, list_coordinate_y)

leng = [5, 4, 3.1, 3.2, 2] 
colors = [(1, 0, 0), (0, 1, 0), (0.5, 0.5, 0), (0.5, 0.5, 0), (0.0, 0.5, 0.5)]
#plt.xlim((-0.5, 10.5))
#plt.ylim((-10.5, 0.5))
for i in range(2):
    k = 0
    matrix = np.zeros(shape = (10, 10))
    list_coordinate_x = []
    list_coordinate_y = []
    list_colors = []
    plt.figure(figsize = (5, 5))
    plt.tick_params(
        axis="x",
        which="both",
        bottom=False,
        top = False,
        labelbottom=False
        )
    plt.tick_params(
        axis="y",
        which="both",
        right=False,
        left = False,
        labelleft=False
        )
    #plt.xlim((0.5, 10.5))
    #plt.ylim((0.5, 10.5))
    while(k < 5):
        matrix, list_coordinate_x, list_coordinate_y = putting_ships(str(i), leng[k], matrix, colors[k])
        k+=1
    if(i==0):    # comp
        print("Computer")
        matrix_user = matrix
        list_user_cord_x = list_coordinate_x
        list_user_cord_y = list_coordinate_y
        #plt.figure(figsize = (5, 5))
        plt.scatter(list_coordinate_y, list_coordinate_x, c = np.array(list_colors), s = 400, marker = "s")
    else:       # user
        print("User")
        matrix_comp = matrix
        list_comp_cord_x = list_coordinate_x
        list_comp_cord_y = list_coordinate_y 
    
        plt.scatter(list_coordinate_y, list_coordinate_x, c = np.array(list_colors), s = 400, marker = "X")
    plt.show()      
#plt.scatter(list_user_cord_x, list_user_cord_y, c = np.array(list_colors), s = 400, marker = "s")
#plt.show()        
#print(matrix_user)
#print(matrix_comp)
    
#*********************************************************************************************
#Part 2: hitting the ships
count_user = 0
count_comp = 0
hit_user_x = []  
hit_user_y = []
hit_comp_x = []  
hit_comp_y = [] 
no_turns_comp = 0 # no. of hits for computer
no_turns_user = 0 # no. of hits for user
matrix_hit_user = matrix_user
matrix_hit_comp = matrix_comp
ch_win = False
while(ch_win==False):
    hit_user_x = np.random.randint(0, 10)
    hit_user_y = np.random.randint(0, 10)
    value_matrix = matrix_hit_user[hit_user_x][hit_user_y]
    if(value_matrix>=0):    #(size > 0): un-hit positions
                no_turns_user+=1
                if(hit_user_x, hit_user_y) in zip(list_user_cord_x, list_user_cord_y): # boat ki positions 
                   count_user+=1
                   if(value_matrix==3.1):
                       #print("You just hit a Cruiser")
                       matrix_hit_user[hit_user_x][hit_user_y] = -3.1
                   elif(value_matrix==3.2):
                       #print("You just hit a Submarine")
                       matrix_hit_user[hit_user_x][hit_user_y] = -3.2
                   elif(value_matrix==4):
                       #print("You just hit a Battleship")
                       #count_user4+=1
                       matrix_hit_user[hit_user_x][hit_user_y] = -4
                       #if(count_user4==4):
                        #   print("Battleship GONE")
                       
                   elif(value_matrix==5):
                     #print("You just hit a Carrier")
                     #count_user5+=1
                     matrix_hit_user[hit_user_x][hit_user_y] = -5
                     """if(count_user5==5):
                         print("carrier GONE")"""
                      
                    
                   elif(value_matrix==2):
                       #print("You just hit a Destroyer")
                       #count_user2+=1
                       matrix_hit_user[hit_user_x][hit_user_y] = -2
                       """if(count_user2==2):
                           print("Destroyer gone")"""
                       
                else: # corresponding to water
                      """print("Water")"""
                      matrix_hit_user[hit_user_x][hit_user_y] = -1.0
                     
                      
                
    if(count_user==17):
       print("User won" + " in ", no_turns_user, "moves")
       ch_win=True
       #plt.scatter(hit_user_x1, hit_user_y1, s = 400, marker = "X")
       #plt.show()
       break
    
    hit_comp_x = np.random.randint(0, 10)
    hit_comp_y = np.random.randint(0, 10)
    size1 = matrix_hit_comp[hit_comp_x][hit_comp_y]
    
    if(size1>=0): 
        no_turns_comp+=1
        if(hit_comp_x, hit_comp_y) in zip(list_comp_cord_x, list_comp_cord_y): 
                    count_comp+=1
                    if(size1==3.1):
                       #count_user3C+=1
                       matrix_hit_comp[hit_comp_x][hit_comp_y] = -3.1
                       
                    elif(size1==3.2):
                       #count_user3C+=1
                       matrix_hit_comp[hit_comp_x][hit_comp_y] = -3.2
                      
                    elif(size1==4):
                       #count_user4C+=1
                       matrix_hit_comp[hit_comp_x][hit_comp_y] = -4
                     
                   
                    elif(size1==5):
                        #count_user5C+=1
                        matrix_hit_comp[hit_comp_x][hit_comp_y] = -5
                        
                  
                    elif(size1==2):
                       #count_user2C+=1 
                       matrix_hit_comp[hit_comp_x][hit_comp_y]= -2
                     
                    
        else:  
            matrix_hit_comp[hit_comp_x][hit_comp_y] = -1
                     
                      
    if(count_comp==17):
        print("Comp. won" + " in ", no_turns_comp, " moves")
        ch_win=True 
        break   

#print(matrix_hit_comp)         
