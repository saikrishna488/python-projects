import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title ="drink water now",
            message="So how much fluid does the average, healthy adult living in a temperate climate need? The U.S. National Academies of Sciences",
            timeout=2
        )
        time.sleep(4)