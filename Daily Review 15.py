capitals = {
    "America": "Washington D.C.",
    "Spain": "Madrid",
}

travelLog = {
    "America": ["Washington D.C.", "New York", "Philadelphia"],
    "Spain": ["Barcelona", "Madrid"]
}

print(travelLog["America"][1])

nestedList = ["A", "B", ["C", "D"]]
print(nestedList[0], nestedList[1], nestedList[2][0], nestedList[2][1])

travelLog2 = {
    "Spain": {
        "times visited": 6,
        "cities visited": ["Barcelona", "Madrid"]
    },
    "America": {
        "times visited": 8,
        "cities visited": ["Washington D.C.", "New York", "Philadelphia"]
    },
}

print(travelLog2["Spain"]["cities visited"][0], travelLog2["Spain"]["cities visited"][1])