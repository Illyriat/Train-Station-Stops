stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverly")

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print(stops)

#5. Remove "Livingston" from the list using its name
stops.remove("Linlithgow")

#6. Delete "Cumbernauld" from the list by index
del stops[1]

#7. Print the number of stops there are in the list
print(stops)
num_stops = len(stops)
print(num_stops)

#8. Sort the list alphabetically
stops.sort()
print(stops)

#9. Reverse the positions of the stops in the list
# Using the slicing method
print(stops[::-1])

#10 Print out all the stops using a for loop
for stop in stops:
    print(f"This stop is {stop}")