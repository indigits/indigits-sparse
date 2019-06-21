from spx.num.rational import *
#(a, b) = (0, 1)
#(c, d) = (1, 0)

(a, b) = (1, 0)
(c, d) = (0, -1)
level = 4
dtype='int32'
for level in range(1, 5):
    [numerators , denominators] = stern_brocot(a, b, c, d, level)
    #print(numerators)
    #print (denominators)
    print_num_den_arrays(numerators, denominators)
    print()
    if not validate_stern_brocot(a, b, c, d, numerators, denominators):
        print('Invalid construction')

