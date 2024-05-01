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

#### URL
```bash
http://localhost:5000/api/model/bitcoin
```
