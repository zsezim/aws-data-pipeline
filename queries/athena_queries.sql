-- Top 10 most popular routes
SELECT route, COUNT(*) AS flight_count
FROM flights
GROUP BY route
ORDER BY flight_count DESC
LIMIT 10;

-- Flights departing from ORD on Christmas morning
SELECT airline, origin_airport, destination_airport
FROM flights
WHERE origin_airport = 'ORD'
AND departure_time BETWEEN 800 AND 1200
AND month = 12 AND day = 25;