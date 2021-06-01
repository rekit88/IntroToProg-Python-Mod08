# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'C:\\_PythonClass\Assignment08\products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products  name
        product_price: (float) with the products standard price
    methods:
    changelog: (When,Who,What)
        RRoot,5/31/2021,Created Class
        P.Timchenko, 5/31/2021, Modified code to complete assignment 8
    """
    Name = ""
    Price = 0

    def __init__(self, str_product_name, flt_product_price):  # Constructor
        self.__product_name = str_product_name
        self.__product_price = flt_product_price

    # Properties
    @property  # Getter
    def __product_name(self):
        return str(self.Name)

    @__product_name.setter
    def __product_name(self, value):
        if value.isnumeric():
            raise Exception("Names cannot be numbers")
        else:
            self.Name = value

    @property  # Getter
    def __product_price(self):
        return float(self.Price)

    @__product_price.setter
    def __product_price(self, value: float):
        if str(value).replace('.', '', 1).isdigit():
            self.Price = value
        else:
            raise Exception("Prices must be numbers")

    # Methods
   # def to_string(self):
     #   return self.__str__()

    def __str__(self):
        return self.Name + " - $" + str(self.Price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,5/31/2021,Created Class
        P.Timchenko, 5/31/2021, Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        file = open(file_name, "w")
        for product in list_of_product_objects:
            file.write(product.__str__()+"\n")
        file.close()


    @staticmethod
    def read_data_from_file(file_name: str):
        list_of_product_rows = []
        file = open(file_name, "r")
        for line in file:
            data = line.split("- $")
            if data:
                row = Product(data[0], float(data[1]))
            list_of_product_rows.append(row)
        file.close()
        return list_of_product_rows
    """ Performs Input and Output tasks """


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for performing Input and Output
    methods:

        print_menu_items()

        print_current_list_items(list_of_rows)

        input_product_data()

    changelog: (When,Who,What)

        RRoot,5/31/2021,Created Class

        P.Timchenko, 5/31/2021, Modified code to complete assignment 8
    """

#TODO: Add code to show menu to user:
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

                :return: nothing
                """
        print(''' 
            Menu of Options 
            1) Show current data 
            2) Add a new item 
            3) Save Data to File 
            4) Exit Program 
            ''')

# TODO: Add code to get user's choice:

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        return choice


# TODO: Add code to show the current data from the file to user:

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        print("Current items and products are: ")
        for row in list_of_rows:
            print(row.Name + " - $" + str(row.Price) + "")
        print("-------------------------------")
# TODO: Add code to get product data from user:
    @staticmethod
    def input_product_data():
        p = Product("", 0)
        try:
            inputname = input("What is the product name? - ").strip()
            inputprice = input("What is the price? - ").strip()
            p = Product(inputname, inputprice)
        except Exception as e:
            print(e)
            return None
        return p


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
except Exception as e:
    print("Error, file not found")

while True:
    IO.print_menu_items()  # Show user a menu of options
    strChoice = IO.input_menu_choice()  # Get user's menu option choice
    if strChoice.strip() == '1':
        IO.print_current_list_items(lstOfProductObjects)  # Show user current data in the list of product objects
        continue
    elif strChoice.strip() == '2':
        userinput = IO.input_product_data()
        if userinput:
            lstOfProductObjects.append(userinput)  # Let user add data to the list of product objects
        continue
    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue
    elif strChoice.strip() == '4':
        input("\n\nPress enter to exit")
        break  # let user save current data to file and exit program




# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
