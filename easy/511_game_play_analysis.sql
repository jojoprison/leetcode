-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | player_id    | int     |
-- | device_id    | int     |
-- | event_date   | date    |
-- | games_played | int     |
-- +--------------+---------+
-- (player_id, event_date) is the primary key (combination of columns with unique values)
-- of this table.
--
-- This table shows the activity of players of some games.
--
-- Each row is a record of a player who logged in and played
-- a number of games (possibly 0) before logging out on someday using some device.


-- pre-requirements
Create table If Not Exists Activity
(
    player_id    int,
    device_id    int,
    event_date   date,
    games_played int
);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played)
values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played)
values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played)
values ('3', '4', '2018-07-03', '5');


-- 1.: СРЕДНИЙ | группируем по player_id, берем самую раннюю дату через MIN
SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id;

-- 2: БЫСТРЫЙ | GROUP BY заменим оконной функцией по event_date + FIRST_VALUE
SELECT DISTINCT player_id,
       FIRST_VALUE(event_date) OVER
           (PARTITION BY player_id ORDER BY event_date) as first_login
FROM Activity;

-- 3: МЕДЛЕННЫЙ | DISTINCT ON вернет первую запись для player_id
-- из отсортированных по event_date
SELECT DISTINCT ON (player_id) player_id, event_date AS first_login
FROM activity
ORDER BY player_id, event_date;
