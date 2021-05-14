import pygame

class Block():
    def __init__(self):
        self.coordinates=[]
        self.positions=[]
        self.current_position=0
    
    def create_block(self, blocks):
        randomform = random.randint(0,6)
        forms = blocks[randomform]
        form = forms[0]
        for x in forms:
            self.positions.append(x)
        for t in range(0,4):
            for n in range(0,5):
                if form[t][n] == "1":
                    self.coordinates.append(((t,n+3),"1"))
                elif form[t][n] == ".":
                    self.coordinates.append(((t,n+3),"."))
        empty = []
        return (empty, self.coordinates)
    
    def move_block(self,direction):
        old_coord = []
        coordinates2 = []
        coord = self.block.coordinates            
        if direction == "L":
            if self.block.coordinates[0][0][1] == 0:
                if coord[0][1] == "." and coord[5][1] == "." and coord[10][1] == "." and coord[15][1] == ".":
                    new = []
                    for x in range(20):
                        if x == 4 or x == 9 or x == 14 or x == 19:
                            new.append((coord[x][0],"."))
                        else:
                            new.append((coord[x][0],coord[x+1][1]))
                    old = coord
                    self.block.coordinates = new
                    return (old, self.block.coordinates)
                else:
                    return
            for coordinate in self.block.coordinates:
                coordinates2.append(coordinate)
            for coordinate in coordinates2:
                old_coord.append(coordinate)
                self.block.coordinates.append(((coordinate[0][0],coordinate[0][1]-1),coordinate[1]))
                self.block.coordinates.remove(coordinate)
            return (old_coord,self.block.coordinates)
        if direction == "R":
            if self.block.coordinates[4][0][1] == 9:
                if coord[4][1] == "." and coord[9][1] == "." and coord[14][1] == "." and coord[19][1] == ".":
                    new=[]
                    for x in range(20):
                        if x == 0 or x == 5 or x == 10 or x == 15:
                            new.append((coord[x][0],"."))
                        else:
                            new.append((coord[x][0],coord[x-1][1]))
                    old = coord
                    self.block.coordinates = new
                    return(old, self.block.coordinates)
                else:
                    return
            for coordinate in self.block.coordinates:
                coordinates2.append(coordinate)
            for coordinate in coordinates2:
                old_coord.append(coordinate)
                self.block.coordinates.append(((coordinate[0][0],coordinate[0][1]+1),coordinate[1]))
                self.block.coordinates.remove(coordinate)
            return (old_coord,self.block.coordinates)



    def rotate_block(self):
        if self.current_position == (len(self.positions)-1):
            uusi_current_position=self.positions[0]
            self.current_position=0
        else:
            uusi_current_position = self.positions[(self.current_position+1)]
            self.current_position =+ 1  
        current_position = []        
        for y in range(0,4):
            for x in range(0,5):
                current_position.append(uusi_current_position[y][x])
        lenght = len(self.coordinates)
        for x in range(0,lenght):
            coordinate = self.coordinates[0][0]
            self.coordinates.append((coordinate,current_position[x]))
            self.coordinates.pop(0)
    