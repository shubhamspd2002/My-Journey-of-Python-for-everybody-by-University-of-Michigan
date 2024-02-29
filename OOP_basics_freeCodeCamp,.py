#OOP
#here we are creating class. say if u type item = 'phone' and then print(type(item)), you will get class 'str'. Similarly we will make our own class
#methods are functions inside classes
class Item:
    def __init__(self): #this is a method that we have created. every def must start with self which takes instance as the 1st parameter
        print('i am created')
    def calculate_total_price(self, x, y): #calculate_total_price is called a method
        return x*y
         
item1 = Item() #u can think this as let instance item1 belong to class Item. item1 can also be called as object
item1.name = 'phone' #item1 of class Item has a variable name containing a string 'phone'
item1.price = 100
item1.quantity = 5

Item.calculate_total_price(item1, 100, 5) #you can also call out the instance like this item1 goes in self, 100 in x and 5 in y

#here each attribute name, price and quantity is assigned to 1 instance 'item' of the class Item

# print(type(item1)) #item
# print(type(item1.name)) #str
# print(type(item1.price)) #int
# print(type(item1.quantity)) #int
print(item1.calculate_total_price(item1.price, item1.quantity)) #here item1, item1.price and item1.quantity are passed as an argument to self, x and y respectively in class Item. This will give OP as 500



item2 = Item() 
item2.name = 'laptop' 
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

class Items:
    def __init__(self, name): #this is a method that we have created. here we have put one more parameter name which is known as the instance
        print(f'an instance created: {name}') 
    def calculate_total_price(self, x, y):
        return x*y

item2 = Items('tablet') #putting here tablets is crucial because we now have new attribute called instance
item2.name = 'tablet' 
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

item1 = Items('pc') #you can now pass in any attribute for name

print('\n')

class Itemss:
    def __init__(self, name: str, price: float, quantity = 0): #this is a method that we have created. here we have put one more parameter name which is known as the instance. u can initialize quantity to 0 incase the quantity argument is not passed by item1 or 2. if it is passed the it gets updated. here name : str means name will only take strings as an argument and not int of float. in price, float represents both int as well as float. In quantity if u pass an argument through instance as '1' it will give an error cause as we have initialized it with an int 0, it will only take int as an argument
        print(f'an instance created: {name} {price} {quantity}')
        #run validations to the received arguments
        assert price >= 0, f'price {price} is not greater than or equal to 0' #assert is a funtion to match what is happening here, to your expectations
        assert quantity >= 0, f'quantity {quantity} is not greater than or equal to 0'  #we assert that both quantity and price must be greater than or equal to 0. later after putting a comma, we can also add a comment that price is not greater than or equal to 0 when the error occurs
    
        #assign to self objects
        self.name = name#by using this we dont need to write item2.name = 'laptop' and item1.name = 'phone'. This is called assigning attributes dynamically
        self.price = price #same concept as name. u can also change the name as item1.cost = price and there is no problem. but later you have to write print(item1.cost)
        self.quantity = quantity #same concept as name
        
    def calculate_total_price(self): #In the calculate_total_price method, you don't need to pass self as an argument explicitly. When defining methods in a class, Python automatically passes the instance itself as the first argument (which is traditionally named self). 
        return self.price*self.quantity #In the calculate_total_price method, you don't need to use self.price or quantity. They are attributes of the instance, so they are accessed directly within the method.

item1 = Itemss('tablet', 100, 5) #here we are passing the attributes name price and quantity of the object item1 as an attribute to the class Itemss. here if u remove 5 and run, then the quantity will automatically become 0 as it is initialized in the class
item2 = Itemss('phone', 1000, 3)


#print(item1.name)
print(item2.name)
#print(item1.price)
print(item2.price)
#print(item1.quantity)
print(item2.quantity)

# Print the total price for each item
print("Total price for item 1:", item1.calculate_total_price()) #here if u dont put the bracket after alculate_total_price then it will show the location of the variable
print("Total price for item 2:", item2.calculate_total_price())

#item3 = Itemss('earphone', '1000', 3) #here if we pass the price as a string then it will print the string three times ('1000' *3)

#item4 = Itemss('phone', -1000, -1)  #if u run this then it will show assertion error cause we assert that both quantity and price must be greater than or equal to 0

#here all we learned about was instance attribute
#now we will learn about the class attribute

class Itemz:
    pay_rate = 0.8 #the pay rate after 20% discount. this is the class attribute
    def __init__(self, name: str, price: float, quantity = 0): #this is a method that we have created. here we have put one more parameter name which is known as the instance. u can initialize quantity to 0 incase the quantity argument is not passed by item1 or 2. if it is passed the it gets updated. here name : str means name will only take strings as an argument and not int of float. in price, float represents both int as well as float. In quantity if u pass an argument through instance as '1' it will give an error cause as we have initialized it with an int 0, it will only take int as an argument
        print(f'an instance created: {name} {price} {quantity}')
        #run validations to the received arguments
        assert price >= 0, f'price {price} is not greater than or equal to 0' #assert is a funtion to match what is happening here, to your expectations
        assert quantity >= 0, f'quantity {quantity} is not greater than or equal to 0'  #we assert that both quantity and price must be greater than or equal to 0. later after putting a comma, we can also add a comment that price is not greater than or equal to 0 when the error occurs
        
        #assign to self objects
        self.name = name#by using this we dont need to write item2.name = 'laptop' and item1.name = 'phone'. This is called assigning attributes dynamically
        self.price = price #same concept as name. u can also change the name as item1.cost = price and there is no problem. but later you have to write print(item1.cost)
        self.quantity = quantity #same concept as name
         
    def calculate_total_price(self): #In the calculate_total_price method, you don't need to pass self as an argument explicitly. When defining methods in a class, Python automatically passes the instance itself as the first argument (which is traditionally named self). 
        return self.price*self.quantity
    
    def apply_discount(self): #this will update or overwrite the price attribute
        self.price = self.price * self.pay_rate #here if u use Itemz.pay_rate then for item.5 here, the payrate wont update here cause now it is strictly going to use class lvl payrate and not instance lvl. so its safe to write self.pay_rate to use it eventhough it is class attribute
        return self.price
    
#print(item4.price) #u just cannot write like this, u have to 1st define the instance
    
item4 = Itemz('keyboard', 100, 10)   
print(Itemz.pay_rate) #here we are accessing the class attribute 
print(item4.pay_rate) #the item4 could not find the pay_rate on the instance level (instance is item4). so it searches at a class level and as it exists, it prints.


print('\n')
#to see all the attributes belonging to class or instance, do the following, which will create a dictionary of attributes
#print(Itemz.__dict__) #here u will find 0.8 because it is an attribute of Itemz class
#print(item4.__dict__) #here u wont find 0.8 cause it isnt an attribute of item4 instance


#print(item4.apply_discount()) #here if u unhash this then run then print(item4.price)below will not print the original price but the updated price
print(item4.price) #op = 2000
item4.apply_discount() #u have to call out the function for the price to get updated aftermultiplying with pay_rate
print(item4.price)

print('break')
#now if u want to change the payrate for a different item, but u dont want to change the payrate class attribute, just do this:
item5 = Itemz('mouse', 100, 10)
item5.pay_rate = 0.5 #now for item 5, class attribute payrate = 0.8 will be overwritten by 0.5
item5.apply_discount() #u have to 
print(item5.price)

#here
