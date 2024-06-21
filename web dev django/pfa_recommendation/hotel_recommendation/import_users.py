import pandas as pd
from hotel_recommendation.models import User
from hotel_recommendation.models import Hotel



# Read CSV file into a DataFrame
csv_file_path = 'user_only_aspects.csv'
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
  

    # Create the Product instance
    user= User(

   username=row['reviewed_by'],
    password="0000",
    aspects=row['aspects'],
       
 
  
     
    )
    #to save the current product
    user.save()

print("CSV data has been loaded into the Django database.")

#python manage.py runscript hotel_recommendation.import_users