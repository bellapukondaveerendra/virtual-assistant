Intelligent Virtual Assistant - "Friday"
========================================

Overview
--------

**Friday** is an intelligent virtual assistant designed to help users automate tasks, retrieve information, and perform various operations seamlessly using voice commands. It leverages speech recognition, text-to-speech, and APIs for real-time functionality.

* * * * *

Features
--------

1.  **Voice Interaction**: Speak with the assistant to perform various tasks.
2.  **Task Automation**:
    -   Open system tools: Notepad, Camera, Calculator, Terminal.
    -   Control mouse and system functionalities.
3.  **Information Retrieval**:
    -   Wikipedia summaries.
    -   Google search.
    -   Latest news updates.
    -   Weather reports based on the user's location.
4.  **Entertainment**:
    -   Play videos on YouTube.
    -   Tell jokes or share random advice.
5.  **Communication**:
    -   Send WhatsApp messages.
    -   Compose and send emails.
6.  **Custom Greetings**: Greets the user based on the time of day.
7.  **Error Handling**: Prompts the user to type commands in case of microphone issues.

* * * * *

Requirements
------------

### Libraries and Dependencies

-   **Python 3.x**
-   **Required Modules**:
    -   `requests`
    -   `speech_recognition`
    -   `pyttsx3`
    -   `datetime`
    -   `pprint`
    -   `openai`
    -   `random`
    -   `pygame`

Install the dependencies using:

```
pip install -r requirements.txt

```

### Additional Files

-   `functions/online_ops.py`: Contains functions for online operations like fetching weather, news, jokes, etc.
-   `functions/os_ops.py`: Includes functions to interact with the system's OS.
-   `utils.py`: Contains predefined opening text responses.

* * * * *

How It Works
------------

1.  **Initialization**:
    -   Sets up text-to-speech engine.
    -   Greets the user based on the current time.
2.  **Voice Input**:
    -   Listens to user input via the microphone.
    -   Converts speech to text using Google's Speech Recognition API.
3.  **Task Execution**:
    -   Recognizes keywords in the user's input and executes corresponding actions.
    -   Handles errors and guides the user for better interaction.
4.  **Real-time APIs**:
    -   Fetches weather, news, jokes, and advice using online APIs.
    -   Plays videos on YouTube or retrieves summaries from Wikipedia.

* * * * *

Usage
-----

1.  Run the script:

    ```
    python main.py

    ```

2.  Speak your command when prompted with "Listening...".

3.  Examples of commands:

    -   "Open Notepad"
    -   "Search on Google"
    -   "Tell me a joke"
    -   "What's the weather like?"
    -   "Play [video name] on YouTube"
    -   "Send a WhatsApp message"
4.  Say "Exit" or "Stop" to terminate the assistant.

* * * * *

Customization
-------------

-   **Assistant Name**:
    -   Change the `BOTNAME` variable to customize the assistant's name.
-   **Username**:
    -   Update the `USERNAME` variable with your name.
-   **API Keys**:
    -   Replace the placeholder `openai.api_key` with your OpenAI API key.

* * * * *

Future Improvements
-------------------

-   Integrate advanced natural language understanding using GPT-based models.
-   Add more system control functionalities.
-   Implement a GUI for enhanced user experience.
-   Enable multi-language support.

* * * * *

License
-------

This project is open-source and licensed under the MIT License. Feel free to modify and distribute as per the license terms.

* * * * *

For any questions or feedback, feel free to reach out. Thank you for using Friday!
