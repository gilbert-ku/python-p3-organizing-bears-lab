select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM bears
    WHERE alive = 1
        AND age > 5;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT DISTINCT
        color
    FROM bears
    WHERE color = 'Brown' OR color = 'Black';
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
        COUNT(*)
    FROM bears
    WHERE name LIKE 'M%';
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""