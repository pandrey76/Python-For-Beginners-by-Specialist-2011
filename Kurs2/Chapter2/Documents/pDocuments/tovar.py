#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optparse
import sqlite3

import mDocuments
import mNakladnay


if __name__ == "__main__" :
    parser = optparse.OptionParser()
    parser.add_option( "-i", "--initdb", dest="initdb",
                       action = "store_true", default=False,
                       help = "Initialise database")
    ( opt, args ) = parser.parse_args()
    if opt.initdb :
        try :
            mNakladnay.Nakladnay.create_table()
#        except Exception as ex   :
        except sqlite3.DatabaseError as ex :         
            print ex.message
            #print ex.args
            
    else :
        ##Nak = mNakladnay.create()
        ##Nak.append_blank()
        ##print Nak  ###    <mNakladnay.Nakladnay object at 0x00000000020D6320>
        #Если в классе определен метод __repr__ или __str__, то
        #при вызове функции print будет вызван он.    
        ##print unicode ( Nak ) #Если в классе определен метод __unucode__, то
        #при данном преобразовании будет вызван он. 
        ##print str ( Nak ) #Если в классе определен метод __str__, то
        #при данном преобразовании будет вызван он. 
        #print Nak.dump()
    
#    Nak.get_position(0).title = u"Карандаши"
#    Nak.get_position(0).unit  = u"шт"  

        #В классе mNkladnay мы переопределили метод __getitem__ 
        ##Nak[0].title = u"Карандаши"
        ##Nak[0].unit  = u"шт"  

        ##Nak.append_blank()
 
        ##print unicode( Nak )
        ##print u"Всего позиций в накладной: ", len(Nak)   
    
        #1#Doc = mDocuments.create()
        #1#Doc.save()
        #1#print Doc.identificator
        
        try :
            
            #Проверка срабатывания исключений
            #--------------
            #print X
            #prin X
            #print 200/0
            #--------------
            
            #2#Doc = mDocuments.load( Iden = 25 ) #25
            #2#print Doc.identificator, Doc._status
            
            #3#Doc = mNakladnay.Nakladnay ( status = mDocuments.Document.New )
            #3#Doc.save()
            #3#Doc.save()
            #3#print Doc.identificator, Doc._status
            Doc = mNakladnay.Nakladnay ( id = 5 )
            Doc.restore()
            print Doc.identificator, Doc._status, Doc._itogo
        except mDocuments.NotFound :
            print u"Документ не найден."
        except mDocuments.Error :
            print u"Какая то ошибка при работе с документом."
        except sqlite3.DatabaseError as Ex:
            print u"Какая то ошибка при работе с базой данных."
            print Ex.message
        except SyntaxError :
            #Эта ошибка возникает ещё раньше при формирования байткода,
            #при импорте модуля или при вызове функции eval
            print u"Какая то ошибка в синтаксисе."
        except NameError :
            print u"Какая то ошибка при записи переменной."
        except Exception as ex:
            print u"""
                Какая то неизвестная ошибка. Так пользоваться тоже не рекомендуется.
                Но если используется то в самом конце блока исключений ( как в С++ )
                """
            print ex.message
        except :
            print u"""
            Кто то выражается не прилично! 
            В реальных программах такой конструкциеё пользоваться нельзя.
                """
            
    

