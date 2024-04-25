-- Check is a constraint which ensures that the only
-- Data that will be entered will be the ones specified
CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country VARCHAR(2) NOT NULL DEFAULT 'US',
	CHECK (country IN ('US', 'CO', 'TN'))
);
