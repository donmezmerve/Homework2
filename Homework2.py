# Get number of points from user
n = int(input ("Please define n="))

# Get datapoints from user
datapoints = []
for i in range(1, n+1):
    raw= input("Please enter " + str(i) + "th coordinates ").split( "," )
    x = float(raw[0])
    y = float(raw[1])
    point=(x,y)
    datapoints.append( point )
print("Datapoints:", datapoints)


# Calculate center of mass
sumx = 0
sumy = 0
for point in datapoints:
    sumx += point[0]
    sumy += point[1]
center_of_mass = (sumx/n, sumy/n)
print("Center of mass:", center_of_mass)


# Calculate distances
distances = []
for point, idx in zip(datapoints, range(n)):
    dist = (center_of_mass[0]-point[0])**2 + (center_of_mass[1]-point[1])**2
    dist = dist**.5
    distances.append( (dist, idx) )
print("Distances are:", distances)

# Find closest point
closest_point = distances[0]
for dist, idx in distances:
    if dist < closest_point[0]:
        closest_point = (dist, idx)
print("Closest point is:", datapoints[closest_point[1]], "with distance:", closest_point[0])





# Find furthest point
furthest_point = distances[0]
for dist, idx in distances:
    if dist >furthest_point[0]:
        furthest_point = (dist, idx)
print("Furthest point is:", datapoints[furthest_point[1]], "with distance:", furthest_point[0])
