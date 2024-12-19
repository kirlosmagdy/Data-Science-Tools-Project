-- 1. Calculate the average price per room for each property type and rank property types within each state
SELECT 
    State,
    Property_Type,
    ROUND(AVG(Price / Rooms), 2) AS Avg_Price_Per_Room,
    RANK() OVER (PARTITION BY State ORDER BY AVG(Price / Rooms) DESC) AS Rank_Per_State
FROM 
    final__1_
WHERE 
    Rooms > 0 AND Price > 0
GROUP BY 
    State, Property_Type;






-- 2. Find the total area covered and cumulative percentage of area for each city
SELECT 
    City,
    SUM(Area) AS Total_Area,
    ROUND(100.0 * SUM(Area) / SUM(SUM(Area)) OVER (), 2) AS Cumulative_Percentage_Area
FROM 
    final__1_
WHERE 
    Area > 0
GROUP BY 
    City
ORDER BY 
    Total_Area DESC;





-- 3. Rank properties globally by price per square unit of area and assign a dense rank within each state
SELECT 
    State,
    Price,
    Area,
    ROUND(Price / Area, 2) AS Price_Per_Square_Unit,
    RANK() OVER (ORDER BY Price / Area DESC) AS Global_Price_Rank,
    DENSE_RANK() OVER (PARTITION BY State ORDER BY Price / Area DESC) AS State_Price_Rank
FROM 
    final__1_
WHERE 
    Area > 0 AND Price > 0;








-- 4. Find the total number of units and the percentage contribution of each property type in each state
SELECT 
    State,
    Property_Type,
    COUNT(*) AS Total_Units,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY State), 2) AS Percentage_Contribution
FROM 
    final__1_
GROUP BY 
    State, Property_Type;





-- 5. Rank building statuses within each state based on the number of units
SELECT 
    State,
    Building_Status,
    COUNT(*) AS Total_Units,
    RANK() OVER (PARTITION BY State ORDER BY COUNT(*) DESC) AS Status_Rank
FROM 
    final__1_
GROUP BY 
    State, Building_Status;






