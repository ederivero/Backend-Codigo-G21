-- USAR LA BD prueba
CREATE TABLE demostracion_triggers(
    id SERIAL PRIMARY KEY NOT NULL,
    mensaje TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);


-- https://www.postgresql.org/docs/current/sql-createfunction.html
CREATE FUNCTION registrar_accion()
RETURNS TRIGGER AS $$
BEGIN
    -- Insertar un mensaje en la tabla de demostracion
    INSERT INTO demostracion_triggers(mensaje) VALUES ('SE INSERTO UN NUEVO REGISTRO');
    -- NEW > sera la informacion que me viene en el trigger, la informacion que se agregara ni bien se ejecute el trigger
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- https://www.postgresql.org/docs/current/sql-createtrigger.html
CREATE TRIGGER trigger_registrar_registros
AFTER INSERT ON clientes
FOR EACH ROW -- Cada vez que se haga un nuevo ingreso de un cliente se ejecutara el trigger
EXECUTE FUNCTION registrar_accion();

-- 
CREATE OR REPLACE FUNCTION crear_clientes_y_cuentas(
    nombre_cliente TEXT,
    correo_cliente TEXT,
    status_cliente status_enum,
    cliente_activo BOOLEAN,
    tipo_moneda tipo_moneda_enum)
RETURNS VOID AS $$
-- Justo antes de empezar la funcion tenemos que declara las variables a utilizar en la funcion
DECLARE
    nuevo_cliente_id INT; -- Este cliente_id lo usare para al momento de crear la cuenta relacionarlo con el
-- Inicia la ejecucion de la funcion
BEGIN
    -- RETURNING se puede llamar cuando hacemos un INSERT | UPDATE | DELETE y sirve para retorna la informacion resultante de la operacion
    INSERT INTO clientes (nombre, correo, status, activo) VALUES (nombre_cliente, correo_cliente, status_cliente, cliente_activo) RETURNING id INTO nuevo_cliente_id;

    -- Ahora procedemos a crear la cuenta del cliente
    INSERT INTO cuentas (numero_cuenta, tipo_moneda, cliente_id) VALUES ('', tipo_moneda, nuevo_cliente_id);
END;
$$ LANGUAGE plpgsql;


-- Para ver las funciones que existen en la bd 
\df


-- https://www.postgresql.org/docs/current/tutorial-transactions.html
BEGIN;
INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    ( 4, null, 100, NOW());


INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    (4, 3, 20, NOW());


INSERT INTO movimientos (cuenta_origen, cuenta_destino, monto, fecha_operacion) VALUES
                    (null, 4, 40, NOW());

-- TODO ESTA BIEN Guardamos los cambios de manera permanente
COMMIT;

-- SI LLEGASE A FALLAR ALGO PODEMOS DEJAR SIN EFECTO ESTE GRUPO DE OPERACION
ROLLBACK;