-- creates table id_not_null with the following columns:
-- id INT with the default value 1
-- name VARCHAR(256)
-- execution shouldn't fail if table exists
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);
