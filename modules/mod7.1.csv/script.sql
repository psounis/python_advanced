SELECT 'Code','Name','Continent','Region','SurfaceArea','IndepYear','Population','LifeExpectancy','GNP','GNPOld','LocalName','GovernmentForm','HeadOfState','Capital','Code2'
UNION
SELECT * 
FROM country
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\countries.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

