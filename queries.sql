DROP VIEW IF EXISTS bestfuelEco;

CREATE VIEW bestfuelEco (car, trim, economy) AS
SELECT c_model as car, t_id as trim, MAX(t_eco) AS economy
FROM car, trim
WHERE c_model = t_model
GROUP BY c_model;


-- 1. All cars made after year 2000 (basic)
SELECT c_model, c_year, c_make, c_bodyType
FROM car
WHERE c_year > 2000;

-- 2. All gasoline engines with horsepower greater than 300 (basic)
SELECT e_id, e_horsepower, e_fuelType
FROM engine
WHERE e_fuelType = 'GASOLINE'
    AND e_horsepower > 300;

-- 3. Show trim with a computed power-to-weight ratio (horsepower / weight) (join 2 tables + calculations)
SELECT t.t_model, t.t_id, e.e_horsepower, t.t_weight, e.e_horsepower / (t.t_weight * 0.45359237) AS hp_per_kg -- lbs to kg conversion
FROM trim t
JOIN engine e ON t.t_engine = e.e_id
ORDER BY hp_per_kg DESC;

-- 4. List all cars along with their manufacturer's nation of origin (join 2 tables)
SELECT c.c_make, c.c_model, c.c_year, m.m_nationOfOrigin
FROM car c
JOIN manufacturer m ON c.c_make = m.m_make;

-- 5. List manufacturers and how many distinct models they have (basic + aggregation)
SELECT m.m_make, COUNT(DISTINCT c.c_model) AS num_models
FROM manufacturer m
JOIN car c ON m.m_make = c.c_make
GROUP BY m.m_make;

-- 6. All models that have either V6 or V8 engines (basic + grouping)
SELECT t_model
FROM trim t
JOIN engine e ON t.t_engine = e.e_id
WHERE e.e_cylinders IN (6, 8)
GROUP BY t_model
HAVING COUNT(DISTINCT e.e_cylinders) = 2;

-- 7. SELECT avg price of manufacturer using VIEW FullTrimOverview (aggregation + view)
SELECT c_make, COUNT(*) AS num_trims, AVG(t_price) AS avg_price
FROM FullTrimOverview
GROUP BY c_make;

-- 8. Cars with at least one trim minimum 300 hp (subquery)
SELECT DISTINCT c.c_make, c.c_model, c.c_year
FROM car c
WHERE EXISTS (
    SELECT 1
    FROM trim t
    JOIN engine e ON t.t_engine = e.e_id
    WHERE t.t_model = c.c_model
      AND e.e_horsepower > 300
);

-- 9. SELECT trims that are cheapest for their model (subquery)
SELECT t1.t_model, t1.t_id, t1.t_price
FROM trim t1
WHERE t1.t_price = (
    SELECT MIN(t2.t_price)
    FROM trim t2
    WHERE t2.t_model = t1.t_model
);

-- 10. Pricing stats per model (aggregation + grouping)
SELECT t_model, AVG(t_price) AS avg_price, MIN(t_price) AS min_price, MAX(t_price) AS max_price
FROM trim
GROUP BY t_model;

-- 11. num of trims per car model (aggregation + grouping)
SELECT c.c_make, c.c_model, COUNT(*) AS num_trims
FROM car c
JOIN trim t ON c.c_model = t.t_model
GROUP BY c.c_make
ORDER BY num_trims DESC ;

-- 12. Drivetrain types and their average fuel economy (aggregation + HAVING)
SELECT tr.tr_driveType, AVG(t.t_eco) AS avg_eco
FROM trim t
JOIN transmission tr ON t.t_transmission = tr.tr_id
GROUP BY tr.tr_driveType
HAVING AVG(t.t_eco) IS NOT NULL;

-- 13. Nation, body type, horsepower per model (join 3 tables)
SELECT m.m_nationOfOrigin, c.c_make, c.c_model, e.e_horsepower
FROM manufacturer m
JOIN car c ON m.m_make = c.c_make
JOIN trim t ON c.c_model = t.t_model
JOIN engine e ON t.t_engine = e.e_id;

-- 14. Car, trim, color (join 3 tables + ordering)
SELECT c.c_make, c.c_model, t.t_id, col.c_color, col.c_finish
FROM car c
JOIN trim t ON c.c_model = t.t_model
JOIN color_Trim ct ON ct.t_id = t.t_model || '-' || t.t_id -- concatenated model-id for trim
JOIN color col ON col.c_id = ct.c_id
ORDER BY c.c_model, t.t_id, col.c_color;

-- 15. Full trim overview with car, engine, and transmission details (join 4 tables)
SELECT c.c_make, c.c_model, c.c_year, t.t_id AS trim_name, e.e_id AS engine_id, e.e_cylinders, e.e_horsepower, tr.tr_id AS transmission_id, tr.tr_gears, tr.tr_type
FROM car c
JOIN trim t ON c.c_model = t.t_model
JOIN engine e ON t.t_engine = e.e_id
JOIN transmission tr ON t.t_transmission = tr.tr_id;

-- 16. Show all trim models with price per horsepower (calculation + join + ordering)
SELECT t.t_model, t.t_id, t.t_price, e.e_horsepower, t.t_price / e.e_horsepower AS price_per_hp
FROM trim t
JOIN engine e ON t.t_engine = e.e_id
ORDER BY price_per_hp ASC;

-- 17. Trims with at least 300 hp and top speed over 140 mph (join + filtering)
SELECT t.t_model, t.t_id, e.e_horsepower, t.t_speed
FROM trim t
JOIN engine e ON t.t_engine = e.e_id
WHERE e.e_horsepower >= 300
  AND t.t_speed >= 140;

-- 18. Count how many colors a trim has (aggregation + join)
SELECT t.t_model,
       t.t_id,
       COUNT(DISTINCT ct.c_id) AS num_colors
FROM trim t
JOIN color_Trim ct ON ct.t_id = t.t_model || '-' || t.t_id
GROUP BY t.t_model, t.t_id;

-- 19. Average horsepower and torque per # of cylinders (aggregation + grouping)
SELECT e.e_cylinders, AVG(e.e_horsepower) AS avg_hp, AVG(e.e_torque) AS avg_torque
FROM engine e
GROUP BY e.e_cylinders;

-- 20. Find trims with manual transmission (basic)
SELECT t.t_model, t.t_id, t.t_price, tr.tr_type
FROM trim t
JOIN transmission tr ON t.t_transmission = tr.tr_id
WHERE tr.tr_type = 'MANUAL';


-- 21. Find best fuel economy per car model (view)
SELECT *
FROM bestfuelEco
ORDER BY economy DESC;


-- 22. List of cars that have trims with fuel economy over 25 mpg (view + filtering)
SELECT DISTINCT c.c_make, c.c_model, bfe.economy
FROM car c
JOIN bestfuelEco bfe ON c.c_model = bfe.car
WHERE bfe.economy > 25;


-- 23 List number of trims by fuel type
SELECT e.e_fuelType, COUNT(*) AS num_trims
FROM engine e
JOIN trim t ON e.e_id = t.t_engine  
GROUP BY e.e_fuelType;