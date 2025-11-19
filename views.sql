-- Full overview of trims with related car, engine, transmission, and wheel details
DROP VIEW IF EXISTS FullTrimOverview;
CREATE VIEW FullTrimOverview AS
SELECT c.c_make,
       c.c_model,
       c.c_year,
       t.t_id AS trim_name,
       t.t_price,
       t.t_eco,
       e.e_id AS engine_id,
       e.e_cylinders,
       e.e_horsepower,
       tr.tr_id AS transmission_id,
       tr.tr_type,
       w.w_diameter,
       w.w_rim
FROM car c
JOIN trim t ON c.c_model = t.t_model
JOIN engine e ON t.t_engine = e.e_id
JOIN transmission tr ON t.t_transmission = tr.tr_id
JOIN wheel w ON t.t_wheels = w.w_id;