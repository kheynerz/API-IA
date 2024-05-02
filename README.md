# API-IA

# Installation and requirements

### Python dependencies
```bash
pip install -r requirements.txt
```
### FFmpeg

[Installation on windows](https://phoenixnap.com/kb/ffmpeg-windows)

# Agents

### POST /api/speech-to-text
ContentType: multipart/form-data;  
Body (Key -> Value):  
Audio -> AudioFile.wav 

#### URL
```bash
http://localhost:5000/api/speech-to-text
```

### POST /api/feeling

ContentType: multipart/form-data;  
Body (Key -> Value):   
Image -> Image.jpg

#### URL
```bash
http://localhost:5000/api/feeling
```
# Machine Learning Models

## Bitcoin prediction

### POST /api/model/bitcoin

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `volume` | required | int  | A numerical variable representing the volume of Bitcoin transactions carried out during the corresponding day.                                                                     |
|     `market_cap` | required | int  | A numerical variable indicating the market capitalization of Bitcoin at the end of the corresponding day. |

## Cirrhosis Classification

### POST /api/model/cirrhosis

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `cholesterol` | required | int  | Serum cholesterol level in mg/dl.                                                                     |
|     `albumin` | required | float64  | Albumin level in gm/dl. |
|     `copper` | required | int  | Urinary copper in ug/day. |
|     `alk_phos` | required | float64  | Alkaline phosphatase in U/liter. |
|     `tryglicerides` | required | int  | Triglyceride level in mg/dl. |
|     `prothrombin` | required | float64  | Prothrombin time in seconds. |

#### URL
```bash
http://localhost:5000/api/model/cirrhosis
```

## Wine Quality Classification

### POST /api/model/wine

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `fixed_acidity` | required | float64  | Fixed acidity of the wine.                                                                     |
|     `volatile_acidity` | required | float64  | Volatile acidity of the wine. |
|     `citric_acid` | required | float64  | Citric acid of the wine. |
|     `residual_sugar` | required | float64  | Residual sugar in the wine. |
|     `chlorides` | required | float64  | Chlorides in the wine. |
|     `free_sulfur_dioxide` | required | float64  |  Free sulfur dioxide in the wine. |
|     `total_sulfur_dioxide` | required | float64  |  Total sulfur dioxide in the wine. |
|     `density` | required | float64  | Density of the wine. |
|     `pH` | required | float64  | pH level of the wine. |
|     `sulphates` | required | float64  | Sulphates in the wine. |
|     `alcohol` | required | float64  | Alcohol content in the wine. |

#### URL
```bash
http://localhost:5000/api/model/wine
```

## Stroke Classification (ictus)

### POST /api/model/stroke

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `age` | required | float64  | Age of the patient. |
|     `hypertension` | required | int64  | 0 if the patient doesn't have hypertension, 1 if the patient has hypertension. |
|     `heart_disease` | required | int64  | 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease. |
|     `avg_glucose_level` | required | float64  | Average glucose level in blood. |
|     `bmi` | required | float64  | Body mass index. |
|     `gender_Male` | required | bool  | True if the patient is male, False otherwise. |
|     `gender_Other` | required | bool  | True if the patient's gender is Other, False otherwise. |
|     `ever_married_Yes` | required | bool  | True if the patient is ever married, False otherwise. |
|     `work_type_Never_worked` | required | bool  | True if the patient's work type is Never worked, False otherwise. |
|     `work_type_Private` | required | bool  | True if the patient's work type is Private, False otherwise. |
|     `work_type_Self-employed` | required | bool  | True if the patient's work type is Self-employed, False otherwise. |
|     `work_type_children` | required | bool  | True if the patient's work type is children, False otherwise. |
|     `Residence_type_Urban` | required | bool  | True if the patient's residence type is Urban, False otherwise. |
|     `smoking_status_formerly_smoked` | required | bool  | True if the patient formerly smoked, False otherwise. |
|     `smoking_status_never_smoked` | required | bool  | True if the patient never smoked, False otherwise. |
|     `smoking_status_smokes` | required | bool  | True if the patient smokes, False otherwise. |


#### URL
```bash
http://localhost:5000/api/model/stroke
```

## Phone Company Churn Classification

### POST /api/model/phone_company_churn

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `gender` | required | Categorical (binary)  | Male, Female |
|     `SeniorCitizen` | required | Categorical (binary)  | Yes, No |
|     `Partner` | required | Categorical (binary)  | Yes, No |
|     `Dependents` | required | Categorical (binary)  | Yes, No |
|     `tenure` | required | Numeric  | Number of months |
|     `PhoneService` | required | Categorical (binary)  | Yes, No |
|     `MultipleLines` | required | Categorical (nominal)  | Yes, No, No phone service |
|     `InternetService` | required | Categorical (nominal)  | DSL, Fiber optic, No |
|     `OnlineSecurity` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `OnlineBackup` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `DeviceProtection` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `TechSupport` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `StreamingTV` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `StreamingMovies` | required | Categorical (nominal)  | Yes, No, No internet service |
|     `Contract` | required | Categorical (ordinal)  | Month-to-month, One year, Two year |
|     `PaperlessBilling` | required | Categorical (binary)  | Yes, No |
|     `PaymentMethod` | required | Categorical (nominal)  | Mailed check, Bank transfer (automatic), Electronic check, Credit card (automatic) |
|     `MonthlyCharges` | required | Numeric  | Monthly charges |
|     `TotalCharges` | required | Numeric  | Total accumulated charges |

#### URL
```bash
http://localhost:5000/api/model/phone_company_churn
```

## Covid Recovered People Prediction

### POST /api/model/covid

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SNo               | required | int     | Serial number, unique identifier of the observation.     |
| ObservationDate   | required | string  | Date of the observation in number format.             |
| Province/State    | required | string  | Province or state of the observation. |
| Country/Region    | required | string  | Country of observation.                                   |
| Last Update       | required | string  | Time in UTC at which the row is updated for the given province or country. (Not standardised and so please clean before using it). |
| Confirmed         | required | int     | Cumulative number of confirmed cases till that date.      |
| Deaths            | required | float   | Cumulative number of deaths till that date.               |

#### URL
```bash
http://localhost:5000/api/model/covid
```


## Body Fat Prediction

### POST /api/model/bmi

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Density          | required | float64 | Density determined from underwater weighing.                                                            |
| Percent_body_fat | required | float64 | Percentage of body fat from Siri's equation.                                                            |
| Age              | required | float64 | Age in years.                                                                                           |
| Weight           | required | float64 | Weight in pounds.                                                                                       |
| Height           | required | float64 | Height in inches.                                                                                       |
| Neck             | required | float64 | Circumference of the neck in centimeters.                                                               |
| Chest            | required | float64 | Circumference of the chest in centimeters.                                                              |
| Abdomen          | required | float64 | Circumference of the abdomen 2 in centimeters.                                                          |
| Hip              | required | float64 | Circumference of the hip in centimeters.                                                                |
| Thigh            | required | float64 | Circumference of the thigh in centimeters.                                                              |
| Knee             | required | float64 | Circumference of the knee in centimeters.                                                               |
| Ankle            | required | float64 | Circumference of the ankle in centimeters.                                                              |
| Biceps           | required | float64 | Circumference of the biceps (extended) in centimeters.                                                  |
| Forearm          | required | float64 | Circumference of the forearm in centimeters.                                                            |
| Wrist            | required | float64 | Circumference of the wrist in centimeters.                                                              |


#### URL
```bash
http://localhost:5000/api/model/bmi
```


## Car Price Prediction

### POST /api/model/car_price

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key            | Required | Type   | Description                                                            |
|----------------|----------|--------|-------------------------------------------------------------------------|
| Year           | Required | int64   | Year                                                                   |
| Selling_Price  | Required | float64 | Selling Price                                                          |
| Kms_Driven     | Required | int64   | Kilometers Driven                                                      |
| Fuel_Type      | Required | int64   | Fuel Type (Petrol, Diesel, or Other)                                   |
| Seller_Type    | Required | int64   | Seller Type (Dealer or Individual)                                     |
| Transmission   | Required | int64   | Transmission Type (Manual or Automatic)                                |
| Owner          | Required | int64   | Number of Previous Owners        

#### URL
```bash
http://localhost:5000/api/model/car_price
```

## Avocado Price Prediction

### POST /api/model/avocado_price

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   total_volume | Required  | float   | Total number of avocados sold                                                                           |
|            4046| Required  | float   | Total number of avocados with PLU 4046 sold                                                            |
|            4225| Required  | float   | Total number of avocados with PLU 4225 sold                                                            |
|            4770| Required  | float   | Total number of avocados with PLU 4770 sold                                                            |
|     total_bags | Required  | float   | Total number of bags                                                                                     |
|      small_bags| Required  | float   | Total number of small bags                                                                              |
|      large_bags| Required  | float   | Total number of large bags                                                                              |
|     xlarge_bags| Required  | float   | Total number of extra large bags                                                                        |
|           type | Required  | int     | Type of avocado (0 for conventional, 1 for organic)                                                    |
|           year | Required  | int     | The year of observation                                                                                 |
|          month | Required  | int     | The month of observation                                                                                |
|         spring | Required  | int     | Indicator for spring season (1 for spring, 0 otherwise)                                                 |
|         summer | Required  | int     | Indicator for summer season (1 for summer, 0 otherwise)                                                 |
|           fall | Required  | int     | Indicator for fall season (1 for fall, 0 otherwise)                                                     |

#### URL
```bash
http://localhost:5000/api/model/avocado_price
```

## Hepatitis C Classification

### POST /api/model/hepatitis

ContentType: application/json;  
**Body**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        AST| Required | float  | Aspartate Aminotransferase                            |
|        BIL| Required | float  | Bilirubin                                             |
|        GGT| Required | float  | Gamma-Glutamyl Transferase      
#### URL
```bash
http://localhost:5000/api/model/hepatitis
```
