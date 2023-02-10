#MODELS/Healthcare Survival rate

Objective:developing a model that will predict the chances of survival of a patient after 1 year of treatment (Survived_1_year).

source:https://raw.githubusercontent.com/dphi-official/Datasets


Data Description:
ID_Patient_Care_Situation: Care situation of a patient during treatment

Diagnosed_Condition: The diagnosed condition of the patient

ID_Patient: Patient identifier number

Treatment_with_drugs: Class of drugs used during treatment

Survived_1_year: If the patient survived after one year (0 means did not survive; 1 means survived)

Patient_Age: Age of the patient

Patient_Body_Mass_Index: A calculated value based on the patient’s weight, height, etc.

Patient_Smoker: If the patient was a smoker or not

Patient_Rural_Urban: If the patient stayed in Rural or Urban part of the country

Previous_Condition: Condition of the patient before the start of the treatment ( This variable is splitted into 8 columns - A, B, C, D, E, F, Z and Number_of_prev_cond. A, B, C, D, E, F and Z are the previous conditions of the patient. Suppose for one patient, if the entry in column A is 1, it means that the previous condition of the patient was A. If the patient didn't have that condition, it is 0 and same for other conditions. If a patient has previous condition as A and C , columns A and C will have entries as 1 and 1 respectively while the other column B, D, E, F, Z will have entries 0, 0, 0, 0, 0 respectively. The column Number_of_prev_cond will have entry as 2 i.e. 1 + 0 + 1 + 0 + 0 + 0 + 0 + 0 = 2 in this case. )



#MODELS/Vehicle_dataset from carsdekho.com
Objective:We all know about the marketing of Carsdekho.com.Company sells mostly the used car.So here our objective is to show the price range dependig on various factors. To analysis usedcar's price different Machine learning Models have been used to observe which ,algorithm is best and gets least error to the accuracy of model.. Dataset is imported from https://www.kaggle.com/code/dg1223/scaling/data?select=car+data.csv. Visualiaztion is done on the featuresv of the model to analyze better.Effor calculating metod are being used to make better perforamance of the predictions. Data set consists of Car_Name : This column should be filled with the name of the car.

            Year : This column should be filled with the year in which the car was bought.

            Selling_Price : This column should be filled with the price the owner wants to sell the car at.

            Present_Price : This is the current ex-showroom price of the car.

            Kms_Driven : This is the distance completed by the car in km.

            Fuel_Type : Fuel type of the car i.e Diesel,Petrol,CNG

            Seller_Type : Defines whether the seller is a dealer or an individual.

            Transmission : Defines whether the car is manual or automatic.

            Owner : Defines the number of owners the car has previously had.
