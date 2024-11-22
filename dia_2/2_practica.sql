-- Crear una base datos llamada finanzas
CREATE DATABASE finanzas;

-- Crear una tabla en la cual registremos la informacion de los clientes de la siguiente manera:
-- id autoincrementable primary key
-- nombre texto no puede ser nulo
-- correo unico(no se repite) no puede ser nulo
-- status texto no puede ser nulo
-- activo booleano por defecto sea verdadero
-- fecha_creacion timestamp

-- ENUMERABLE: sirve para indicar un cierto numero de valores permitidos que pueden almacenarse en esta columna
CREATE TYPE status_enum AS ENUM ('BUEN_CLIENTE', 'CLIENTE_RIESGOSO', 'CLIENTE PELIGROSO');

CREATE TABLE clientes(
    id SERIAL NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    status status_enum NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT NOW() -- Agarra la hora y fecha actual del servidor cuando se realice una insercion
);

-- Si ya crearon la tabla con la columna status y el tipo de dato text, para cambiar el tipo de dato:
ALTER TABLE clientes ALTER COLUMN status TYPE status_enum USING status::status_enum;

-- Para renombrar el nombre de una tabla
ALTER TABLE finanzas RENAME TO clientes;

-- Insertamos la siguiente informacion
INSERT INTO clientes (nombre, correo, status, activo) VALUES
('Rodrigo Juarez Quispe', 'rjuarez@gmail.com', 'BUEN_CLIENTE', true),
('Mariana Sanchez Gil', 'msanchez@hotmail.com', 'CLIENTE_RIESGOSO', true),
('Juliana Taco Martinez', 'jtaco@gmail.com', 'BUEN_CLIENTE', true),
('Gabriel Gonza Perez', 'ggonza@yahoo.es', 'CLIENTE PELIGROSO', false);

-- Mostrar todos los clientes que sea BUEN_CLIENTE
SELECT * FROM clientes WHERE status = 'BUEN_CLIENTE';

-- Mostrar todos los clientes que esten activos y que sean CLIENTE_RIESGOSO
SELECT * FROM clientes WHERE status = 'CLIENTE_RIESGOSO' AND activo = true;

-- Mostrar los clientes que tengan correo gmail o que sean CLIENTE_RIESGOSO
SELECT * FROM clientes WHERE correo ILIKE '%gmail.com' OR status = 'CLIENTE_RIESGOSO';

-- Mostrar todos los clientes cuyo nombre tengan el apellido Gonza o Juarez y que no esten activos
-- Gabriel Gonza
SELECT * FROM clientes WHERE (nombre ILIKE '%Gonza%' OR nombre ILIKE '%Juarez%') AND activo = FALSE;

-- Mostrar todos los clientes cuyo nombre tengan el apellido Gonza o Juarez y que esten activos
-- Rodrigo Juarez
SELECT * FROM clientes WHERE (nombre ILIKE '%Gonza%' OR nombre ILIKE '%Juarez%') AND activo = TRUE;