use pyworld;

DROP TABLE IF EXISTS dates;

CREATE TABLE dates (
	vdate DATE,
    vtime TIME,
    vdatetime DATETIME,
    vtimestamp TIMESTAMP DEFAULT NOW()
);

INSERT INTO dates (vdate, vtime, vdatetime)
VALUES(CURRENT_DATE(), CURRENT_TIME(), NOW());

SELECT * 
FROM dates;

    