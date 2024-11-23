-- Asi se puede obtener la informacion de dos tablas relacionadas entre si
SELECT * FROM clientes INNER JOIN cuentas ON clientes.id = cuentas.cliente_id;

-- Para declara un left JOIN que seria de manera obligatoria todo lo de la izquierda y opcionalmente lo de la derecha
SELECT * FROM clientes LEFT JOIN cuentas ON clientes.id = cuentas.cliente_id;

-- Para declara un RIGHT JOIN que seria de manera obligatoria todo lo de la derecha y opcionalmente lo de la izquierda
SELECT * FROM clientes RIGHT JOIN cuentas ON clientes.id = cuentas.cliente_id;


-- Tenemos que declara la tabla de la columna si vamos a seleccionar una columna que es ambigua en las dos tablas
SELECT clientes.id, clientes.nombre, cuentas.id, cuentas.numero_cuenta FROM clientes LEFT JOIN cuentas ON clientes.id=cuentas.cliente_id;

-- Ademas, podemos agregar un alias a nuestra tabla para hacer mas corta en su nombre
SELECT cli.id, cli.nombre, cue.id, cue.numero_cuenta FROM clientes AS cli LEFT JOIN cuentas AS cue ON cli.id=cue.cliente_id;

-- EJERCICIO
-- Devolver la informacion (nombre, correo, status, numero_cuenta, tipo_moneda)
SELECT cli.nombre, cli.correo, cli.status, cue.numero_cuenta, cue.tipo_moneda 
FROM clientes AS cli 
        INNER JOIN cuentas AS cue ON cli.id = cue.cliente_id;

-- Devolver la informacion de los usuario que tengan cuenta que no sea en soles (solo quiero el nombre y correo)
SELECT cli.nombre, cli.correo 
FROM clientes AS cli 
        INNER JOIN cuentas AS cue ON cli.id = cue.cliente_id
WHERE cue.tipo_moneda != 'SOLES';

-- Devolver el nombre, mantenimiento y tipo_moneda 
SELECT cli.nombre, cue.mantenimiento, cue.tipo_moneda 
FROM clientes AS cli 
        INNER JOIN cuentas AS cue ON cli.id = cue.cliente_id;

-- Devolver el usuario (correo, nombre) y el tipo_moneda de los usuarios que tengan correo gmail y que su mantenimiento sea menor que 1.1 y que el usuario este activo
SELECT cli.correo, cli.nombre , cue.tipo_moneda 
FROM clientes AS cli INNER JOIN cuentas AS cue ON cli.id = cue.cliente_id
WHERE cli.correo ILIKE '%gmail.com' AND cue.mantenimiento < 1.1 AND cli.activo = TRUE;

-- Devolver cuantos clientes no tienen cuentas
SELECT COUNT(*) 
FROM clientes AS cli 
    LEFT JOIN cuentas AS cue ON cli.id = cue.cliente_id
WHERE cue.numero_cuenta IS NULL;


-- Si queremos hacer condicional con una columna que es boolean podemos solamente declara la columna si queremos el valor verdadero
-- WHERE activo;
-- Y si queremos el valor falso entonces usamos el NOT
-- WHERE NOT activo;


-- Para hacer busquedas con valores nulos se utiliza la palabra IS 
-- WHERE columna IS NULL;
-- WHERE columna IS NOT NULL;


-- CREAR TABLA LLAMADA movimientos
-- id serial primary key not null
-- cuenta_origen RELACION con la tabla cuentas puede ser null
-- cuenta_destino RELACION con la tabla cuentas NO puede ser null
-- monto float NO puede ser null
-- fecha_operacion timestamp la hora del servidor por defecto

CREATE TABLE movimientos (
    id SERIAL PRIMARY KEY NOT NULL,
    cuenta_origen INT,
    cuenta_destino INT NOT NULL,
    monto FLOAT NOT NULL,
    fecha_operacion TIMESTAMP DEFAULT NOW(),
    -- RELACIONES
    CONSTRAINT fk_cuenta_origen FOREIGN KEY(cuenta_origen) REFERENCES cuentas(id),
    CONSTRAINT fk_cuenta_destino FOREIGN KEY(cuenta_destino) REFERENCES cuentas(id)
);

-- Asi quitamos una configuracion de una columna en este caso, el not null
ALTER TABLE movimientos ALTER COLUMN cuenta_destino DROP NOT NULL;


INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                        (null, 1, 100.10, '2024-07-01T14:15:17'),
                        (null, 2, 500.20, '2024-07-06T09:30:15'),
                        (null, 3, 650.00, '2024-07-06T15:29:18'),
                        (null, 4, 456.00, '2024-07-08T10:15:17'),
                        (null, 5, 500.00, '2024-07-10T17:18:24'),
                        (null, 6, 1050.24, '2024-07-04T12:12:12'),
                        (null, 7, 984.78, '2024-07-09TT11:06:49'),
                        (1,2, 40.30, '2024-07-10T10:10:10'),
                        (4,7, 350.00, '2024-07-16T20:15:35'),
                        (3, null, 50.00, '2024-07-16T22:15:10'),
                        (5, null, 100.00, '2024-07-17T10:19:25'),
                        (6, null, 350.28, '2024-07-18T14:15:16');


SELECT CASE
WHEN activo IS TRUE THEN 'ESTA ACTIVO EL CLIENTE'
WHEN activo IS FALSE THEN 'EL CLIENTE NO PUEDE HACER OPERACIONES'
ELSE 'HUBO UN ERROR'
END,
activo
FROM clientes;

SELECT CASE activo
WHEN TRUE THEN 'ESTA ACTIVO EL CLIENTE'
WHEN FALSE THEN 'EL CLIENTE NO PUEDE HACER OPERACIONES'
ELSE 'HUBO UN ERROR'
END,
activo
FROM clientes;

-- Usando el switch case Mostrar los movimientos que sean DEPOSITO, TRANSFERENCIA o RETIRO, siendo:
-- DEPOSITO: Cuando no hay cuenta_origen pero si cuenta destino
-- TRANSFERENCIA: Cuando hay cuenta_origen y cuenta_destino
-- RETIRO : Cuando hay cuenta_origen y no hay cuenta_destino
-- y sus montos

SELECT CASE
WHEN cuenta_origen IS NULL AND cuenta_destino IS NOT NULL THEN 'DEPOSITO'
WHEN cuenta_origen IS NOT NULL AND cuenta_destino IS NOT NULL THEN 'TRANSFERENCIA'
WHEN cuenta_origen IS NOT NULL AND cuenta_destino IS NULL THEN 'RETIRO'
END,
monto
FROM movimientos;


-- En base al correo de los clientes hacer lo siguiente
-- Si el correo es gmail > 'ES UNA PERSONA JOVEN'
-- Si el correo es hotmail > 'ES UNA PERSONA ADULTA'
-- Si el correo es yahoo > 'ES UN DINOSAURIO'
-- PISTA: Usar el like en el CASE
SELECT correo,
    CASE
        WHEN correo ILIKE '%gmail.com' THEN 'ES UNA PERSONA JOVEN'
        WHEN correo ILIKE '%hotmail.com' THEN 'ES UNA PERSONA ADULTA'
        WHEN correo ILIKE '%yahoo%' THEN 'ES UN DINOSAURIO'
        ELSE 'DOMINIO DESCONOCIDO'
    END AS calculo_edad_persona
FROM clientes;

-- Usando la funcion de agregacion SUM obtener los debitos de todas cuenta (lo que sale) cuenta_origen NO ES NULA
SELECT cuenta_origen, SUM(monto)
FROM movimientos
WHERE cuenta_origen IS NOT NULL
GROUP BY cuenta_origen;

-- Obtener los creditos de todas las cuentas (lo que llega / entra) > cuanta_destino NO ES NULA
SELECT cuenta_destino, SUM(monto)
FROM movimientos
WHERE cuenta_destino IS NOT NULL
GROUP BY cuenta_destino;