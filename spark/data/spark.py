from pyspark import SparkContext
import itertools


DEBUG = False


def test(rdd):
    for i in range(10):
        print('----------------------------------------------------------')
    output = rdd.collect()
    if len(output) > 0:
        for row in output:
            print(row)
    else:
        print('no data...')
    for i in range(10):
        print('----------------------------------------------------------')


sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/test.log", 2)     # each worker loads a piece of the data file

# tab separated log file => (user_id, product_id)
user_to_prod = data.map(lambda line: tuple(line.split("\t")))

if DEBUG:
    test(user_to_prod)

user_to_prod_distinct = user_to_prod.distinct()

if DEBUG:
    test(user_to_prod_distinct)

# [user_id, product_id] => [user_id, [product_id_1, product_id_2, ...]]
user_to_prod_list = user_to_prod_distinct.groupByKey()

if DEBUG:
    test(user_to_prod_list)

# [user_id, [product_id_1, product_id_2, ...]] => every possible unique ((product_id_X, product_id_Y), 1)
# we don't need the user anymore so we replace it with 1 click
# because we already aggregated the product id list for each user, we know each "1" represents
# a product pair from a unique user
user_to_prod_pairs = user_to_prod_list.flatMap(
    lambda row: tuple(map(
        # the sorted() is important here to make sure the pair (3, 2) always comes out (2, 3)
        lambda pair: (tuple(sorted(pair)), 1),
        tuple(itertools.combinations(row[1], 2))
    ))
)

if DEBUG:
    test(user_to_prod_pairs)

# ((product_id_X, product_id_Y), 1) => ((product_id_X, product_id_Y), total_clicks)
prod_pair_to_clicks = user_to_prod_pairs.reduceByKey(lambda x, y: int(x) + int(y))

if DEBUG:
    test(prod_pair_to_clicks)

# filter out pairs with fewer than 3 clicks
final_counts = prod_pair_to_clicks.filter(lambda row: row[1] >= 3)

# key value pairs of the form ((product_id_1, product_id_2), int holding unique clicks)
output = final_counts.collect()




# feed output data into SQL here




sc.stop()
