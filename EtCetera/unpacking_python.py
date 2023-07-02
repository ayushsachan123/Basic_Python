def total(galleons, sickles, knuts):
    return (galleons *17 + sickles)*29 + knuts

coins = [100,50,25]
# we use * to unpack list
print(total(*coins), "knuts")

# we use ** to unpack dictonery
coins1 = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins1), "knuts")