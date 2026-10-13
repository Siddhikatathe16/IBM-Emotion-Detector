\# IBM Emotion Detector



A Python and Flask web application that analyzes text and identifies five emotions: anger, disgust, fear, joy, and sadness. It determines the dominant emotion using the IBM Watson NLP emotion service.



\## Features



\- Text input through a web interface

\- Flask endpoint for emotion detection

\- Emotion scores and dominant emotion output

\- Input validation and error handling

\- Unit tests using Python's `unittest` and mocked HTTP responses



\## Technologies Used



\- Python

\- Flask

\- Requests

\- IBM Watson NLP Emotion Prediction service

\- HTML, JavaScript, and Bootstrap



\## Project Structure



```text

IBM-Emotion-Detector/

├── EmotionDetection/

│   ├── \_\_init\_\_.py

│   └── emotion\_detection.py

├── static/

│   └── mywebscript.js

├── templates/

│   └── index.html

├── server.py

├── test\_emotion\_detection.py

└── README.md

```



\## Installation



Install Python, then run:



```bash

python -m pip install Flask requests

```



\## Run the Application



```bash

python server.py

```



Open `http://127.0.0.1:5000` in your browser, enter text, and click \*\*Run Sentiment Analysis\*\*.



\## Run Unit Tests



```bash

python -m unittest test\_emotion\_detection.py -v

```



\## Code Quality



Check the Flask server with:



```bash

python -m pylint server

```



\*\*Note:\*\* Successful live emotion analysis requires the IBM Watson NLP service to be reachable. If that service is unavailable or times out, the application reports an error rather than displaying invented emotion scores.

