import datetime
subs=input("START_SUBSCRIPTION ")
cat1,pl1 =input("ADD_SUBSCRIPTION ").split(' ')
cat2,pl2 =input("ADD_SUBSCRIPTION ").split(' ')
cat3,pl3 =input("ADD_SUBSCRIPTION ").split(' ')
tp,mon =input("ADD_TOPUP ").split(' ')

def music(cat,pl):
    if(pl1 == "free"):
        print(f"RENEWAL_REMINDER ",cat1,'\t',subs)

    elif(pl1 == "personal"):
        print(f"RENEWAL_REMINDER ",cat1,'\t' ,subs)    

    else:
        print(f"RENEWAL_REMINDER ",cat1,'\t' ,subs)     

music(cat1,pl1)

def video(cat,pl):
    if(pl2 == "free"):
        print(f"RENEWAL_REMINDER ",cat2,'\t',subs)

    elif(pl2 == "personal"):
        print(f"RENEWAL_REMINDER ",cat2,'\t' ,subs)    

    else:
        print(f"RENEWAL_REMINDER ",cat2,'\t' ,subs)     

video(cat2,pl2)

def podcast(cat,pl):
    if(pl3 == "free"):
        print(f"RENEWAL_REMINDER ",cat3,'\t',subs)

    elif(pl3 == "personal"):
        print(f"RENEWAL_REMINDER ",cat3,'\t' ,subs)    

    else:
        print(f"RENEWAL_REMINDER ",cat3,'\t' ,subs)     

podcast(cat3,pl3)

def pricing(*kw):
    mprice =0
    vprice =0
    poprice =0
    topup =0
    total_pricing =0
    
    def music2(pl1):  
        if(pl1 == "free" or pl1 =="Free" or pl1 =="FREE"):
            mprice =0
        elif(pl1 == "personal" or pl1 =="Personal" or pl1 =="PERSONAL"):
            mprice =100   
        elif(pl1 == "premium" or pl1 =="Premium" or pl1 =="PREMIUM"):
            mprice =250  
        else:
            return "Invalid Plan"

    music2(pl1)
         


    def video2(pl2):
        if(pl2 == "free" or pl2 =="Free" or pl2 =="FREE"):
            vprice =0
        elif(pl2 == "personal" or pl2 =="Personal" or pl2 =="PERSONAL"):
            vprice =200 
        elif(pl2 == "premium" or pl2 =="Premium" or pl2 =="PREMIUM"):
            mprice =550  
        else:
            return "Invalid Plan"      
        
    video2(pl2)
    
    
    def podcast2(pl3):
        if(pl3 == "free" or pl3 =="Free" or pl3 =="FREE"):
            poprice =0
        elif(pl3 == "personal" or pl3 =="Personal" or pl3 =="PERSONAL"):
            poprice =100   
        elif(pl3 == "premium" or pl3 =="Premium" or pl3 =="PREMIUM"):
            mprice =350  
        else:
            return "Invalid Plan"
        
    podcast2(pl3) 
       

    def topup2(tp,mon):
        if(tp =="four" or tp =="Four" or tp == "FOUR"):
            topup = 50 * int(mon)

        elif(tp =="ten" or tp =="Ten" or tp == "TEN"):
            topup = 100 *int(mon)

        else:
            return "Invalid Plan"
                   
    topup2(tp,mon)


    total_pricing=mprice +vprice+poprice+topup
    return total_pricing            
            

print(pricing(pl))  
      
















# print(subs)
# print(cat1 ,'\t', pl1)
# print(cat2 ,'\t', pl2)
# print(cat3 ,'\t', pl3)