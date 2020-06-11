#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Пример Замыкания
############################
def func ( x, y ) :
    pass

func1 = lambda y : func ( 3, y )    
############################
#Пример Карирование
############################
func ( 1, 2 )
#func2 = (1)(3)
############################

#Класс стакан
class Stakan ( object ) :
#После имени класса в скобочках необходимо что-нибудь записывать 

#Эмулируем перечисление
#Position = [u"shkaf", u"table"]
    def __init__ ( self ) :
#Так создавать данные ошибка так как все данные объекта 
#являются открытыми и будут доступны из вне
#        self.Water = 0.0

#В Питон внутренние (закрытые) имена методов и данных должны начинаться с двух подчёркиваний
        self.__Water = 1.0
        print  u"self.__Water      ", self.__Water     #   1.0       
        
        self.__Milk  = 0.0
        self.__Pos   = u"shkaf"
        
    def add_water( self, vol ) :
        if vol < 0 :
            raise ValueError
        self.__Water += vol

    def add_milk ( self, vol ) :
        if vol < 0 :
            raise ValueError
        self.__Milk += vol
        
    def take( self, vol ) :
        if vol < 0 :
            raise ValueError
        if vol > self.total() :
            raise Exception
        P = self.part_milk
        M = P * vol
        W = vol - M
        self.__Milk  -= M 
        self.__Water -= W 
        return ( vol, P )

    def set_position ( self, pos ) :
        pass

    def total( self ) :
        return self.__Water + self.__Milk
        
    @property
    def part_milk( self ) :
        P = self.__Milk / self.total()
        return P
        
if __name__ == "__main__" :
    St = Stakan()
    St.__Water = 5.0
    #Так делать нельзя так как в данной ситуации определяется новая переменная St.__Water
    print  u"St.__Water        ", St.__Water           #   5.0
    print  u"St._Stakan__Water ", St._Stakan__Water    #   1.0
#но если надо обратится к закрытой переменной, то это делается так.
#    St._Stakan__Water = 5.0

#добавить воды в стакан можно так,  но это не типичный способ его использования
    Stakan.add_water( St, 5.1 )
#типичный способ использования
    St.add_water ( 5.1 )
    St.add_milk ( 1.0 )    
    print St._Stakan__Water + St._Stakan__Milk
    print St.total()
#    St.add_water ( -2 )    
    print St.part_milk                                #0.0819672131148
    
    print St.take(3.2)                                 #(3.2, 0.0819672131147541)
    print St.total()                                   #9.0
    print  u"St.__Water        ", St.__Water           #   5.0
    print  u"St._Stakan__Water ", St._Stakan__Water    #   8.26229508197
    print  u"St._Stakan__Milk ", St._Stakan__Milk      #   0.737704918033    

    print St.take(2.2)                                 #(2.2, 0.0819672131147541)
    print St.total()                                   #6.8
    print  u"St._Stakan__Water ", St._Stakan__Water    #6.24262295082
    print  u"St._Stakan__Milk ", St._Stakan__Milk      # 0.55737704918
    
    print St.take(1.2)                                 #(1.2, 0.0819672131147541)
    print St.total()                                       #5.6
                  
    print  u"St._Stakan__Water ", St._Stakan__Water    #   5.14098360656
    print  u"St._Stakan__Milk ", St._Stakan__Milk      #   0.459016393443        
    
    
    print u"part_milk", 0.459016393443 / 5.6