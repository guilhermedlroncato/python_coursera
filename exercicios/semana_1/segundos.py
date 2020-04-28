segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = (segundos // 3600) // 24
horas =  (segundos // 3600) % 24
seg_restantes = segundos % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(dia, 'dias,', horas, 'horas,', minutos, 'minutos e', seg_restantes_final, 'segundos')