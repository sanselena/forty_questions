import pandas as pd
import matplot.pylot as plt
import numpy as np 
from sqlalchemy import create_engine


#Example-1: Data Frames

left=pd.DataFrame({'key':['k0','k1','k2','k3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']
                   })

right=pd.DataFrame({'key':['k0','k1','k2','k3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']
                    })


#Example-2: Merge

left=pd.DataFrame({'key1':['k0','k0','k1','k2'],
                   'key2':['k0','k1','k0','k1'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']
                   })

right=pd.DataFrame({'key1':['k0','k1','k1','k2'],
                    'key2':['k0','k0','k0','k0'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']
                    })

pd.merge(left,right ['key1','key2']) 
#iki index de eşit olur

pd.merge(left,right, how='outer', on=['key1','key2']) 
#eşlenenler ile eşlenmeyenler birlikte getirilir, her iki taraftaki eşlenmeyenlerin karşı değeri
#(birleştirilme değeri) NaN olarak yerleştirilir.


# example about how plots work (self example - not included in the hw)
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 3, 6]
plt.plot(x, y)

#adds labels and assigns title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Line Plot')

plt.show()


#Functional way (page 29, introduction of plots and creating subplots)
x = np.linspace(0:5:11)
y=x**2

plt.plot(x,y)
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

#Object Oriented Method

fig=plt.figure()
#figure is like an imaginary canvas!

axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')


#commerce exercise

sf_solares_data = {
    'Property': ['HomeA', 'HomeB', 'HomeC'],
    'Price': [10000000, 15000000, 12000000],
    'Location': ['San Francisco', 'San Francisco', 'San Francisco']
}

commerce_data = {
    'Product': ['ProductA', 'ProductB', 'ProductC'],
    'Sales': [200, 300, 2500],
    'Revenue': [100000, 15000, 12500]
}

sf_solares_df = pd.DataFrame(sf_solares_data)
commerce_df = pd.DataFrame(commerce_data)

engine = create_engine('sqlite:///mydatabase.db')

sf_solares_df.to_sql('sf_solares', con=engine)
commerce_df.to_sql('commerce', con=engine)


sf_solares_read = pd.read_sql('SELECT * FROM sf_solares', con=engine)
commerce_read = pd.read_sql('SELECT * FROM commerce', con=engine)

average_price = sf_solares_read['Price'].mean()
print(f'Ortalama Konut Fiyatı: {average_price}')

total_sales = commerce_read['Sales'].sum()
print(f'Toplam Satış: {total_sales}')