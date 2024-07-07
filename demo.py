import pandas as pd
capitals = pd.DataFrame(
    [
        ['Ngerulmud', 391,1.87],
        ['Vatican City', 826,100],
        ['Yaren', 1100,10.91],
        ['Funafuti', 4492,45.48],
        ['City of San Marino', 4493],
    ],
    index=['Palau', 'Vatican City', 'Nauru', 'Tuvalu', 'san Marino'],
    columns=['Capital', 'Population', 'Percentage']
)

grades = pd.DataFrame([
    [6,4], 
    [7,8], 
    [6,7], 
    [6,5], 
    [5,2], 
    [6,4], 
],
index = ['Mary', 'John', 'Ann', 'Pete', 'Laura'],
columns=['test_1', 'test_2']
)

p = pd.DataFrame({'id': [823965, 823905, 235897, 235897,235897, 983422,983422],
                   'item': ['prize', 'unit', 'prize', 'unit', 'stack', 'prize', 'stack'],
                   'value': [3.49, 'kg', 12.89, 'l', 50, 0.49, 4]
                  })
p