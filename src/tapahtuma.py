import pygame
import palikka from palikka.py

class Tapahtuma():
    def __init__(self, koordinaatit, tapahtuma):
        self.tapahtuma=tapahtuma
        self.koordinaatit=koordinaatit

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
                    return (vanha, )
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