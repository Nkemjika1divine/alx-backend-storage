-- Ranks country origin of bands 
-- Ordered by non unique sum
SELECT
	origin,
	SUM(fans) AS nb_fans
FROM
	metal_bands
WHERE
	origin IS NOT NULL
GROUP BY
	origin
ORDER BY
	nb_fans DESC;
