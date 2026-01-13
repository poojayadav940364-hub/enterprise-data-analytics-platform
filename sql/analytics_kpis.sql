-- Analytics KPIs built on cleaned user data
-- Snowflake-compatible SQL

CREATE OR REPLACE TABLE ANALYTICS.USER_KPIS AS
SELECT
    id AS user_id,
    username,
    email,
    name_length,
    username_length,
    LENGTH(email) AS email_length,
    CURRENT_DATE AS snapshot_date
FROM STAGING.CLEAN_USERS;
