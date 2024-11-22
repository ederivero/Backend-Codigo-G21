-- Seguiremos utilizando la bd de finanzas

-- Crear una tabla cuentas 
-- NOTA: NO CREAR LA TABLA

-- id autoincrementable primary key
-- numero_cuenta text not null unico,
-- tipo_moneda SOLES | DOLARES | EUROS no nulo
-- fecha_creacion timestamp valor actual del servidor no nulo
-- mantenimiento float puede ser nulo
CREATE TYPE tipo_moneda_enum AS ENUM ('SOLES', 'DOLARES', 'EUROS');

-- Un cliente puede tiener muchas cuentas PERO cada cuenta le va a pertener a un solo cliente
CREATE TABLE cuentas (
    id SERIAL PRIMARY KEY NOT NULL,
    numero_cuenta TEXT NOT NULL UNIQUE,
    tipo_moneda tipo_moneda_enum NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT NOW() NOT NULL,
    mantenimiento FLOAT,
    -- RELACIONES
    cliente_id INT NOT NULL,
    -- Llave foranea utilizando la columna cliente_id y que se va a referencia con la columna id de la tabla clientes
    CONSTRAINT fk_clientes FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);


INSERT INTO cuentas (numero_cuenta, tipo_moneda, fecha_creacion, mantenimiento, cliente_id) VALUES
('0f302b7e-41b6-45e9-950c-d2640f3ddcdf', 'SOLES', '2023-10-08T10:05', 1.5, 1),
('7160f103-dc2a-4e67-9123-3d795bf4938b', 'SOLES', '2024-02-01T14:23', 1, 2),
('b2eeb8ab-f06b-49df-8dac-332b2b48d7ff', 'DOLARES', '2020-12-08T16:17', 0, 1),
('82c51e22-f4a6-4430-b401-05e458979c1b', 'SOLES', '2022-05-14T09:45', 1, 3),
('57c54a3c-0a92-45b7-b888-0cbf827c93f8', 'SOLES', '2024-03-14T11:28', 1.2, 4),
('c62ed24c-430b-462f-bdb3-ba79199bcffc', 'EUROS', '2023-10-04T12:27', 0.5, 3),
('2343b92e-152a-4316-a4af-7406f8e551b8', 'SOLES', '2023-11-09T11:11', 0, 2);



-- FUNCIONES DE AGREGACION
-- Cuando queremos utilizar una funcion de agregacion nos vemos en la necesidad de agregar la clausula GROUP BY para poder hacer el agrupamiento antes de realizar la operacion de la funcion 
SELECT avg(mantenimiento), tipo_moneda FROM cuentas GROUP BY tipo_moneda;


-- El count sirve para contar los registros en base al group by y tambien se podria agregar una clausula WHERE
 SELECT tipo_moneda, count(tipo_moneda) FROM cuentas GROUP BY tipo_moneda;

-- Dame la cuenta que paga mas mantenimiento
-- Usar la funcion max
SELECT * FROM cuentas WHERE mantenimiento = (SELECT MAX(mantenimiento) FROM cuentas);

-- Dame la cuenta que paga menos mantenimiento
-- Usar la funcion min
SELECT * FROM cuentas WHERE mantenimiento = (SELECT MIN(mantenimiento) FROM cuentas);


-- Que cliente tiene mas cuentas
SELECT cliente_id, count(cliente_id) FROM cuentas GROUP BY cliente_id ORDER BY count DESC;

-- Mostrar los numeros de cuenta, su tipo de moneda y su fecha de creacion ordenada de la mas reciente a las mas antigua
SELECT numero_cuenta, tipo_moneda, fecha_creacion FROM cuentas ORDER BY fecha_creacion DESC;


-- Ingresar un nuevo cliente 
INSERT INTO clientes (nombre, correo, status, activo) VALUES
('Eduardo de Rivero Manrique', 'ederivero@gmail.com', 'BUEN_CLIENTE', true);


-- Queries y guardarlas de manera temporal mientras ejecutamos la query principal
WITH conteo AS (SELECT cliente_id, count(cliente_id) AS total FROM cuentas GROUP BY cliente_id),
conteo_maximo AS (SELECT MAX(total) AS conteo_maximo_total  FROM conteo) -- 2
SELECT cliente_id, total FROM conteo WHERE total = (SELECT conteo_maximo_total FROM conteo_maximo);


SELECT cliente_id ,count(cliente_id) FROM cuentas
GROUP BY cliente_id 
HAVING count(cliente_id) = (SELECT count(cliente_id) FROM cuentas GROUP BY cliente_id LIMIT 1)