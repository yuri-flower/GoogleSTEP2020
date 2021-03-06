def one_or_opt(tour, dist):
    N = len(tour)
    # is_improved = False

    while True:
        count = 0
        for i in range(N):
            i0 = i
            i1 = (i + 1) % N
            i2 = (i + 2) % N
            for j in range(N):
                j0 = j
                j1 = (j + 1) % N
                if j0 not in {i0, i1}:
                    l1 = dist[tour[i0]][tour[i1]]
                    l2 = dist[tour[i1]][tour[i2]]
                    l3 = dist[tour[j0]][tour[j1]]
                    l4 = dist[tour[j0]][tour[i1]]
                    l5 = dist[tour[j1]][tour[i1]]
                    l6 = dist[tour[i0]][tour[i2]]
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        city = tour.pop(i1)
                        if i1 < j1:
                            tour.insert(j0, city)
                        else:
                            tour.insert(j1, city)
                        count += 1
        if count == 0:
            break
        # else:
        #     is_improved = True
    return tour
    # return tour, is_improved