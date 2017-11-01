
CREATE DATABASE IF NOT EXISTS mskorokhod;
USE mskorokhod;
-- Create posts_sample_external table

DROP TABLE IF EXISTS `posts_sample_external`;
CREATE EXTERNAL TABLE IF NOT EXISTS `posts_sample_external`(
  `id` int,
  `post_type_id` tinyint,
  `date` string,
  `owner_user_id` int,
  `parent_id` int,
  `score` int,
  `favorite_count` int,
  `tags` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
  "input.regex" = '^<row.*?(?=.*\\bId=\"(\\d+)\")(?=.*\\bPostTypeId=\"(\\d+)\")(?=.*\\bCreationDate=\"([^"]*)\")(?=.*\\bOwnerUserId=\"(\\d+)\")?(?=.*\\bParentId=\"(\\d+)\")?(?=.*\\bScore=\"(-?\\d+)\")(?=.*\\bFavoriteCount=\"(\\d+)\")?(?=.*\\bTags=\"([^"]*)\")?.*',
  "input.regex.case.insensitive" = 'true'
)
STORED AS TEXTFILE
LOCATION
  '/data/stackexchange100/posts'
;
-- Create managed table and fill data

DROP TABLE IF EXISTS `posts_sample`;
CREATE TABLE IF NOT EXISTS `posts_sample`(
  `id` int,
  `post_type_id` tinyint,
  `date` string,
  `owner_user_id` int,
  `parent_id` int,
  `score` int,
  `favorite_count` int,
  `tags` array <string>
)
PARTITIONED BY ( 
  `year` string, 
  `month` string
)
CLUSTERED BY ( 
  `date`
) 
SORTED BY ( 
  id ASC
) 
INTO 8 BUCKETS
STORED AS TEXTFILE
LOCATION
  '/user/jovyan/task1'
;

SET hive.exec.dynamic.partition=true;  
SET hive.exec.dynamic.partition.mode=nonstrict;

INSERT OVERWRITE TABLE `posts_sample`
PARTITION (`year`, `month`)
SELECT
  `id`,
  `post_type_id`,
  `date`,
  `owner_user_id`,
  `parent_id`,
  `score`,
  `favorite_count`,
  split(regexp_replace(`tags`, '(&lt\;|&gt\;$)', ''), '&gt\;') AS `tags`,
  regexp_extract(`date`, '^(\\d{4})', 1) AS `year`,
  regexp_extract(`date`, '^(\\d{4}-\\d{2})', 1) AS `month`
FROM `posts_sample_external`
;
SELECT * FROM (
    SELECT year, month, count(1)
    FROM posts_sample
    GROUP BY year, month
    LIMIT 3
) AS SubQ
SORT BY month DESC
LIMIT 1
;