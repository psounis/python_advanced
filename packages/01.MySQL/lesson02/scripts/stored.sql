DROP PROCEDURE IF EXISTS country_cities;

DELIMITER $$
CREATE PROCEDURE country_cities(
	IN in_country_name CHAR(52)
) 
BEGIN
	SELECT ct.name, ct.district, ct.population
    FROM country cn JOIN city ct
		ON cn.code = ct.countrycode
    WHERE cn.name = in_country_name;    
    
END$$
DELIMITER ;

CALL country_cities('Greece'); 

