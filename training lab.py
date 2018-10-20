w = float(input())
h = float(input())

w_to_cm = w*100
h_to_cm = h*100

rows = int(w_to_cm/120)

h_to_cm -= 100
desks_in_row = h_to_cm//70

all_desks = rows*desks_in_row-3
print(all_desks)

