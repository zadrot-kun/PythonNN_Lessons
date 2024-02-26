
class MyPath:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def __str__(self):
        return self.base_path

    def __truediv__(self, scalar):
        return MyPath(self.base_path + scalar)

    def __getitem__(self, index):
        return self.base_path.split('\\')[index]

    def __len__(self):
        return len(self.base_path.split('\\'))


my_folder = MyPath(r'C:\users\artem')
my_folder = my_folder / '\\desktop'

print(my_folder)
print(my_folder[3])
print(len(my_folder))
print('-'*100)

list1 = [50, 60, 70]
print(list1[1])
