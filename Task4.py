#Given two sets: one of students who play football, another who play cricket.

#Display students who play both, only one, or none.


all_students = {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"}

football_players = {"Alice", "Bob", "Eve"}
cricket_players = {"Bob", "Charlie", "Frank"}


both = football_players & cricket_players


only_football = football_players - cricket_players
only_cricket = cricket_players - football_players
only_one = only_football | only_cricket

none = all_students - (football_players | cricket_players)

print("Students who play both football and cricket:", both)
print("Students who play only one of the two:", only_one)
print("Students who play neither football nor cricket:", none)