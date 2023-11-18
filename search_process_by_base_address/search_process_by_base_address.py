import sys

def search_process_by_base_address(log_file, base_address):
    with open(log_file, 'r') as file:
        lines = file.readlines()
        process_name = None
        for line in lines:
            if 'Process Name:' in line:
                process_name = line.strip().split('\t')[0].split(': ')[1]
            if 'Base Address:' in line and base_address in line:
                print(f"Process: {process_name} has the base address: {base_address}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <log_file> <base_address>")
        sys.exit(1)
    log_file = sys.argv[1]
    base_address = sys.argv[2]
    search_process_by_base_address(log_file, base_address)
