segundos = int(input('Entre com o valor dos segundos: '))

horas =  segundos // 3600
seg_restantes = segundos % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(horas, ' horas, ', minutos, ' minutos, ', seg_restantes_final, ' segundos')
