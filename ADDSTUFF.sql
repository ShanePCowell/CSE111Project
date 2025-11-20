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
    e_displacement DECIMAL (2, 0), 
    e_horsepower DECIMAL (4, 0) NOT NULL,
    e_torque DECIMAL (4, 0) NOT NULL,
    e_redline DECIMAL (4, 0) NOT NULL
);

CREATE TABLE transmission (
    tr_id VARCHAR (255)  NOT NULL,
    tr_gears INT (2, 0) NOT NULL,
    tr_driveRatio  VARCHAR (255) NOT NULL,
    tr_driveType VARCHAR (255) NOT NULL,
    tr_type VARCHAR (255) NOT NULL
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

-- 240SX - NISSAN

INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
VALUES ('240SX', 1993, 'NISSAN', 'COUPE', 97.4);

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('240SX', 'SE', 'KA24DE', 'KA24 5-speed', '240SX 15s', 8, 22, 2800, 130, 15000.00);

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('240SX', 'Base', 'KA24DE', 'KA24 4-speed Auto', '14 inch Steelies', 8.6, 20, 2900, 120, 13500.00);

insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('KA24DE', 4, 'INLINE', 'GASOLINE', 2.4, 155, 160, 6900);

INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('KA24 5-speed', 5, '3.692', 'RWD', 'MANUAL');

INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('KA24 4-speed Auto', 4, '3.916', 'RWD', 'AUTOMATIC');

INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('240SX 15s', 15, '7 Spoke Aluminum', 205);

INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('14 inch Steelies', 14, 'Steel', 195);

INSERT INTO manufacturer(m_make, m_nationOfOrigin)
VALUES ('NISSAN', 'JAPAN');

insert into engine_Transmission(e_id, tr_id)   
VALUES ('KA24DE', 'KA24 5-speed');
VALUES ('KA24DE', 'KA24 4-speed Auto');

INSERT INTO color(c_id, c_finish, c_color) VALUES ('Hot Red', 'METALLIC', 'RED');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Midnight Blue', 'METALLIC', 'BLUE');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Champagne', 'METALLIC', 'BEIGE');


INSERT INTO color_Trim(c_id, t_id) VALUES ('Hot Red', '240SX-SE');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Midnight Blue', '240SX-SE');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Champagne', '240SX-SE');

-- 2007 Dodge Charger
INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
VALUES ('Charger', 2007, 'DODGE', 'SEDAN', 120.2);

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('Charger', 'SXT', 'EGG V6', '42RLE Automatic', 'Dodge 18 inch 5 Spokes', 7.2, 19, 3700, 130, 25000.00); 

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)     
VALUES ('Charger', 'R/T', '5.7L HEMI V8', 'W5A580', 'Dodge 18 inch 5 Spokes', 5.3, 15, 4000, 145, 30000.00);

INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('Charger', 'SRT8', '5.7L HEMI V8', 'W5A580', 'Dodge 18 inch 5 Spokes', 4.7, 14, 4200, 155, 40000.00);

insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('EGG V6', 6, 'V', 'GASOLINE', 3.5, 250, 250, 6500);

insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)  
VALUES ('5.7L HEMI V8', 8, 'V', 'GASOLINE', 5.7, 340, 390, 6000);

Insert into engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)  
VALUES ('5.7L HEMI V8', 8, 'V', 'GASOLINE', 5.7, 340, 390, 6000);

INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('42RLE Automatic', 4, '3.91', 'RWD', 'AUTOMATIC');

INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('W5A580', 5, '3.07', 'RWD', 'AUTOMATIC');

INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('Dodge 18 inch 5 Spokes', 18, '5 Spoke Aluminum', 245);

INSERT INTO manufacturer(m_make, m_nationOfOrigin)
VALUES ('DODGE', 'USA');    

insert into engine_Transmission(e_id, tr_id)   
VALUES ('EGG V6', '42RLE Automatic');
VALUES ('5.7L HEMI V8', 'W5A580');

INSERT INTO color(c_id, c_finish, c_color) VALUES ('Bright Silver', 'METALLIC', 'WHITE');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Brilliant Black', 'PEARL', 'BLACK');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Inferno Red', 'METALLIC', 'RED');   

INSERT INTO color_Trim(c_id, t_id) VALUES ('Bright Silver', 'Charger-SXT');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Brilliant Black', 'Charger-SXT');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Inferno Red', 'Charger-R/T');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Bright Silver', 'Charger-R/T');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Brilliant Black', 'Charger-R/T');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Inferno Red', 'Charger-SRT8');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Bright Silver', 'Charger-SRT8');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Brilliant Black', 'Charger-SRT8');

-- 2014 BMW X5
INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
VALUES ('X5', 2014, 'BMW', 'SUV', 115.5);
INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('X5', 'xDrive35i', 'N55 I6', 'ZF 8HP', 'BMW 19 inch Double Spoke', 6.5, 20, 4600, 130, 55000.00);  
insert into trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('X5', 'xDrive50i', 'N63 V8', 'ZF 8HP', 'BMW 20 inch M Double Spoke', 4.7, 17, 4900, 155, 70000.00);
insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('N55 I6', 6, 'INLINE', 'GASOLINE', 3.0, 300, 300, 7000);  
insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('N63 V8', 8, 'V', 'GASOLINE', 4.4, 445, 480, 6500);  
INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('ZF 8HP', 8, '2.93', 'AWD', 'AUTOMATIC');  
INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)  
VALUES ('BMW 19 inch Double Spoke', 19, 'Double Spoke Aluminum', 255);  
INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('BMW 20 inch M Double Spoke', 20, 'M Double Spoke Aluminum', 275);
INSERT INTO manufacturer(m_make, m_nationOfOrigin)
VALUES ('BMW', 'GERMANY');
insert into engine_Transmission(e_id, tr_id)   
VALUES ('N55 I6', 'ZF 8HP');    
VALUES ('N63 V8', 'ZF 8HP');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Alpine White', 'SOLID', 'WHITE');
INSERT INTO color_trim(c_id, t_id) VALUES ('Alpine White', 'X5-xDrive35i');
INSERT INTO color_trim(c_id, t_id) VALUES ('Alpine White', 'X5-xDrive50i');




-- 2023 Toyota Prius
INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
VALUES ('Prius', 2023, 'TOYOTA', 'HATCHBACK', 108.3);
INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('Prius', 'LE', 'M20A-FXS', 'Toyota E-CVT', 'Toyota 17 inch Alloys', 7.0, 53, 3100, 112, 25000.00);
INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('Prius', 'PRIME', 'M20A-FXS PHEV', 'Toyota E-CVT AWD', 'Toyota 20 inch Alloys', 6.4, 50, 3150, 112, 30000.00);
insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('M20A-FXS', 4, 'INLINE', 'HYBRID', 2.0, 193, 155, 6000);
insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('M20A-FXS PHEV', 4, 'INLINE', 'HYBRID', 2.0, 220, 193, 6000);
INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('Toyota E-CVT', 1, 'N/A', 'FWD', 'AUTOMATIC');
INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('Toyota E-CVT AWD', 1, 'N/A', 'AWD', 'AUTOMATIC');
INSERT INTO wheel(w_id, w_diameter, w_rim, w_size) 
VALUES ('Toyota 17 inch Alloys', 17, 'Alloy', 215);
INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('Toyota 20 inch Alloys', 20, 'Alloy', 235);
INSERT INTO manufacturer(m_make, m_nationOfOrigin)  
VALUES ('TOYOTA', 'JAPAN');
insert into engine_Transmission(e_id, tr_id)   
VALUES ('M20A-FXS', 'Toyota E-CVT');    
VALUES ('M20A-FXS PHEV', 'Toyota E-CVT AWD');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Wind Chill Pearl', 'PEARL', 'WHITE');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Karashi', 'METALLIC', 'YELLOW');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Wind Chill Pearl', 'Prius-LE');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Wind Chill Pearl', 'Prius-PRIME');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Karashi', 'Prius-PRIME');  

-- 2006 Volvo V70
INSERT INTO car(c_model, c_year, c_make, c_bodyType, c_wheelBase)
VALUES ('V70', 2006, 'VOLVO', 'WAGON', 108.5);
INSERT INTO trim(t_model, t_id, t_engine, t_transmission, t_wheels, t_accel, t_eco, t_weight, t_speed, t_price)
VALUES ('V70', '2.4D', 'D5244T5', 'AW55-51SN', 'Volvo 16 inch Alloys', 8.9, 28, 3500, 130, 28000.00);
insert INTO engine(e_id, e_cylinders, e_layout, e_fuelType, e_displacement, e_horsepower, e_torque, e_redline)
VALUES ('D5244T5', 5, 'INLINE', 'DIESEL', 2.4, 163, 250, 5000);
INSERT INTO transmission(tr_id, tr_gears, tr_driveRatio, tr_driveType, tr_type)
VALUES ('AW55-51SN', 5, '3.91', 'FWD', 'AUTOMATIC');
INSERT INTO wheel(w_id, w_diameter, w_rim, w_size)
VALUES ('Volvo 16 inch Alloys', 16, 'Alloy', 205);
INSERT INTO manufacturer(m_make, m_nationOfOrigin)  
VALUES ('VOLVO', 'SWEDEN');
insert into engine_Transmission(e_id, tr_id)    
VALUES ('D5244T5', 'AW55-51SN');
INSERT INTO color(c_id, c_finish, c_color) VALUES ('Ice White', 'SOLID', 'WHITE');
INSERT INTO color_Trim(c_id, t_id) VALUES ('Ice White', 'V70-2.4D');
