# Detrimne the responses from the bot to certain things
def handle_response(message) -> str:
    lower_message = message.lower()
    
    if lower_message == "Check":
        return 'I am running'
        
    if lower_message == "Skibidi Gyat":
        return 'Toilet Rizz'
    
    