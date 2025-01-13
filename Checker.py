import requests
import csv
import time

API_KEY = ""
BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

IP_LIST_FILE = "ip_list.txt"
OUTPUT_FILE = "output.csv"

def read_ip_list(file_path):
    try:
        with open(file_path, 'r') as file:
            ip_list = []
            for line in file.readlines():
                line = line.strip()
                ip_list.append(line)
        return ip_list
    except FileNotFoundError:
        print(f"File {file_path} not exists.")
        return []

def get_ip_reputation(ip):
    headers = {
        "x-apikey": API_KEY
    }
    response = requests.get(BASE_URL + ip, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error while getting data for {ip}: {response.status_code}")
        return None

def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Reputation", "Detections"])
        
        for entry in data:
            writer.writerow(entry)

def main():
    ip_list = read_ip_list(IP_LIST_FILE)
    if not ip_list:
        return
    
    results = []
    for ip in ip_list:
        print(f"Checking reputation for: {ip}")
        reputation = get_ip_reputation(ip)
        if reputation:
            malicious_count = reputation.get("data", {}).get("attributes", {}).get("malicious", 0)
            
            results.append([ip, "Malicious" if malicious_count > 0 else "Clean", malicious_count])
        if ip_list[-1] != ip:
            time.sleep(15)  # Only 4 requests/min
    
    save_to_csv(results, OUTPUT_FILE)
    print(f"Results saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
