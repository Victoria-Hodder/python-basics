
-- Joining Students and Grades tables using WHERE
select s.name, g.grade, s.marks
from students s, grades g
where s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name;

-- Idea for join with JOIN:  'join abc on x >=  min and x  <= max'

-- Playing with CASE
select s.name, g.grade, s.marks,
case
    when g.grade < 8 then 'The grade is less than 8'
    else 'The grade is equal to or more than 8'
end
from students s, grades g
where s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name;
