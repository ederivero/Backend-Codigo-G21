-- Si queremos buscar los alumnos por su correo y que el texto no sea sensible a mayus y minus usamos el operador ILIKE
SELECT * FROM alumnos WHERE email ILIKE '%GmAiL%';

-- Si queremos buscar los alumnos cuyo correo contenga el texto gmail en cualquier posicion pero sensible a mayus y minus
SELECT * FROM alumnos WHERE email LIKE '%gmail%';

-- Mostrara todos los alumnos cuyo correo terminan en gmail
SELECT * FROM alumnos WHERE email LIKE '%gmail';


-- Mostrar todos los alumnos en cuya segunda posicion tengamos la letra r
SELECT * FROM alumnos WHERE nombre ILIKE '__r%';

-- Mostrar todos los alumnos cuyo nombre tengan en la cuarta posicion la letra i y que terminen con letra r 
SELECT * FROM alumnos WHERE nombre ILIKE '___i%r';

-- Para realizar un ordenamiento utilizamos la clausula ORDER BY y los valores son ASC | DESC
SELECT * FROM alumnos ORDER BY nombre DESC, email ASC;

-- Actualizara todos los nombre y apellidos de los alumnos cuyo id = 1 
UPDATE alumnos SET nombre = 'Ramiro', apellidos = 'Perez' WHERE id = 1;

-- Eliminara a todos los alumnos que cumplan la condicion
DELETE FROM alumnos WHERE id = 1;