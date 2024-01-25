#Load CSV Files with Pandas
#--------------------------------------------------------
import pandas
pandas.set_option('display.max_rows', 8)
pandas.set_option('display.max_column',5)
pandas.set_option('display.width', 1000)

filename="indians-diabetes.data.csv"
hnames = ['preg', 'plas', 'pres',
          'skin', 'test', 'mass', 'pedi', 'age', 'class']

df = pandas.read_csv( filename, names=hnames   )
print("Size of training data = ", df.shape  )

print("\n\n")
print( df.dtypes )
print("\n\n")
print(df)
print("\n\n\n")

print( df.describe()  )
print("\n\n\n")


print( df.describe(include="all")  )
print("\n\n\n")

class_counts = df.groupby('class').size()
print( class_counts  )