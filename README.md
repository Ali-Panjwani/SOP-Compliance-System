# SOP-Compliance-System

This Project is a Combination and Integration of Face Mask Detection System, Face Detection and Recognition System and an Email Alert System.

Project Functionalities and Specifications:
- Developed a real-time face mask detection system using a pre-trained model.
- Incorporated a face recognition and identification system for identifying SOP violators
- Implemented face recognition system using Convolution neural network and Haarcascade model
- Developed using Python language and TensorFlow, NumPy and Pandas framework.

How the Project Works:
- Train the model for Mask Detection
- Implement a camera system to detect individuals not wearing a mask in a designated area.
- Utilize facial recognition technology to match individuals with their corresponding information from the system's database, including name and email.
- Save the names of image file in the following format: Name.RollNumber e.g. Ali Panjwani.k190365
- Trigger an alarm to alert individuals who are not wearing a mask.
- Send an email notification to the designated administration, alerting them of individuals who are not wearing a mask.
- If the individual is present in the system's database, send an additional email notification to that individual as a reminder to wear a mask.

Further Scope of the the Project:
- Continual refinement and optimization of the facial recognition technology to increase accuracy and decrease false alarms.
- Development of a reporting and analytics system to track compliance over time.
- Exploration of additional technologies such as mobile application integration for enhanced accessibility and real-time monitoring capabilities.
- Incorporation of additional models for monitoring compliance with other SOPs such as social distancing and crowd management. This could be done by integrating additional cameras, sensors and AI models to monitor and alert any potential breaches of the established protocols.

Moreover this Repository Contain:

- Project Poster
- Project Report
- The Project itself containing Mask Detection File and Face Detection File

Make a Folder name Images adding Pictures of people with their name and email in the caption. Moreover I'll be adding a Data_Generator I found online which augments face mask on face images for testing purposes.

NOTE: The Mask Detection Model and Code was found on Github and was integrated to the Project. The Credit for this portion goes to Chandrika Deb. For More Information Visit: https://github.com/chandrikadeb7/Face-Mask-Detection
