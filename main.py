import subprocess
input_file = "ip.txt"
output_file = "output.txt"

def ping_ip(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Error pinging IP {ip}: {e}")
        return False

def traceroute_ip(ip):
    try:
        result = subprocess.run(["traceroute", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"Error performing traceroute on IP {ip}: {e}")
        return False

if __name__ == "__main__":
    with open(input_file, "r") as file:
        ips = [line.strip() for line in file if line.strip()]

    responding_ips = []
    non_responding_ips = []

    for ip in ips:
        print(f"Processing IP: {ip}")
        is_responding = ping_ip(ip)
        is_traceable = traceroute_ip(ip)

        if is_responding and is_traceable:
            responding_ips.append(ip)
        else:
            non_responding_ips.append(ip)

    with open(output_file, "w") as file:
        file.write("IP Address\tObservations\n")

        if responding_ips:
            for ip in responding_ips:
                file.write(f"{ip}\tThese hosts were responding to ICMP Echo requests and traceable.\n")

        if non_responding_ips:
            for ip in non_responding_ips:
                file.write(f"{ip}\tThese hosts were neither responding to ICMP Echo requests nor traceable.\n")

    print(f"Output written to {output_file}")
