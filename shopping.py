# ******************************************************************************************
# KnapSack Problem
# Author: Eric Armstrong
# Date: 01/24/19
# Course: CS 325
# Description: Program reads text file of lines of integers, and writes them to
#              text file sorted by line
# Citations: Office Hours
#            Algorithms by: Dasgupta, Papdimitriou, and Vazirani
#            StackExchange
# ******************************************************************************************


# ******************************************************************************************
# Procedure: Shop Items
# Description: Place values into results array based on optimized solution for capacity
#               When value changes, new item is returned to sack
# ******************************************************************************************
def shop_items(k, n, bag, items):
    for i in range(n, 0, -1):
        if k[i][bag] != k[i - 1][bag]:
            yield i
            bag -= items[i - 1][1]


# ******************************************************************************************
# Procedure: Shop
# Description: Algorithm searches for optimum value to place in bag. For every value we
#               Decide if we should keep what is in the bag or replace what we have in bag
# ******************************************************************************************
def shop(items, family):
    bag = max(family)
    n = len(items)
    # Create 2d array to hold optimum value for each item as n gets larger
    k = [[0 for x in range(bag + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(bag + 1):
            # initialize 0,w and i,0 to 0 for all values w and i
            if i == 0 or w == 0:
                k[i][w] = 0
            # if item weigh less than items in bag decide to keep what is in bag or add new item to difference of
            # bag and reduced capacity
            elif items[i - 1][1] <= w:
                k[i][w] = max(items[i - 1][0] + k[i - 1][w - items[i - 1][1]], k[i - 1][w])
            else:
                k[i][w] = k[i - 1][w]
    total = 0
    results = []

    # find total an items needed for each bag capacity
    for val in family:
        picked = list(shop_items(k, n, val, items))
        picked.reverse()
        results.append(picked)
        for x in picked:
            total += items[x - 1][0]
    results.append(total)

    return results


# ******************************************************************************************
# Procedure: Shopping
# Description: Reads lines from shopping.txt, and determines optimal solution for values given
#               writes items to results.txt
# ******************************************************************************************
def shopping(input_file, output_file):
    file = open(input_file)
    writefile = open(output_file, 'w')

    test = int(file.readline().strip())

    for case in range(test):
        caseItems = int(file.readline().strip())

        items = []
        family = []

        for stock in range(caseItems):
            items.append(list(int(x) for x in file.readline().strip().split()))

        people = int(file.readline().strip())

        for person in range(people):
            for x in file.readline().strip().split():
                family.append(int(x))
        results = shop(items, family)
        writefile.write('Test Case {}'.format(case + 1))
        writefile.write('\n')
        writefile.write('Total Price {}'.format(results[len(family)]))
        writefile.write('\n')
        writefile.write('Member Items:')
        writefile.write('\n')

        for person in range(people):
            writefile.write('{}: {}'.format(person, results[person]))
            writefile.write('\n')
    writefile.close()


shopping('shopping.txt', 'results.txt')
