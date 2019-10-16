
#How many trees per house average of about 4 trees per house

#How many houses per block

#How many blocks per square mile

#How many square miles in Sacramento

# Google states that Sacramento is approx 97 sq mi
# and approx 19.1% of Sac is covered by trees
coverage = .191 * 97
# Multiple sources state 290 trees per acre and 640 acres = 1 sq mi
tree_per_mi = 290 * 640
print (coverage * tree_per_mi)
