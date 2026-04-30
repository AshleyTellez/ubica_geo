import pandas as pd
base= pd.read_stata('C:/Users/asti/.spyder-py3/concentradohogar.dta')
base1=base[(base['ubica_geo']=='15033')]


#Indicador 1 consumo de carne
base2=base1.groupby(['folioviv']).aggregate({'carnes':'mean'})
print(base2['carnes'].describe())

#ndicador 2 Consumo de verduras
base2=base1.groupby(['folioviv']).aggregate({'verduras':'mean'})
print(base2['verduras'].describe())

#Indicador 3 Consumo de frutas
base2=base1.groupby(['folioviv']).aggregate({'frutas':'mean'})
print(base2['frutas'].describe())

#Indicador 4 Consumo de tabaco
base2=base1.groupby(['folioviv']).aggregate({'tabaco':'mean'})
print(base2['tabaco'].describe())

#Indicador 5 Consumo de medicinas
base2=base1.groupby(['folioviv']).aggregate({'medicinas':'mean'})
print(base2['medicinas'].describe())

#Indicador 6 Edad del jefe de familia
base2=base1.groupby(['folioviv']).aggregate({'edad_jefe':'mean'})
print(base2['edad_jefe'].describe())

#Indicador 7 Comparacion de total de integrantes con total de ocupados                   
suma_tot_integ = base1['tot_integ'].sum()
suma_ocupados = base1['ocupados'].sum()
print(suma_tot_integ)
print(suma_ocupados)

media_tot_integ = base1['tot_integ'].mean()
media_ocupados = base1['ocupados'].mean()
print(media_tot_integ)
print(media_ocupados)

#Indicador 8 Educacion del jefe del hogar
#01 Sin instrucción
#02 Preescolar
#03 Primaria incompleta
#04 Primaria completa
#05 Secundaria incompleta
#06 Secundaria completa
#07 Preparatoria incompleta
#08 Preparatoria completa
#09 Profesional incompleta
#10 Profesional completa
#11 Posgrado

educacion=base1['educa_jefe'].value_counts ()
print(educacion)


#Indicador 9 Estrato socioeconomico
#1 Bajo2 Medio bajo 3 Medio alto 4 Alto

clase=base1['clase_hog'].value_counts ()
print(clase)

#Indicador 10 comparcion de gasto en educacion Ecatepec y Miguel Hidalgo
#Ecatepec
educacionE=base1.groupby(['folioviv']).aggregate({'educacion':'mean'})
print(educacionE['educacion'].describe())

MH=base[(base['ubica_geo']=='09016')]
educacionMH=MH.groupby(['folioviv']).aggregate({'educacion':'mean'})
print(educacionMH['educacion'].describe())



