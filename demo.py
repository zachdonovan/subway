from subway import SubwaySystem

s=SubwaySystem()

print("adding some lines")
s.add_train_line(stops=["1st Station", "2nd Station", "3rd Station", "4th Station"], name="The Natural Line")
s.add_train_line(stops=["A Station", "B Station", "C Station"], name="The Letter Line")
s.add_train_line(stops=["B Station", "4th Station", "U Station", "l8r Station"], name="The T9 Word Line") 


print("taking the train from 1st Station to U Station")
print(s.take_train(origin="1st Station", destination="U Station"))

print("taking the train from A Station to 1st Station")
print(s.take_train(origin="A Station", destination="1st Station"))

print("creating a new subway system with distances")

s_prime = SubwaySystem()
s_prime.add_train_line(stops=["1st Station", "2nd Station", "3rd Station", "4th Station"], name="The Natural Line")
s_prime.add_train_line(stops=["A Station", "B Station", "C Station"], name="The Letter Line", 
    time_between_stations=[("A Station", "B Station", 2), ("B Station", "C Station", 4)])
s_prime.add_train_line(stops=["B Station", "4th Station", "U Station", "l8r Station"], name="The T9 Word Line",
    time_between_stations=[("B Station", "4th Station", 12),
                           ("4th Station", "U Station", 7),
                           ("U Station", "l8r Station", 177)]) 


print("taking the train from 1st Station to 4th Station (3 hops)")
print(s_prime.take_train(origin="1st Station", destination="4th Station"))

print("taking the train from A Station to 1st Station (5 hops, but distance=17)")
print(s_prime.take_train(origin="A Station", destination="1st Station"))
