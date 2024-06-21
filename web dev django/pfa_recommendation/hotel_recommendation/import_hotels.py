import pandas as pd
from django.contrib.auth.models import User
from hotel_recommendation.models import Hotel



# Read CSV file into a DataFrame
csv_file_path = 'Hotel_Booking_dataset.csv'
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
  

    # Create the Product instance
    hotel= Hotel(

       
    hotel_name=row['hotel_name'],
    hotel_url=row['hotel_url'],
    avg_rating=row['avg_rating'],
    image_url=row['image_url'],
    location=row['location'],
     
    )
    #to save the current product
    hotel.save()

print("CSV data has been loaded into the Django database.")

#python manage.py runscript hotel_recommendation.import_hotels