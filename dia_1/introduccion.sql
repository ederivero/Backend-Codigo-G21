-- Asi se define un comentario en las bases de datos
-- DDL (Data Definition Language) es un sublenguaje de SQL que sirve para definir como se almacenaran los datos
CREATE DATABASE pruebas;

-- Limpiara la terminal de nuestro psql
\! cls

CREATE TABLE alumnos (
    id SERIAL NOT NULL PRIMARY KEY, -- Columna que sera autoincrementable, no puede ser nula y sera llave primaria
    nombre TEXT NOT NULL, -- Sera texto y no puede ser nula
    email TEXT NOT NULL UNIQUE, -- Sera texto, no puede ser nula y debe ser unica (no se repite)
    matriculado BOOLEAN DEFAULT true, -- Sera booleana y su valor por defecto si no se ingresa sera TRUE
    fecha_nacimiento DATE NULL -- Sera fecha y puede tener valores nulos (su valor por defecto si no se define)
);


-- Para agregar columnas a una tabla ya existente
ALTER TABLE alumnos ADD COLUMN apellidos TEXT;

-- Cambiamos el tipo de dato de la columna nombre ahora sera VARCHAR(100)
-- NOTA: solamente se puede cambiar el tipo de dato si la columna no tiene registros
-- o si ya tiene registros entonces el nuevo tipo de dato debe ser compatible con el antiguo
-- no podemos cambiar de un TEXT > INT o de un INT > FECHA
ALTER TABLE alumnos ALTER COLUMN nombre TYPE VARCHAR(100);


-- Elimina de manera permanente e irreversible la tabla y toda la informacion que hay en ella
DROP TABLE direcciones;
DROP DATABASE NOMBRE_BD;

-- DML (Data Manipulation Language)
-- Es una sublenguaje para poner interactuar con la informacion de las tablas

-- Muestra la configuracion de la tabla con todas sus columnas y restricciones
\d alumnos


-- Insertamos un registro en la bd definiendo las columnas
INSERT INTO alumnos (id, nombre, email, matriculado, fecha_nacimiento, apellidos)
VALUES (DEFAULT, 'Eduardo', 'ederiveroman@gmail.com', TRUE, '1992-08-01', 'De Rivero');


-- Insertamos dos o mas registros sin la necesidad de colocar las columnas
INSERT INTO alumnos VALUES (DEFAULT, 'Cesar', 'ccenteno@tecsup.edu.pe', DEFAULT, '1995-06-02', 'Centeno'),
(DEFAULT, 'Javier', 'jwiesse@gmail.com', FALSE, '2000-02-14', 'Wiesse'),
(DEFAULT, 'Farit', 'fespinoza@gmail.com', TRUE, '1990-07-28', 'Espinoza');


-- Seleccionar una columna
SELECT nombre FROM alumnos;

-- Seleccionar dos o mas columnas
SELECT id, nombre FROM alumnos;

-- Seleccionar todas las columnas
SELECT * FROM alumnos;

-- Agregar una condicion para filtrar datos
SELECT * FROM alumnos WHERE matriculado = FALSE;

-- Mostrara todos los alumnos que esten matriculados Y su id sea menor que 3
SELECT * FROM alumnos WHERE matriculado = TRUE AND id < 3;

-- Mostrara todos los alumnos que esten matriculados O su id sea menor que 3
SELECT * FROM alumnos WHERE matriculado = TRUE OR id < 3;