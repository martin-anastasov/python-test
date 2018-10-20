N_playground_meters = float(input())
W_tile_meters = float(input())
L_tile_meters = float(input())
M_bench_width_meters = float(input())
O_bench_length_meters = float(input())
tile_install_time = 0.2

N_area = N_playground_meters * N_playground_meters
bench_area = M_bench_width_meters * O_bench_length_meters
area = N_area - bench_area
tile_area = W_tile_meters * L_tile_meters

required_tiles = area/tile_area

print("Required tiles = " + str(required_tiles))
print("Required time = " + str(required_tiles*tile_install_time))
print(area)


