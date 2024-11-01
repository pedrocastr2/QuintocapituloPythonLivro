chuva = input("Como está o tempo? Está chovendo (s/n)").lower()

frio = input("Está frio? (s/n)").lower()

if(chuva =='s' and frio =='s'): 
    print("Você está numa fria e chovendo ,utilize roupas de inverno e pegue um guarda-chuva")
    
if(chuva =='s' and frio !='s'): 
    print("Está chovendo,mas não está frio , você deveria usar um guarda-chuva")
    
if(chuva !='s' and frio =='s'): 
    print("Está frio,mas não está chovendo , pegue roupas de inverno ")
    
if(chuva !='s' and frio !='s'): 
    print("Está quente e sem chuva, aproveite")