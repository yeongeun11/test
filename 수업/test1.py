# n = 5

#     *
#    ***
#   *****
#  *******
# *********

row_count = 5
blank_count = row_count - 1
star_count = 1


for _ in range(row_count):
    for _ in range(blank_count):
        print(" ", end = "")

for _ in range(star_count):
    print("*", end = "")       
  