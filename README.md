# CZ4171-IoT-Joei

This project features the development of the application called Coffee Dripper Detector. This application allows users to input images of coffee drippers into the application to receive a prediction on what the coffee dripper is. Users may either select images from their Android Device or use the in-built camera to take a picture of the coffee dripper. The image input will then be sent to the Flask Server that performs a prediction based on the image sent. The prediction result will then be sent to the Android Application for display.

These were the three development phases for this project: 
1. Creation of the Image Classification Model 
2. Flask Server Development 
3. Android Application Development 

## 1. Creation of the Image Classification Model

Google Teachable Machine was used to generate the model for classification of the 5 selected coffee drippers in this project. To train the model, a total of 100 images were fed into the model per class. The model is then exported to Tensorflow in the Keras Format, titled coffeeDripper.h5. The Google Teachable Machine file is titled IOTModel.tm which is accessible through the Google Teachable Machine website and allows for the adjustment of any of the parameters for future use.

The classes used are as follows: 
1. Origami Dripper
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234938667-d11ef6b5-d2ae-481e-a556-66142f3e4ead.png">

2. Kalita Wave Dripper
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234933587-7e451ea6-9bd1-4f2c-8ac0-e84cc85fcc7b.png">

3. Clever Dripper
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234933946-a9b3ed89-7701-4511-852e-51e1a7784a7d.jpg">

4. Flower Dripper
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234934228-31fe207a-2f58-4ec7-b138-33ac51503173.jpg">

5. V60 Dripper
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234934299-ce22c9c1-9baa-4913-8f31-4f1a8785ae0d.jpg">

The training parameters are as follows: 
1. Epochs: 50 (The total number of iterations in one cycle of the training data used for training the machine learning model)
2. Batch Size: 16 (The number of training samples utilized in one iteration)
3. Learning Rate: 0.001 (A tuning parameter in the optimization algorithm that determines the step size at each iteration)

The accuracy of the trained model can be further conveyed through the following diagrams provided for by Google Teachable Machine:

### 1. Accuracy Per Class
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234929624-a1e216cd-95d2-4a7e-8704-c0718cfd7db9.png">

### 2. Confusion Matrix
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234929762-f7832e2d-ec4d-48da-b873-47832cb3ce21.png">

### 3. Accuracy Per Epoch
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234929879-42d48ddc-c25c-4c0a-b44d-74f99d92802e.png">

### 4. Loss Per Epoch
<img width="400" alt="image" src="https://user-images.githubusercontent.com/70619856/234929982-7c54bca9-c922-4957-be15-3291728dd16d.png">

## 2. Flask Server Development 

The source code for the Python Flask Server is saved in the iotServer folder. 

The Keras Model, as detailed above, should be saved within the same file directory as the Flask Server. A Predict Function can be found within the code, which deploys the model and allows the user to run the prediction on coffee dripper images, and thereafter returns the predicted coffee dripper classification. In the Flask server, a POST request can be created to retrieve the image file uploaded from the IoT Device. The predict function would then run using the file directory storing the uploaded image. This prediction will be returned as a response, which will be sent to the apllication. 

## 3. Android Application Development 
The source code for the Android Application used is saved in the iotProject folder. 

There are 2 buttons that allows users to either select images from their Android Device or use the Android device's in-built camera to take a picture of the coffee dripper. Once the image is selected or taken from the camera, it will be shown in the placeholder space. Once the Predict Button is selected, the image is sent to the Flask Server that has the Keras Machine Learning Model. The prediction process will then be processed in the server and the result will be sent back to the application and the corresponding coffee dripper in the image will be identified and displayed as text.
