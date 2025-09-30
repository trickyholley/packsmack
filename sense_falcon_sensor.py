import subprocess

BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'

def sense_falcon_sensor():
    print(f"{YELLOW}Sense Falcon Sensor v0.never")
    print(f"{BLUE}----------------------------------")
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', 'falcon-sensor'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        status = result.stdout.strip()

        if status == 'active':
            print(f"{GREEN}PackSmack sensed the Falcon Sensor!")

    except subprocess.CalledProcessError as e:
        status = e.stdout.strip() if e.stdout else 'unknown'
        print(f"{RED}PackSmack did NOT sense the Falcon Sensor!")
        print(f"{RED}Falcon Sensor status: {status}")
        print(f"{BLUE}----------------------------------")

        log_result = subprocess.run(
            ['systemctl', 'status', 'falcon-sensor'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"{CYAN}Falcon Sensor systemctl status log:")
        print(f"{CYAN}{log_result.stdout}")

if __name__ == "__main__":
    sense_falcon_sensor()
