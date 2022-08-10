-- creates table unique_id with the following cols:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- execution shouldn't fail if table exists
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
