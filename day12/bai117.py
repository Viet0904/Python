##################### Scope ###################
# Scope chỉ có trong def(function) không có trong Block Scope(if else for)
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies inside function: {enemies}")

#Local Scope 