# Sichuan Mahjong Advisor
Authors: Jiaxi Liu and Hongkai Lou

## Abstract
The "Sichuan Mahjong Advisor" project aims to create an interactive web application that assists players in making optimal decisions during the game of Sichuan Mahjong. This will be achieved through a multi-step process:
  
1. **Image Processing for Tile Recognition**: Utilize computer vision techniques to identify Mahjong tiles from screenshots of an existing Mahjong app.

2. **User Interface for Input and Feedback**: Create an intuitive interface allowing users to upload their game state screenshots and receive tailored advice. Users will also be able to provide feedback on the suggestions.

3. **Heuristic-Based Initial Recommendations**: Implement a heuristic-based approach in the absence of user feedback or a machine learning model. This involves providing initial suggestions based on predefined rules derived from common Mahjong strategies.

4. **Data Handling for User Feedback Analysis**: Implement a feedback loop to continuously analyze and incorporate user input into the system. The feedback loop operates as follows:
    
    1. **Collection of Feedback**: Users provide feedback on the advice given by the system. This may include whether the suggested moves were helpful or not, or the user may even suggest the best move if they think the advice is not helpful.
    
    2. **Feedback Analysis**: The system aggregates and analyzes user feedback to understand which types of advice are most effective.
    
    3. **Refinement of Advice Strategies**: The system refines its advice strategies based on the feedback received, gradually improving its recommendations over time.

Technical Components:
  1. Image Processing for Mahjong Tile Recognition
  2. User Interface for Input and Feedback
  3. Heuristic-Based Initial Recommendations
  4. Data Handling for User Feedback Analysis

## Planned Deliverables
### Full Success
The full success scenario envisions a functional web application where users can upload screenshots of their Mahjong game state, receive tailored advice, and provide feedback on the suggestions. The system will learn from this feedback to improve future recommendations.
### Partial Success
In case the web application encounters challenges in implementation, we will ensure that there is a code repository available showcasing the image processing pipeline, the heuristic-based recommendations, and the feedback loop. This will serve as a foundation for future development and can be used for further refinement.

## Resources Required
1. Data: We will need a dataset of screenshots from an existing Mahjong app for tile recognition and user interface testing. This dataset will be used for training and testing our image processing pipeline.
2. Computational Resources: We will require access to a machine with sufficient computational power for image processing tasks. This can be a personal computer or a cloud-based service like Google Colab.

## Tools and Skills Required
1. Python: Proficiency in Python programming for implementing the image processing pipeline, web interface, and feedback loop.
2. Image Processing Libraries: Familiarity with libraries like OpenCV or PIL for processing and recognizing Mahjong tiles in screenshots.
3. Web Development (Flask): Knowledge of web frameworks, particularly Flask, for creating an interactive user interface.

## What You Will Learn
1. Advanced Image Processing Techniques:
We will gain expertise in advanced image processing techniques, including object recognition and data extraction.
2. Integration of User Feedback in Application Design:
We will acquire skills in designing a user interface that encourages user feedback and effectively incorporates it into the system.

## Risks
1. Image Quality: The success of our image processing pipeline heavily depends on the quality and consistency of the screenshots provided by users. In case of low-resolution or distorted images, the algorithm's performance may be compromised.
2. User Feedback Quality: Ensuring that user feedback is constructive and representative of the user's actual experience will be crucial for the effectiveness of the feedback loop.

## Ethics
The Sichuan Mahjong Advisor has the potential to impact various groups of users. It's important to consider potential biases or harms:
1. Accessibility: We will work to ensure that the web application is accessible to a wide range of users, including those with disabilities.
2. Cultural Sensitivity: We'll be cautious about any cultural biases in the advice provided, ensuring that it caters to a diverse user base.
3. User Privacy: We will prioritize user privacy and data security, ensuring that no personally identifiable information is stored or misused.

The "Sichuan Mahjong Advisor" has the potential to benefit several groups of people:
1. Mahjong Enthusiasts: This app can greatly benefit Mahjong players, especially those who are looking to improve their skills and strategic thinking in the game.
2. Novice Players: Newcomers to Mahjong may find this app particularly helpful in understanding optimal moves and gaining confidence in their gameplay.
3. Elderly Individuals: Mahjong is known for its cognitive benefits, making it particularly beneficial for elderly individuals. It requires strategic thinking, memory, and attention, which helps keep the mind active and engaged.

While the app offers significant benefits, there are potential groups that may not find it as suitable:
1. Players Preferring Manual Decision-Making: Some players, including elderly individuals, may prefer the challenge of making their own decisions without relying on external advice. The app might reduce the satisfaction for this group.
2. Traditionalists: Elderly players who have a strong attachment to the traditional way of playing Mahjong may view the app as deviating from the authentic experience of the game.

Considering the potential benefits and thoughtful implementation, the "Sichuan Mahjong Advisor" could contribute positively:
1. The app assumes that providing tailored advice in Mahjong can enhance the overall gaming experience and potentially lead to a broader appreciation of the game.
2. It is assumed that the app respects the cultural and ethical aspects of the game, avoiding any form of bias, discrimination, or unfair advantage. This is particularly crucial when considering the elderly demographic.

The "Sichuan Mahjong Advisor" has the potential to significantly benefit a wide range of players, including Mahjong enthusiasts, novices, and especially elderly individuals seeking cognitive stimulation. By respecting the preferences and needs of different player groups, the app can contribute to the well-being and quality of life of its users.

## Conclusion
The "Sichuan Mahjong Advisor" project aims to create a valuable tool for Mahjong players, leveraging advanced image processing, heuristic-based recommendations, and user feedback to provide tailored advice. We are excited to embark on this project and look forward to the learning opportunities it presents.
