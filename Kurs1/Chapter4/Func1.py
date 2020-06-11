#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func ( x ) :
    return x*x
print func(3)



        
#Делаем присваивание имени
A = func
print A(3)
#Делаем присваивание имени функции
func = u"This is not function"
print func
print A(3)

#Работа функции как объекта 1-ого типа
def oper( L, function ) :
    Res = []
    for K in L :
        Res.append ( function( K ) )
    return Res

#Упращаем функцию oper
def oper1( L, function ) :
    Res = [function(K) for K in L ]
    return Res
    
X = [ 1, 34, 67, 100 ]
#Помним, что A = func
func = A
print oper( X, func ) 

#Возвращаем функцию как результ другой функции
#################################
def func1(Selector) :
    if Selector < 0 :
        def func2( x ) :
            return x*x
        return func2
    else :
        def func3( x ) :
            return x*x*x
        return func3
#################################
print oper( X, func1(-1) )
print oper(X, func1(1))
 
print oper1( X, func1(-1) )
print oper1(X, func1(1))
 
#Упрощаем, записываем функции func1,
#в виде двух лябда функций вместо
#func2 и func3
#################################
#Возвращаем функцию как результ другой функции
#################################
def func10(Selector) :
    if Selector < 0 :
        return lambda X : X*X
    else :
        return lambda X : X*X*X
        
#Можно делать и так
func20 = lambda x : x*x*x*x

print oper1( X, func10(-1) )
print oper1(X, func10(1))

print oper1(X, func20)


#################################
#################################

