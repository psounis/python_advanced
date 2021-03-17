DROP TABLE IF EXISTS images;

CREATE TABLE images (
	image_id INT PRIMARY KEY AUTO_INCREMENT,
    image BLOB,
    descr VARCHAR(100)
);

select * from images;
