

def main():
    #str1 = "CV188_lb_"
    #str2 = "CV188_p_"

    str1 = "CE34-5_lb_"
    str2 = "CE34-5_p_"

    n  = open("numero_iniziale.txt", "r")
    l = n.readline()
    num = int(l)
    l = n.readline()
    pag = int(l)
    l = n.readline()
    rv = str(l.rstrip("\n"))
    l = n.readline()
    par = int(l)

    n.close()
    
    print(num)
    print(pag)
    print(rv)
    print()
    print()
    f  = open("Editto Rotari_lb.txt", "r")
    f2 = open("Editto Rotari_lb_elab.txt", "w")
    for line in f:

        t = line.find(str2)
        if (t>0):
            prima = line[0:t+9]
            if (pag<10):
                prima=prima+"00"+str(pag)+rv+"_"+str(par)+"""\" n=\""""+str(par)+"""\""""
            elif(pag<100):
                prima=prima+"0"+str(pag)+rv+"_"+str(par)+"""\" n=\""""+str(par)+"""\""""
            else:
                prima=prima+str(pag)+rv+"_"+str(par)+"""\" n=\""""+str(par)+"""\""""
            seconda = line[t+26:len(line)]
            line = prima+seconda
            par=par+1

        #print(prima)

            
        t = line.find(str1)
        if (t>0):
            #print(t)
            prima = line[0:t+10]
            
            if (pag<10):
                prima=prima+"00"+str(pag)+rv+"_"
            elif(pag<100):
                prima=prima+"0"+str(pag)+rv+"_"
            else:
                prima=prima+str(pag)+rv+"_"

            #if(rv=="r"):
            #    rv = "v"
            #else:
            #    rv = "r"
            #    pag = pag+1
            
            seconda = line[t+24:len(line)]
            if (num<10):
                inter="0"+str(num)+"""\" n=\""""+str(num)+"""\""""
            else:
                inter = str(num)+"""\" n=\""""+str(num)+"""\""""
            linea2= prima+inter+seconda
            #print(line[t:t+9])
            #print(line)
            print(linea2)
            f2.write(linea2)
            num = num+1
        else:
            f2.write(line)
            
    f.close()
    f2.close()



main()
