

distance_matrix = [
        [0,5,6,4],
        [5,0,3,2],
        [6,3,0,2],
        [4,2,2,0]
        ]

species = ["B", "M", "H", "O"]

def create_adjusted_matrix(M):
    adjusted_matrix = [[0 for i in range(len(M[0]))] for j in range(len(M))]
    n = len(M)
    for i in range(len(adjusted_matrix)):
        for j in range(len(adjusted_matrix[0])):
            row = M[i]
            col = [M[x][j] for x in range(len(row))]
            if (i == j):
                continue
            adjusted_matrix[i][j] = (n-2) * M[i][j] - sum(row) - sum(col)

    return adjusted_matrix

def find_minimal_element(M):
    min_val = min([min(row) for row in M])
    for row in range(len(M)):
        for col in range(len(M[0])):
            if M[row][col] == min_val:
                return (row, col)

def remove_minimal_element(M_star, M):
    i,j = find_minimal_element(M_star)
    n= len(M)
    delta = (sum(M[i]) - sum([M[x][j] for x in range(len(M[0]))])) / (n-2)

    ll_i = 0.5 * (M[i][j] + delta)
    ll_j = 0.5 * (M[i][j] - delta)
    new_M = [[0 for i in range(len(M[0]) - 1)] for j in range(len(M) - 1)]

    for i2 in range(len(new_M)):
        for j2 in range(len(new_M[0])):
            if i2==0:
                distance = (M[i][j2] + M[j][j2] - M[i][j])/2
            elif j2 == 0:
                distance = (M[i][i2] + M[j][i2] - M[i][j])/2
            else:
                distance = M[i2][j2]
            new_M[i2][j2] = distance

    return (i, j, ll_i, ll_j, new_M)

def neighbour_joining(M):
    while len(M) > 1:
        for row in M:
            print(row)

        M_star = create_adjusted_matrix(M)
        i,j,ll_i,ll_j,M = remove_minimal_element(M_star, M)
        print(i, j, ll_i, ll_j)

        print()

neighbour_joining(distance_matrix)


