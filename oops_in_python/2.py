# class C1:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __mul__(self, other):
#         n1 = self.a * other.a
#         n2 = self.b * other.b
#         return C1(n1, n2)
#     def __repr__(self):
#         return f"({self.a},{self.b})"


# obj1 = C1(2, 3)
# obj2 = C1(4, 5)
# obj3 = C1(6, 7)
# result = (obj1 * obj2) * obj3
# print(result)   


"""
data handling
"""


""" Read mode - r
    Write mode - w
    Append mode - a
    Read and write - r+
    Write and read - w+
    Append and read - a+
"""
# with open("file.txt", "a+") as f:
#     data = f.write("Hello i am chinmay joshi\n")
#     f.write("new data\n")
#     f.seek(0)
#     data = f.read()
#     print(data)
#     f.close()

# with open ("file.txt", "w+") as f:
#     data = f.writelines("File ka bhi brain wash ho gaya\n")
#     f.seek(0)
#     data = f.read()
#     print(data)
#     f.close()

# with open ("file.txt", "r+") as f:
#     data = f.read()
#     print(data)
#     f.close()

""" delete file """
# import os
# os.remove("file.txt")


# with open("file.txt", "a+") as f:
#     f.writelines(["Chinu bhai\n","Chinu\n","Joshi\n","Chinmay\n","Joshi\n"])
#     f.seek(0)
#     data = f.readlines()
#     for line in data:
#         print(line)
#     f.close()

""" CSV files"""

# import csv
# data = [["Name", "Age", "City"],
#         ["Chinmay", 24, "Pune"],
#         ["Amol", 27, "Mumbai"],
#         ["Akash", 22, "Nagpur"]]
# with open("data.csv", "w", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#     f.close()

""" append data to csv file"""

# with open("data.csv", "a", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Sunil", 29, "Delhi"])
#     f.close()

"""print CSV file data"""

# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     f.close()

data = " i am chinmay joshi "
if __name__ == "__main__":
    print(data)