# The logic determines validity by checking if the total area of the 
# requested presents is less than or equal to the total area of the region.
def check_regions(file_path):
    # Area of shapes based on '#' count in diagrams 0-5
    shape_areas = [7, 6, 5, 7, 7, 8]
    successful_fits = 0
    
    with open(file_path, 'r') as f:
        for line in f:
            if 'x' in line and ':' in line:
                # Parse dimensions and requirements
                header, counts = line.split(':')
                width, height = map(int, header.split('x'))
                presents = list(map(int, counts.split()))
                
                # Calculate total area required
                total_needed = sum(presents[i] * shape_areas[i] for i in range(6))
                
                # Check against total available grid space
                if total_needed <= (width * height):
                    successful_fits += 1
    return successful_fits

print(check_regions('Day12.txt'))