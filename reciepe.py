import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'reciepedb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print("1 add reciepe")
    print("2 view all reciepe ")  
    print("3 search reciepe")
    print("4 update reciepe")    
    print("5 delete reciepe")
    print("6 exit")
    choice = int(input('enter an option:'))
    if(choice==1):
        print('reciepe enter selected')
        name = input('enter the name')
        category  = input('enter the category')
        taste = input('enter the taste')
        price = input('enter the price ')
        sql = 'INSERT INTO `reciepe`( `name`,`category`,`taste`, `price`) VALUES (%s,%s,%s,%s)'

        data = (name,category,taste,price)
        mycursor.execute(sql , data)
        mydb.commit()
    elif(choice==2):
        sql = 'SELECT * FROM `reciepe`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        

        print("search recipeselected")

        category = input("enter the category: ")

        sql="SELECT `id`, `name`, `category`, `taste`,`price` FROM `reciepe` WHERE `category` ='"+category+"'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)
    elif(choice==4):
        print("update recipe selected")
        name = input("enter the name")
        category = input("enter the category to be updated")
        taste = input("enter the taste to be updated")
        price = input("enter the price to be updated")
        sql = "UPDATE `reciepe` SET `category`='"+category+"',`taste`='"+taste+"',`price`='"+price+"' WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("updated succusfully")
    elif(choice==5):
        print('delete the category')
        category = input('enter the category to be deleting: ')
        sql = "DELETE FROM `reciepe` WHERE `category`='"+category+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted succesfully")
    elif(choice==6):
        break