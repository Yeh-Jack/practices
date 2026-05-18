# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Taxi :
    # 類別屬性
    idis , udis , ifee , ufee = 1000 , 500 , 20 , 10
    
    # 實例方法 初始化方法 建構方法
    def __init__( self , d = 0 ) : 
        self.dis = d
    
    # 類別方法
    @classmethod # 類別方法
    def charge( cls , dis ) :
        if dis < cls.idis :
            return cls.ifee
        else :
            return cls.ifee + cls.ufee * (1+(dis-cls.idis) //cls.udis)
    
    # 實例方法  物件方法
    def fee( self ) :
        return Taxi.charge(self.dis)
    
    # 實例方法 物件方法
    def __str__( self ) :
        return "距離: " + str(self.dis) + " m"
    
    # 靜態方法 類別及物件皆可用
    @staticmethod
    def fee_rule() :
        return """idis : 初始里程 udis : 單位里程ifee : 初始費用 ufee : 單位里程費用"""



# [ Taxi(200*i) for i in range(5,21) ]  #range(5,21) --> 5,6,7,8,9,....20 

# [Taxi(100*5),Taxi(100*6),Taxi(100*7),Taxi(100*8),Taxi(100*9).....Taxi(100*20)]  --> 共16個物件
# 程式碼由此開始執行


taxies = [ Taxi(200*i) for i in range(5,21) ]  # list  --> 物件串列
print( Taxi.fee_rule() )

for car in taxies :     # list  --> 物件串列-->一個個取出物件taxi
    # car.fee() 與 Taxi.charge(car.dis) 相同
    print( car , "-->" , car.fee() , "NT" )
    #print( car , "-->" , Taxi.charge(car.dis), "NT" )
    
    