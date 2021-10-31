foods = {'Appetizers': {"Wings": 0, "Cookies": 0, "Spring Rolls": 0},
         'Entrees': {'Salmon': 0, 'Steak': 0, 'Meat Tornado': 0, 'A Literal Garden': 0},
         'Desserts': {'Ice Cream': 0, 'Cake': 0, 'pie': 0},
         'Drinks': {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}
         }


def menu():
    print('*'*39)
    print('**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n** To quit at any time, type "quit" **')
    print('*'*39)
    for x in foods:
        print(f"\n{x} \n------")
        for y in foods[x]:
            print(y)
    print("\n", '*'*35, '\n ** What would you like to order? **\n', '*'*35)
    quit = 1
    while(quit):
        order = input('> ')
        if(order == 'quit'):
            quit = 0
            for x in foods:
                for y in foods[x]:
                    if (foods[x][y]):
                        print(f'** {foods[x][y]} order of {y} have been added to your meal **')        
        for x in foods:
            if(order in foods[x]):
                foods[x][order]+=1
                print(f'** {foods[x][order]} order of {order} have been added to your meal **')
                break
        else:
            print("please enter item from the menu")

    


menu()
