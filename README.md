# Subway Modeling Exercise

# Questions
1. Can we assume that any subway system presented under Challenge 2 will have total time coverage? How are mixed graphs handled? (My solution assumes total coverage)
2. What is the desired behavior in the event that the two stations are unreachable? (I do not treat this as an error, but instead return an empty path)
3. Are all train lines a sequence of nodes with a maximum of two edges? (My solution assumes so)
4. Are circular lines allowed (e.g., Station A -> Station B -> Station C -> Station A)? (My solution assumes not)
