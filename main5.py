print("Please enter every of your expression with suitable parentheses and follow the examples below. "
      "\nEg: sin(x)^(1/3), cos(x^(2))^(sin(x))^(ln(x)), e^((1/3)x), sqrt(e^((2/3)x^(sin(x)))), ln(sin(2x)^(sqrt(4x)))")
print("Parentheses are always needed for fractions but not decimals. \nAlways enter (x/3) as (1/3)x and (1/3x) as (1/3)x^(-1)")
print("sin(x)^(-1) means (1/sin(x)) but not arcsin(x) and try to express roots other than square roots as fractional power")
#f1 = "sqrt(e^((2/3)x^(sin(x))))e^((1/3)x)^(sin(ln(cot(x)+1)))"
#f2 = "e^((1/3)x)^(sin(ln(cot(x)+1)))sqrt(e^((2/3)x^(sin(x))))"
#f3 = "sin(2x)^(1/3)^(sqrt(4x))"
#f4 = 'sqrt((1/3)e^((2/3)x^(sin(x))))^(4.78(1+cot(x)))'
f5='sqrt(e^((2/3)x^(sin(x))))e^((1/3)x)^(sin(ln(cot(x)+1)))sqrt((1/3)e^((2/3)x^(sin(x))))^(4.78(1+cot(x)))sin(2x)^(1/3)^(sqrt(4x))tan(x)'
f6='sin(2x)^(1/3)^(sqrt(4x))sqrt(e^((2/3)x^(sin(x))))e^((1/3)x)^(sin(ln(cot(x)+1)))'
exp=input("Enter your expression in terms of x: ")
#exp=f5
nums=['0','1','2','3','4','5','6','7','8','9','.','/']
mathfunc=["sin(x)","cos(x)","tan(x)","sec(x)","csc(x)","cot(x)",
          "arcsin(x)", "arccos(x)", "arctan(x)", "arcsec(x)", "arccsc(x)", "arccot(x)",
          "ln(x)","log(x)","sqrt(x)","e^(x)","x^(x)"]
mt1,mt2,mt3,mt4,mt5,coefound,firstlbs,firstrbs=[],[],[],[],[],False,False,False
# number,noexclpow,power=[],[],[]
funcs,firstfunc,secfunc,thirdfunc,fourthfunc,fifthfunc=[],[],[],[],[],[]
secpros,thirdpros,fourthpros=[],[],[]
def getfirstnffunc():
    tki,tkj=0,0
    for i in range(len(exp)):
        if exp[i]==")":
            tki+=1
            for j in range(i+1):
                if exp[j]=="(": tkj+=1
                if j==i and tki!=tkj: tkj=0
            if tki!=0 and tkj!=0 and tki==tkj:
                # only one func
                if i==len(exp)-1:
                    firstfunc.append("".join(exp[:i+1]))
                    break
                # more than one func
                elif exp[i+1] in ["s","c","t","l","e","x"]:
                    firstfunc.append("".join(exp[:i+1]))
                    secpros.append("".join(exp[i+1:]))
                    break
                # involve power
                elif exp[i+1]=="^":
                    tkpi,tkpj=0,0
                    for k in range(i+2,len(exp)):
                        if exp[k]==")":
                            tkpi+=1
                            for l in range(i+2,k+1):
                                if exp[l]=="(": tkpj+=1
                                if l==k and tkpi!=tkpj: tkpj=0
                            if tkpi!=0 and tkpj!=0 and tkpi==tkpj:
                                # only one func involve power
                                if k==len(exp)-1:
                                    firstfunc.append("".join(exp[:k+1]))
                                    break
                                # more than one func after power
                                elif exp[k+1] in ["s","c","t","l","e","x"]:
                                    firstfunc.append("".join(exp[:k+1]))
                                    secpros.append("".join(exp[k+1:]))
    funcs.append(firstfunc[0])
def getsecnffunc():
    if len(secpros)!=0:
        ski,skj=0,0
        for i in range(len(secpros[0])):
            if secpros[0][i]==")":
                ski+=1
                for j in range(i+1):
                    if secpros[0][j]=="(": skj+=1
                    if j==i and ski!=skj: skj=0
                if ski!=0 and skj!=0 and ski==skj:
                    # only one func
                    if i==len(secpros[0])-1:
                        secfunc.append("".join(secpros[0][:i+1]))
                        break
                    # more than one func
                    elif secpros[0][i+1] in ["s","c","t","l","e","x"]:
                        secfunc.append("".join(secpros[0][:i+1]))
                        thirdpros.append("".join(secpros[0][i+1:]))
                        break
                    # involve power
                    elif secpros[0][i+1]=="^":
                        skpi,skpj=0,0
                        for k in range(i+2,len(secpros[0])):
                            if secpros[0][k]==")":
                                skpi+=1
                                for l in range(i+2,k+1):
                                    if secpros[0][l]=="(": skpj+=1
                                    if l==k and skpi!=skpj: skpj=0
                                if skpi!=0 and skpj!=0 and skpi==skpj:
                                    # only one func involve power
                                    if k==len(secpros[0])-1:
                                        secfunc.append("".join(secpros[0][:k+1]))
                                        break
                                    # more than one func after power
                                    elif secpros[0][k+1] in ["s","c","t","l","e","x"]:
                                        secfunc.append("".join(secpros[0][:k+1]))
                                        thirdpros.append("".join(secpros[0][k+1:]))
        funcs.append(secfunc[0])
def getthirdnffunc():
    if len(thirdpros)!=0:
        fki,fkj=0,0
        for i in range(len(thirdpros[0])):
            if thirdpros[0][i]==")":
                fki+=1
                for j in range(i+1):
                    if thirdpros[0][j]=="(": fkj+=1
                    if j==i and fki!=fkj: fkj=0
                if fki!=0 and fkj!=0 and fki==fkj:
                    # only one func
                    if i==len(thirdpros[0])-1:
                        thirdfunc.append("".join(thirdpros[0][:i+1]))
                        break
                    # more than one func
                    elif thirdpros[0][i+1] in ["s","c","t","l","e","x"]:
                        thirdfunc.append("".join(thirdpros[0][:i+1]))
                        fourthpros.append("".join(thirdpros[0][i+1:]))
                        break
                    # involve power
                    elif thirdpros[0][i+1]=="^":
                        fkpi,fkpj=0,0
                        for k in range(i+2,len(thirdpros[0])):
                            if thirdpros[0][k]==")":
                                fkpi+=1
                                for l in range(i+2,k+1):
                                    if thirdpros[0][l]=="(": fkpj+=1
                                    if l==k and fkpi!=fkpj: fkpj=0
                                if fkpi!=0 and fkpj!=0 and fkpi==fkpj:
                                    # only one func involve power
                                    if k==len(thirdpros[0])-1:
                                        thirdfunc.append("".join(thirdpros[0][:k+1]))
                                        break
                                    # more than one func after power
                                    elif thirdpros[0][k+1] in ["s","c","t","l","e","x"]:
                                        thirdfunc.append("".join(thirdpros[0][:k+1]))
                                        fourthpros.append("".join(thirdpros[0][k+1:]))
        funcs.append(thirdfunc[0])
def getfourthandfifthnffunc():
    if len(fourthpros)!=0:
        kki,kkj=0,0
        for i in range(len(fourthpros[0])):
            if fourthpros[0][i]==")":
                kki+=1
                for j in range(i+1):
                    if fourthpros[0][j]=="(": kkj+=1
                    if j==i and kki!=kkj: kkj=0
                if kki!=0 and kkj!=0 and kki==kkj:
                    # only one func
                    if i==len(fourthpros[0])-1:
                        fourthfunc.append("".join(fourthpros[0][:i+1]))
                        break
                    # more than one func
                    elif fourthpros[0][i+1] in ["s","c","t","l","e","x"]:
                        fourthfunc.append("".join(fourthpros[0][:i+1]))
                        fifthfunc.append("".join(fourthpros[0][i+1:]))
                        break
                    # involve power
                    elif fourthpros[0][i+1]=="^":
                        kkpi,kkpj=0,0
                        for k in range(i+2,len(fourthpros[0])):
                            if fourthpros[0][k]==")":
                                kkpi+=1
                                for l in range(i+2,k+1):
                                    if fourthpros[0][l]=="(": kkpj+=1
                                    if l==k and kkpi!=kkpj: kkpj=0
                                if kkpi!=0 and kkpj!=0 and kkpi==kkpj:
                                    # only one func involve power
                                    if k==len(fourthpros[0])-1:
                                        fourthfunc.append("".join(fourthpros[0][:k+1]))
                                        break
                                    # more than one func after power
                                    elif fourthpros[0][k+1] in ["s","c","t","l","e","x"]:
                                        fourthfunc.append("".join(fourthpros[0][:k+1]))
                                        fifthfunc.append("".join(fourthpros[0][k+1:]))
        funcs.append(fourthfunc[0])
        funcs.append(fifthfunc[0])

class Derivative:
      pass



d=Derivative()
getfirstnffunc()
getsecnffunc()
getthirdnffunc()
getfourthandfifthnffunc()
print(funcs)

#not solved

#Polynomial
#'x^(2)(2x^(3)+1)^(10)'
#Multiplication
#xarctan(x)
#Multiplication inside composite
#'sin(sqrt(x)ln(x))'
#Addition
#'sin(x)^(3)+sin(x^(3))'
#'sqrt(e^(x))+e^(sqrt(x))'
#Addition and multiplies
#'sec(x)tan(x)+ln(sec(x)+tan(x))'