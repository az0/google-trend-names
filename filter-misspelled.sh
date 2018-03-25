grep -vP '[\x80-\xFF]' people-misspelled.txt  | grep -P '^[A-Z][a-z]{3,}' | sort | uniq > people-misspelled-filtered.txt
wc -l people-misspelled-filtered.txt
