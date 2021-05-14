import random
import pygame
import os


dirname=os.path.dirname(__file__)

class Tetris:
    def __init__(self):
        pygame.init()
        self.kentta=[]
        self.kello=pygame.time.Clock()
        self.kello.tick(60)
        self.aika=0
        self.aika2=0
        self.nopeus=500
        self.alas=False
        self.palikka=Palikka()
        self.naytto=pygame.display.set_mode((700,800))
        self.luo_kentta()
        self.kierros()

    def luo_kentta(self):
        for rivi in range(0,23):
            self.kentta.append([".",".",".",".",".",".",".",".",".","."])
        self.luo_palikka()

    def liikuta(self,suunta):
        vanhat=[]
        koordinaatit2=[]            
        if suunta=="V":
            if self.palikka.koordinaatit[0][0][1]==0:
                koord=self.palikka.koordinaatit
                if koord[0][1]=="." and koord[5][1]=="." and koord[10][1]=="." and koord[15][1]==".":
                    uusi=[]
                    for x in range(20):
                        if x==4 or x==9 or x==14 or x==19:
                            uusi.append((koord[x][0],"."))
                        else:
                            uusi.append((koord[x][0],koord[x+1][1]))
                    vanha=koord
                    self.palikka.koordinaatit=uusi
                    self.siirra_kohtaan(vanha, self.palikka.koordinaatit)
                    return
                else:
                    return
            for koordinaatti in self.palikka.koordinaatit:
                koordinaatit2.append(koordinaatti)
            for koordinaatti in koordinaatit2:
                vanhat.append(koordinaatti)
                self.palikka.koordinaatit.append(((koordinaatti[0][0],koordinaatti[0][1]-1),koordinaatti[1]))
                self.palikka.koordinaatit.remove(koordinaatti)
            self.siirra_kohtaan(vanhat,self.palikka.koordinaatit)
        if suunta=="O":
            if self.palikka.koordinaatit[4][0][1]==9:
                koord=self.palikka.koordinaatit
                if koord[4][1]=="." and koord[9][1]=="." and koord[14][1]=="." and koord[19][1]==".":
                    uusi=[]
                    for x in range(20):
                        if x==0 or x==5 or x==10 or x==15:
                            uusi.append((koord[x][0],"."))
                        else:
                            uusi.append((koord[x][0],koord[x-1][1]))
                    vanha=koord
                    self.palikka.koordinaatit=uusi
                    self.siirra_kohtaan(vanha, self.palikka.koordinaatit)
                    return
                else:
                    return
            for koordinaatti in self.palikka.koordinaatit:
                koordinaatit2.append(koordinaatti)
            for koordinaatti in koordinaatit2:
                vanhat.append(koordinaatti)
                self.palikka.koordinaatit.append(((koordinaatti[0][0],koordinaatti[0][1]+1),koordinaatti[1]))
                self.palikka.koordinaatit.remove(koordinaatti)
            self.siirra_kohtaan(vanhat,self.palikka.koordinaatit)
            




    def siirra_kohtaan(self,Vkoordinaatit, Ukoordinaatit):
        for k in Vkoordinaatit:
            if self.kentta[k[0][0]][k[0][1]]=="2":
                continue
            self.kentta[k[0][0]][k[0][1]]="."
        for k in Ukoordinaatit:
            if k[1]=="1":
                self.kentta[k[0][0]][k[0][1]]="1"
    
    def tiputa(self):
        for koordinaatti in self.palikka.koordinaatit:
            if koordinaatti[1]=="1":
                if self.kentta[koordinaatti[0][0]+1][koordinaatti[0][1]]=="2":
                    self.pysayta()
                    return
                elif koordinaatti[0][0]+1==20:
                    self.pysayta()
                    return

        vanhat=[]
        koordinaatit2=[]
        for koordinaatti in self.palikka.koordinaatit:
            koordinaatit2.append(koordinaatti)
        for koordinaatti in koordinaatit2:
            vanhat.append(koordinaatti)
            self.palikka.koordinaatit.append(((koordinaatti[0][0]+1,koordinaatti[0][1]),koordinaatti[1]))
            self.palikka.koordinaatit.remove(koordinaatti)
        for k in vanhat:
            if self.kentta[k[0][0]][k[0][1]]!="2":
                self.kentta[k[0][0]][k[0][1]]="."
        for k in self.palikka.koordinaatit:
            if k[1]=="1":
                self.kentta[k[0][0]][k[0][1]]="1"
        self.aika2=pygame.time.get_ticks()

    def pysayta(self):
        for koordinaatti in self.palikka.koordinaatit:
            if koordinaatti[1]=="1":
                self.kentta[koordinaatti[0][0]][koordinaatti[0][1]]="2"
        for rivi in range(1,20):
            if self.kentta[rivi]==["2","2","2","2","2","2","2","2","2","2"]:
                uusi=[]
                for rivi2 in range(0,23):
                    if rivi2==0:
                        uusi.append([".",".",".",".",".",".",".",".",".","."])
                    elif rivi2<=rivi:
                        uusi.append(self.kentta[rivi2-1])
                    else:
                        uusi.append(self.kentta[rivi2])
                self.kentta=uusi
        self.nopeus=500
        self.palikka=Palikka()
        self.luo_palikka()
    
    def luo_palikka(self):
        I=[["..1..",
        "..1..",
        "..1..",
        "..1.."],
        [".1111",
        ".....",
        ".....",
        "....."]]

        J=[[".1...",
        ".111.",
        ".....",
        "....."],
        ["11...",
        ".1...",
        ".1...",
        "....."],
        ["111..",
        "...1."
        ".....",
        "....."]]

        L=[["...1.",
        ".111.",
        ".....",
        "....."],
        [".1...",
        ".1...",
        ".11..",
        "....."],
        ["11...",
        ".1...",
        ".1...",
        "....."]]

        O=[["..11.",
        "..11.",
        ".....",
        "....."]]

        S=[["..11.",
        ".11..",
        ".....",
        "....."],
        ["..1..",
        ".11..",
        ".1...",
        "....."]]

        T=[["..1..",
        ".111.",
        ".....",
        "....."],
        ["..1..",
        "..11.",
        "..1..",
        "....."],
        [".111.",
        "..1..",
        ".....",
        "....."],
        ["..1..",
        ".11..",
        "..1..",
        "....."]]

        Z=[[".11..",
        "..11.",
        ".....",
        "....."],
        ["..1..",
        ".11..",
        ".1...",
        "....."]
        ]

        eri_muodot=[I,J,L,O,S,T,Z]
        jokumuoto=random.randint(0,6)
        muodot=eri_muodot[jokumuoto]
        muoto=muodot[0]
        for x in muodot:
            self.palikka.asennot.append(x)
        for t in range(0,4):
            for n in range(0,5):
                if muoto[t][n]=="1":
                    self.palikka.koordinaatit.append(((t,n+3),"1"))
                elif muoto[t][n]==".":
                    self.palikka.koordinaatit.append(((t,n+3),"."))
        tyhja=[]
        self.siirra_kohtaan(tyhja,self.palikka.koordinaatit)
                
    
    def kaanna_palikkaa(self):
        if self.palikka.asento==(len(self.palikka.asennot)-1):
            uusi_asento=self.palikka.asennot[0]
            self.palikka.asento=0
        else:
            uusi_asento=self.palikka.asennot[(self.palikka.asento+1)]
            self.palikka.asento=+1  
        asento=[]        
        for y in range(0,4):
            for x in range(0,5):
                asento.append(uusi_asento[y][x])
        pituus=len(self.palikka.koordinaatit)
        for x in range(0,pituus):
            koordinaatti=self.palikka.koordinaatit[0][0]
            self.palikka.koordinaatit.append((koordinaatti,asento[x]))
            self.palikka.koordinaatit.pop(0)
    
    def kierros(self):
        while True:
            for tapahtuma in pygame.event.get():
                if tapahtuma.type==pygame.KEYDOWN:
                    if tapahtuma.key==pygame.K_DOWN:
                        self.alas=True
                    if tapahtuma.key==pygame.K_LEFT:
                        self.liikuta("V")
                    if tapahtuma.key==pygame.K_RIGHT:
                        self.liikuta("O")
                    if tapahtuma.key==pygame.K_UP:
                        self.kaanna_palikkaa()
                    
                if tapahtuma.type==pygame.KEYUP:
                    if tapahtuma.key==pygame.K_DOWN:
                        self.alas=False
                        
                if tapahtuma.type==pygame.QUIT:
                        exit()
            
    
            self.aika=pygame.time.get_ticks()
            if self.alas==True:
                self.nopeus=100
            else:
                self.nopeus=500
            if self.aika - self.aika2>self.nopeus:
                self.tiputa()
            self.naytto.fill((0,0,0))
            pygame.draw.line(self.naytto,(255,255,255),(200,100),(500,100),2)
            pygame.draw.line(self.naytto,(255,255,255),(200,100),(200,700),2)
            pygame.draw.line(self.naytto,(255,255,255),(470,50),(500,50),2)
            pygame.draw.line(self.naytto,(255,255,255),(500,100),(500,700),2)
            pygame.draw.line(self.naytto,(255,255,255),(200,700),(500,700),2)
            for y in range(0,20):
                for x in range(0,10):
                    if self.kentta[y][x]==".":
                        x1=200+x*30
                        y1=100+y*30
                        pygame.draw.rect(self.naytto,(255,255,255),(x1,y1,30,30),1)
                    if self.kentta[y][x]=="1":
                        x1=200+x*30
                        y1=100+y*30
                        pygame.draw.rect(self.naytto,(255,255,255),(x1,y1,30,30))
                    if self.kentta[y][x]=="2":
                        x1=200+x*30
                        y1=100+y*30
                        pygame.draw.rect(self.naytto,(100,255,100),(x1,y1,30,30))



        


            pygame.display.flip()

class Palikka(pygame.sprite.Sprite):
    def __init__(self):
        super(Palikka, self).__init__()
        self.koordinaatit=[]
        self.asennot=[]
        self.asento=0

    


if __name__=="__main__":
    Tetris()
    pygame.quit()