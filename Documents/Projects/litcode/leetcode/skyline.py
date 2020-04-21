def getSkyline(buildings):
    skyline = []
        
    if len(buildings) == 1:
        left = buildings[0][0]
        right = buildings[0][1]
        height = buildings[0][2]
        
        skyline.append([left, height])
        skyline.append([right, 0])
        
        return skyline
    
    for i, building in enumerate(buildings):
        left = building[0]
        right = building[1]
        height = building[2]

        if i == 0:
            skyline.append([left, height])
            continue

        prev_left = buildings[i-1][0]
        prev_right = buildings[i-1][1]
        prev_height = buildings[i-1][2]

        # if buildings are just touching
        if height == prev_height:
            continue

        # if there's a gap between buildings
        if left > prev_right:
            skyline.append([prev_right, 0])

        # if buildings overlap
        if left < prev_right and height < prev_height:
            skyline.append([prev_right, height])
        else:
            skyline.append([left, height])

        if i == len(buildings)-1:
            skyline.append([right, 0])

    return skyline

if __name__ == '__main__':
    B = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # B = [[2,9,10],[3,7,15],[5,12,12]]
    

    print("============")
    print(getSkyline(B))