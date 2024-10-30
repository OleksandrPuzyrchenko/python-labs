class Pool:

    def __init__(self, address="Address", water_volume=0, max_visitors=0):
        self.__address = address
        self.__water_volume = water_volume #є доступ через інстанс за межами класу
        self.__max_visitors = max_visitors

        self.public_num_field = 0
        self.public_str_field = " "

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_water_volume(self):
        return self.__water_volume

    def set_water_volume(self, water_volume):
        self.__water_volume = water_volume

    def get_max_visitors(self):
        return self.__max_visitors

    def set_max_visitors(self, max_visitors):
        self.__max_visitors = max_visitors

    def __str__(self):
        return f"Басейн за адресою {self.__address}, Об'єм води: {self.__water_volume} л, Макс. відвідувачів: {self.__max_visitors}"

    def __repr__(self):
        return f"Pool(address = {self.__address}, water_volume = {self.__water_volume}, max_visitors = {self.__max_visitors})"

    def __del__(self):
        print(f"Басейн за адресою {self.__address} видалено")

def main():
    pool_1 = Pool("Shevchenka Street 10", 500, 50)
    pool_2 = Pool("Gorodocka Street 15", 1000, 100)
    pool_3 = Pool("Stryiska Street 20", 1500, 150)
    default_pool = Pool()

    print(pool_1)
    print(pool_2)
    print(pool_3)
    print(str(pool_1))
    print(repr(pool_1))
    print(default_pool)
    print(type(default_pool) is Pool) 
    print(default_pool is Pool)

if __name__ == "__main__":
    main()
    #все наслідується через об'єкт