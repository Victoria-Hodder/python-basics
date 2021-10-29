
-- Joining Students and Grades tables using WHERE
select s.name, s.marks, g.grade
from students s, grades g
where s.marks between g.min_mark and g.max_mark
order by g.grade desc;

-- Idea for join with JOIN:  'join abc on x >=  min and x  <= max'
