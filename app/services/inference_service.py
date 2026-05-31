import random
import time

def run_inference(prompt: str): 

    start_time = time.time()

    possible_responses = ["Positive sentiment", "Negative sentiment", "Neutral sentiment"]

    time.sleep(random.uniform(0.2, 1.0))

    latency = round(time.time() - start_time, 3)

    return{
        "response": random.choice(possible_responses),
        "confidence": round(random.uniform(0.75, 0.99), 2),
        "latency": latency,
        "status": "success"
    }

