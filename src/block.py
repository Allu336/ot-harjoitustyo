class Block():
    def __init__(self):
        self.coordinates = []
        self.positions = []
        self.current_position = 0
        self.first = False
    
    def create_block(self, blocks, grid, next):
        gameover = False
        self.coordinates = []
        self.positions = []
        self.current_position = 0
        forms = blocks[next]
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
        for coordinate in self.coordinates:
            if coordinate[1] == "1" and grid[coordinate[0][0]][coordinate[0][1]] == "2":
                gameover = True
        return(empty, self.coordinates, gameover)
    
    def move_block(self,direction, grid):
        old_coord = []
        coordinates2 = []           
        if direction == "L":
            if self.coordinates[0][0][1] == 0:
                coord = self.coordinates
                if coord[0][1] == "." and coord[5][1] == "." and coord[10][1] == "." and coord[15][1] == ".":
                    new = []
                    for x in range(20):
                        if x == 4 or x == 9 or x == 14 or x == 19:
                            new.append((coord[x][0],"."))
                        else:
                            new.append((coord[x][0],coord[x+1][1]))
                    old = coord
                    self.coordinates = new
                    return (old, self.coordinates)
                else:
                    return ("no change")
            else:
                for coordinate in self.coordinates:
                    if coordinate[1] == "1":
                        if grid[coordinate[0][0]][coordinate[0][1]-1] == "2":
                            return ("no change")
            for coordinate in self.coordinates:
                coordinates2.append(coordinate)
            for coordinate in coordinates2:
                old_coord.append(coordinate)
                self.coordinates.append(((coordinate[0][0],coordinate[0][1]-1),coordinate[1]))
                self.coordinates.remove(coordinate)
            return (old_coord,self.coordinates)
        if direction == "R":
            if self.coordinates[4][0][1] == 9:
                coord = self.coordinates
                if coord[4][1] == "." and coord[9][1] == "." and coord[14][1] == "." and coord[19][1] == ".":
                    new=[]
                    for x in range(20):
                        if x == 0 or x == 5 or x == 10 or x == 15:
                            new.append((coord[x][0],"."))
                        else:
                            new.append((coord[x][0],coord[x-1][1]))
                    old = coord
                    self.coordinates = new
                    return(old, self.coordinates)
                else:
                    return("no change")
            else:
                for coordinate in self.coordinates:
                    if coordinate[1] == "1":
                        if grid[coordinate[0][0]][coordinate[0][1]+1] == "2":
                            return ("no change")
            for coordinate in self.coordinates:
                coordinates2.append(coordinate)
            for coordinate in coordinates2:
                old_coord.append(coordinate)
                self.coordinates.append(((coordinate[0][0],coordinate[0][1]+1),coordinate[1]))
                self.coordinates.remove(coordinate)
            return (old_coord,self.coordinates)


    def rotate_block(self, grid):
        right = False
        left = False
        old_coordinates = []
        old_position = self.current_position
        for coordinate in self.coordinates:
            old_coordinates.append(coordinate)

        for coordinate in self.coordinates:
            if coordinate[0][1] == 9 and coordinate[1] == "1":
                right = True
                break
            elif coordinate[0][1] == 0 and coordinate[1] == "1":
                left = True
                break
        
        if self.current_position == (len(self.positions)-1):
            new_position = self.positions[0]
            self.current_position = 0
        else:
            new_position = self.positions[(self.current_position+1)]
            self.current_position = self.current_position + 1
        current_position = []

        for y in range(0,4):
            for x in range(0,5):
                current_position.append(new_position[y][x])
        lenght = len(self.coordinates)
        for x in range(0,lenght):
            coordinate = self.coordinates[0][0]
            self.coordinates.append((coordinate,current_position[x]))
            self.coordinates.pop(0)
        for coordinate in self.coordinates:
            if coordinate[1] == "1" and grid[coordinate[0][0]][coordinate[0][1]] == "2":
                self.coordinates = old_coordinates
                self.current_position = old_position
                return
        if right:
            self.move_block("R", grid)
            self.move_block("R", grid)
        elif left:
            self.move_block("L", grid)
            self.move_block("L", grid)
    