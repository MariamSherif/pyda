
SELECT
    age,
    sum(questions),
    sum(answers)
FROM (
    SELECT
        owner_user_id,
        if (post_type_id = 1, 1, 0) as questions,
        if (post_type_id = 2, 1, 0) as answers
    FROM posts
    WHERE
        owner_user_id IS NOT NULL
) AS SubQ
INNER JOIN users ON
    users.id = SubQ.owner_user_id
GROUP BY
    age
ORDER BY
    age
;