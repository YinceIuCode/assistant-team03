# UI Module
## 1. Design and features

The UI of the chat page should contain:
  - Title (can be used for greetings)
  - Text box for input
  - Message display
    + User messages are shown on the right
    + Assistant messages are shown on the left
  - Send button (optional)

## 2. Calling backend
  - The UI can call the backend once the user has prompted within the text box and send either by pressing Enter or using the Send button, after which the contents of the text box can be delivered to the backend for processing.
  - Note: The UI should not call the backend if the user attempts to send empty data (ie. text box contains no text or only whitespaces)
