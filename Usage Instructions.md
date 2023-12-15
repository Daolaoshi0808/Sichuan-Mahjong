# Mahjong Advisor for Sichuan Mahjong - Installation and Usage Instructions

## Prerequisites:

1. **Install Python 3:**
   - Ensure that you have Python 3 installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Packages:**
   - Open a terminal and run the following commands to install the necessary Python packages:
     ```bash
     pip install numpy
     pip install opencv-python==4.6.0.66
     ```

## Mahjong Advisor Installation:

1. **Clone the Repository:**
   - Visit the Mahjong Advisor GitHub repository: [https://github.com/Daolaoshi0808/Sichuan-Mahjong](https://github.com/Daolaoshi0808/Sichuan-Mahjong)
   - Clone or download the repository to your local machine.

2. **Navigate to the Project Directory:**
   - Open a terminal and change your current directory to the location where you have cloned/downloaded the Mahjong Advisor repository.

3. **Verify the Contents:**
   - Ensure that the following files and folders are present in the project directory:
     - `app.py`
     - `mahjong_utils.py`
     - `mahjong_predict.py`
     - 27 PNG files (representing each mahjong tile)
     - `templates` folder containing:
       - `index.html`
       - `not_menqing.html`
       - `select_tiles.html`
       - `display_result.html`

## Running Mahjong Advisor:

1. **Run the Application:**
   - In the terminal, while in the project directory, run the following command:
     ```bash
     python app.py
     ```

2. **Access the Webpage:**
   - Open a web browser and go to the URL displayed in the terminal (typically something like `http://127.0.0.1:5000/`).

3. **Upload Screenshot:**
   - On the webpage, upload a screenshot containing mahjong tiles.
   - Specify whether the tiles are menqing (all concealed) or not.

4. **Submit and Receive Recommendations:**
   - Submit the screenshot, and the Mahjong Advisor will provide recommendations for the next best move to win if the tiles are menqing.

## Important Notes:

- **Supported Screenshots:**
  - The current version only accepts screenshots from Tencent Mahjong App and iPhone 13 Pro Max.

- **Limitations:**
  - The Mahjong Advisor currently works only if the tiles are menqing (all concealed).

- **Feedback Loop:**
  - There is a machine learning feedback loop that takes user advice for better recommendations. However, the interactive user interface for this feature is not yet implemented.

## Future Updates:

- **Upgrading the Method:**
  - Future updates may include improvements and additional features. Users can download the latest version from the GitHub repository.

- **Machine Learning Integration:**
  - The machine learning feedback loop is planned to be integrated into the interacting user interface in future updates, allowing users to provide feedback for continuous improvement.

Feel free to reach out to the Mahjong Advisor community on the GitHub repository for any issues, feedback, or inquiries: [https://github.com/Daolaoshi0808/Sichuan-Mahjong](https://github.com/Daolaoshi0808/Sichuan-Mahjong)
