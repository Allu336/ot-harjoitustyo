class Stopdrop():
    def __init__(self, tetris, block):
        self.tetris = tetris
        self.block = block
    
    def drop(self):
        for coordinates in self.block.coordinates:
            if coordinates[1] == "1":
                if self.tetris.grid[coordinates[0][0]+1][coordinates[0][1]] == "2":
                    self.stop()
                    return("new block")
                elif coordinates[0][0]+1 == 20:
                    self.stop()
                    return("new block")
        old_coordinates=[]
        coordinates2=[]
        for coordinate in self.block.coordinates:
            coordinates2.append(coordinate)
        for coordinate in coordinates2:
            old_coordinates.append(coordinate)
            self.block.coordinates.append(((coordinate[0][0]+1,coordinate[0][1]),coordinate[1]))
            self.block.coordinates.remove(coordinate)
        for k in old_coordinates:
            if self.tetris.grid[k[0][0]][k[0][1]]!="2":
                self.tetris.grid[k[0][0]][k[0][1]]="."
        for k in self.block.coordinates:
            if k[1]=="1":
                self.tetris.grid[k[0][0]][k[0][1]]="1"
        return

    def stop(self):
        for coordinates in self.block.coordinates:
            if coordinates[1] == "1":
                self.tetris.grid[coordinates[0][0]][coordinates[0][1]] = "2"
        for row in range(1,20):
            if self.tetris.grid[row] == ["2","2","2","2","2","2","2","2","2","2"]:
                print("jep")
                print(self.tetris.grid)
                new = []
                for row2 in range(0,23):
                    if row2 == 0:
                        new.append([".",".",".",".",".",".",".",".",".","."])
                    elif row2 <= row:
                        new.append(self.tetris.grid[row2-1])
                    else:
                        new.append(self.tetris.grid[row2])
                self.tetris.grid = new
                print(self.tetris.grid)