def profit(info):
     return round(info["sell_price"] * info["inventory"]) - round(info["cost_price"] * info["inventory"])

def count_overlapping(intervals, point):
	count = 0
	for interval in intervals:
		print(interval)
		if count >= interval[0] and count <= interval[1]:
			hasPoint = hasPoint + interval
	return count

def accumulating_list(lst):
    return [sum(lst[:i+1]) for i in range(len(lst))]

def num_of_sublists(lst):
	return sum(isinstance(i, list) for i in lst)

def seven_boom(lst):
    for x in lst:
        if "7" in str(x):
            return "Boom!"
    return "there is no 7 in the list"

def is_pandigital(n):
	pset = set()
	for x in str(n):
		pset.add(int(x))
	return range(0,10) in pset

if __name__ == "__main__":

    test = {
      "cost_price": 378.11,
      "sell_price": 990.00,
      "inventory": 99
    }

    print(is_pandigital(98140723568910)
