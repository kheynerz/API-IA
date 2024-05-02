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

## Cirrhosis Classification

### POST /api/model/cirrhosis

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
