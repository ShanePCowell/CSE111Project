DROP TABLE car;
DROP TABLE trim;
DROP TABLE engine;
DROP TABLE color;
DROP TABLE color_Trim;
DROP TABLE transmission;
DROP TABLE wheel;
DROP TABLE engine_Transmission;
DROP TABLE manufacturer;


CREATE TABLE car (
    c_model VARCHAR (255)  NOT NULL,
    c_year DECIMAL (4, 0) NOT NULL,
    c_make  VARCHAR (255) NOT NULL,
    c_trim VARCHAR (255),
    c_bodyType VARCHAR (255) NOT NULL,
    c_wheelBase DECIMAL(2, 0) NOT NULL
);  

CREATE TABLE trim (
    t_model VARCHAR (255) NOT NULL,
    t_id VARCHAR (255)  NOT NULL,
    t_engine VARCHAR (255) NOT NULL,
    t_transmission  VARCHAR (255) NOT NULL,
    t_wheels VARCHAR (255) NOT NULL,
    t_accel DECIMAL(2, 0),
    t_eco DECIMAL(2, 0) NOT NULL,
    t_weight DECIMAL(2, 0) NOT NULL,
    t_speed DECIMAL(2, 0) NOT NULL,
    t_price DECIMAL(10, 2) NOT NULL
);  

CREATE TABLE engine (
    e_id VARCHAR (255)  NOT NULL,
    e_cylinders INT (2, 0), 
    e_layout  VARCHAR (255),
    e_fuelType  VARCHAR (255) NOT NULL,
    e_displacement DECIMAL (2, 0)
);

CREATE TABLE transmission (
    tr_id VARCHAR (255)  NOT NULL,
    tr_gears INT (2, 0) NOT NULL,
    tr_driveRatio  VARCHAR (255) NOT NULL
);

CREATE TABLE wheel (
    w_id VARCHAR (255)  NOT NULL,
    w_diameter DECIMAL (2, 0) NOT NULL,
    w_rim  VARCHAR (255) NOT NULL,
    w_size  DECIMAL (2, 0) NOT NULL
);

CREATE TABLE color_Trim (
    c_id VARCHAR (255) NOT NULL,
    t_id VARCHAR (255) NOT NULL
);

CREATE TABLE engine_Transmission (
    e_id VARCHAR (255) NOT NULL,
    tr_id VARCHAR (255) NOT NULL
);

CREATE TABLE color (
    c_id VARCHAR (255) NOT NULL,
    c_finish VARCHAR (255) NOT NULL,
    c_color  VARCHAR (255) NOT NULL
);

CREATE TABLE manufacturer (
    m_make VARCHAR (255) NOT NULL,
    m_nationOfOrigin VARCHAR (255) NOT NULL
);



DELETE FROM car;
DELETE FROM engine;
DELETE FROM trim;
DELETE FROM color;
DELETE FROM color_Trim;
DELETE FROM transmission;
DELETE FROM engine_Transmission;
DELETE FROM wheel;
DELETE FROM manufacturer;

INSERT INTO car(c_model, c_year, c_make, c_trim, c_bodyType, c_wheelBase)
VALUES ('240SX', 1993, 'NISSAN', '240SX-SE', 'COUPE', 97.4);

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('240SX', 'SE', 'KA24E', '"KA24 5-speed"', '240SX 15s', 8, 22, 2800, 130, 15000.00);

INSERT INTO color_Trim(c_id, t_id) VALUES ('RED', '240SX-SE');
INSERT INTO color_Trim(c_id, t_id) VALUES ('BLUE', '240SX-SE');