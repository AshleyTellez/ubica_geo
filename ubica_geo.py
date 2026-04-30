import pandas as pd
import matplotlib.pyplot as plt
base= pd.read_stata('C:/Users/ast/.spyder-py3/concentradohogar.dta')
base = base[base['ubica_geo'] == '15033']

#PRIMERA
clase=base['clase_hog'].value_counts ()
#print(clase)
#plt.bar(clase.index, clase.values, color='skyblue')
#plt.show()


#SEGUNDA
SUELDO=base['sueldos'].describe()
#print(SUELDO)

#TERCERA
ING=base['ing_cor'].describe()
#print(ING)

#CUARTA
JEFE=base['sexo_jefe'].value_counts ()
#print(JEFE)
#plt.bar(JEFE.index, JEFE.values, color='skyblue')
#plt.show()

#QUINTA
HOMBRE=base[(base['sexo_jefe']== '1')]
H=HOMBRE['ing_cor'].describe()
#print(H)

MUJER=base[(base['sexo_jefe']== '2')]
M=MUJER['ing_cor'].describe()
#print(M)

#SEXTA
LIMP=HOMBRE['limpieza'].describe()
#print(LIMP)

limpM=MUJER['limpieza'].describe()
#(limpM)

#SEPTIMA
AGUA=base['agua'].describe()
#print(AGUA)

#OCTAVA
medi=base['medicinas'].describe()
#print(medi)

#NOVENA
alimento =base['alimentos'].describe()
#print(alimento)

#DECIMA
serv =base['servicio'].describe()
#print(serv)


print(base).head
