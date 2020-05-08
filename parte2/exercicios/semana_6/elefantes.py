def elefantes(n, ini = 1):
    elefante = ''
    if n < 1:
        return ''
    else:
        if ini == 1:
            elefante = 'Um elefante '+ incomodam(ini) + 'muita gente\n'
            elefante = elefante + elefantes(n - 1, ini + 1)
        else:
            elefante = elefante + f'{ini} elefantes {incomodam(ini)}muito mais\n'
            elefante = elefante + f'{ini} elefantes incomodam muita gente\n'                        
            elefante = elefante + elefantes(n -1, ini + 1)
        
    return elefante      

def incomodam(n, ini = 1):
    if n < 1:
        return ''    
    else:
        if ini == 1 and n == 1:
            frase = 'incomoda ' + incomodam(n - 1, ini + 1)
        else:
            frase = 'incomodam ' + incomodam(n - 1, ini + 1)
    
    return frase

print(elefantes(1))