# Escribir un programa que almacene el diccionario con los créditos de las 
# asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
#  muestre por pantalla los créditos de cada asignatura en el 
#  formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de 
#  las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también
#   el número total de créditos del curso.

course = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_credits = 0
for subject, credits in course.items():
    print(subject, 'tiene', credits, 'créditos')
    total_credits += credits
print('Número total de créditos del curso: ', total_credits)

# output:
# Matemáticas tiene 6 créditos
# Física tiene 4 créditos
# Química tiene 5 créditos
# Número total de créditos del curso:  15