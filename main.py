from utils.helpers import load_config

def main():
    config = load_config()
    print("Application Name:", config["app_name"])
    print("Version:", config["version"])

if __name__ == "__main__":
    main()