from datetime import datetime
def sample_responses(input_text):
    user_message= str(input_text).lower()
    if user_message in ("hello","hi","whats popping",):
        return "Whats up my brother/sister?"

    if user_message in ("who are you",):
        return "i am daddies favorite bot ;)"

        if user_message in ("time","time?"):
            now= datetime.now()
            date_time= now.strftime("%d/%m/%y, %H:%M:%S")
            return str(date_time)

        
        return "i don't understand you."
