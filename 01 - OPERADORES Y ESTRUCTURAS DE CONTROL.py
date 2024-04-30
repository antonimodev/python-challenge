"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """
##########################
# OPERADORES ARITMÉTICOS #
##########################

# Operador de suma
suma = 2 + 2
print(f"Operador suma: 2 + 2 = {suma}")

# Operador de resta
resta = 2 - 2
print(f"Operador resta: 2 - 2 = {resta}")

# Operador de multiplicación
multiplicacion = 2 * 2
print(f"Operador multiplicación: 2 * 2 = {multiplicacion}")

# Operador de división
division = 2 / 2
print(f"Operador división: 2 / 2 = {division}")

# Operador de división entera
division_entera = 2 // 2
print(f"Operador división entera: 2 // 2 = {division_entera}")

# Operador de módulo
modulo = 2 % 2
print(f"Operador módulo: 2 % 2 = {modulo}")

# Operador de exponente
exponente = 2 ** 2
print(f"Operador exponente: 2 ** 2 = {exponente}")

######################
# OPERADORES LÓGICOS #
######################

# Operador '&&' // 'and'
# Devuelve True si los dos son verdaderos
print(f"Operador 'and': True and False = {True and False}")

# Operador '||' // 'or'
# Devuelve True si alguno de los dos es verdadero
print(f"Operador 'or': True or false = {True or False}")

# Operador 'not'
# Devuelve True si el operando es falso (complemento)
print(f"Operador 'not': not True = {not True}")

#############################
# OPERADORES DE COMPARACIÓN #
#############################

# Operador '==' // Igual que
# Devuelve True si los dos operandos son iguales
print(f"Operador '==': 10 == 20 = {10 == 20}")

# Operador '!=' // No es igual que
# Devuelve True si los dos operandos son diferentes
print(f"Operador '!=': 10 != 20 = {10 != 20}")

# Operador '<' // Menor que
# Devuelve True si el operando de la izquierda es menor que el de la derecha
print(f"Operador '<': 10 < 20 = {10 < 20}")

# Operador '<=' // Menor o igual que
# Devuelve True si el operando de la izquierda es menor o igual que el de la derecha
print(f"Operador '<=': 10 <= 20 = {10 <= 20}")

# Operador '>' // Mayor que
# Devuelve True si el operando de la izquierda es mayor que el de la derecha
print(f"Operador '>': 10 > 20 = {10 > 20}")

# Operador '>=' // Mayor o igual que
# Devuelve True si el operando de la izquierda es mayor o igual que el de la derecha
print(f"Operador '>=': 10 >= 20 = {10 >= 20}")

############################
# OPERADORES DE ASIGNACIÓN #
############################

a = 10

# Operador '=' // Asignación
# Asigna el valor del operando de la derecha al operando de la izquierda
print(f"Operador '=': a = 10 => a = {a}")

# Operador '+=' // Suma y asignación
# Suma el operando de la derecha al operando de la izquierda y asigna el resultado al operando de la izquierda
a += 5
print(f"Operador '+=': a += 5 => a = {a}")

# Operador '-=' // Resta y asignación
# Resta el operando de la derecha al operando de la izquierda y asigna el resultado al operando de la izquierda
a -= 2
print(f"Operador '-=': a -= 2 => a = {a}")

# Operador '*=' // Multiplicación y asignación
# Multiplica el operando de la derecha por el operando de la izquierda y asigna el resultado al operando de la izquierda
a *= 3
print(f"Operador '*=': a *= 3 => a = {a}")

# Operador '/=' // División y asignación
# Divide el operando de la izquierda por el operando de la derecha y asigna el resultado al operando de la izquierda
a /= 4
print(f"Operador '/=': a /= 4 => a = {a}")

# Operador '%=' // Módulo y asignación
# Toma el módulo del operando de la izquierda con el operando de la derecha y asigna el resultado al operando de la izquierda
a %= 3
print(f"Operador '%=': a %= 3 => a = {a}")

# Operador '**=' // Exponente y asignación
# Eleva el operando de la izquierda al exponente del operando de la derecha y asigna el resultado al operando de la izquierda
a **= 2
print(f"Operador '**=': a **= 2 => a = {a}")

# Operador '//=' // División entera y asignación
# Divide el operando de la izquierda por el operando de la derecha, redondea el resultado hacia abajo a la entera más cercana y asigna el resultado al operando de la izquierda
a //= 2
print(f"Operador '//=': a //= 2 => a = {a}")

#######################################################
""" 				#	EJERCICIOS	#
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
#######################################################

# DEL 10 AL 55. OMITIR 16 Y MÚLTIPLOS DE 3
for i in range(10, 56):
	if (i % 2 == 0) and (i != 16) and (i % 3 != 0):
		print(i)

# DEL 20 AL 100. OMITIR MÚLTIPLOS DE 5
for i in range(20, 101):
	if (i % 5 != 0):
		print(i)

# DEL 1 AL 1000 MÚLTIPLOS DE 7. OMITIR MÚLTIPLOS DE 5
for i in range(1, 1001):
	if (i % 7 == 0) and (i % 5 != 0):
		print(i)

# DEL 50 AL 150. MÚLTIPLOS DE 3 Y 5. OMITIR MÚLTIPLOS DE 10
for i in range(50, 151):
	if (i % 3 == 0) and (i % 5 == 0) and (i % 10 != 0):
		print(i)

# DEL 200 AL 300. MÚLTIPLOS DE 4. OMITIR MÚLTIPLOS DE 6 Y 8
for i in range(200, 301):
	if (i % 4 == 0) and (i % 6 != 0) and (i % 8 != 0):
		print(i)

# DEL 100 AL 200. MÚLTIPLOS DE 5. OMITIR EL 150 Y MÚLTIPLOS DE 10
for i in range(100, 201):
	if (i % 5 == 0) and (i != 150) and (i % 10 != 0):
		print(i)

# Crea un programa que imprima todos los números primos entre 1 y 1000
# que también sean múltiplos de 7 pero no de 5.