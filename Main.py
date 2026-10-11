name = input("Member name:")
club = input("Club name:")

member_num = 8
points = 9.5
is_active = True
print("Member_name:",member_num,"->type:",type(member_num))
print("Points:",points,"->type:",type(points))
print("Is_Active:",is_active,"->type:",type(is_active))

badge_code = name[0:3] + club[-1:] + str(member_num)
print("Badge_code",badge_code)

print("=================== CLUB BADGE =================")
print("Member:" + name)
print("Club:" + club)
print("Badge_code:" + badge_code)
print("Points:" + str(points) +  "| Active:" + str(is_active))