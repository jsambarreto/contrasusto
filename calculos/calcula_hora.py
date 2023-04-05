#!.\.env python3

def calcula_hora(mes, ano):
  if (mes <=12 and ano==2018):
    horas_aula = 16.12
    return horas_aula
  if (mes<=10 and ano==2019):
    horas_aula=16.40
    return horas_aula
  if (mes<=8 and ano==2020):
    horas_aula=29.68
    return horas_aula
  if (mes<=11 and ano==2020):
    horas_aula=24.83
    return horas_aula
  else:
    horas_aula=29.68
    return horas_aula
  
