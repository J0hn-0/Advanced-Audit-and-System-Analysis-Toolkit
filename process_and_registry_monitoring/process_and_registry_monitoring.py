import winreg
import psutil

processes_to_monitor = ['svchost.exe', 'msmpeng.exe', 'searchapp.exe', 'rundll32.exe', 'dwm.exe']

def fetch_registry_values_for_process(process_name):
    path = f"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{process_name}"
    try:
        main_key_str, sub_key = path.split('\\', 1)
        main_key = {
            'HKLM': winreg.HKEY_LOCAL_MACHINE,
            'HKCU': winreg.HKEY_CURRENT_USER,
        }[main_key_str]

        with winreg.OpenKey(main_key, sub_key) as key:
            i = 0
            while True:
                try:
                    name, value, type_ = winreg.EnumValue(key, i)
                    print(f"Name: {name}, Value: {value}, Type: {type_}")
                    i += 1
                except OSError:
                    break
    except FileNotFoundError:
        print(f"No specific registry keys found for {process_name}.")
    except Exception as e:
        print(f"Error reading {path}: {e}")

def fetch_process_details():
    for proc in psutil.process_iter(['pid', 'name', 'threads']):
        if proc.info['name'] in processes_to_monitor:
            print(f"Details for {proc.info['name']} (PID: {proc.info['pid']}):")
            print("Threads:")
            for thread in proc.info['threads']:
                try:
                    print(f"    ID: {thread.id}, User Time: {thread.user_time}, System Time: {thread.system_time}")
                    # Memory info for thread (rough estimation by using the process's memory info)
                    mem_info = proc.memory_info()
                    print(f"    MEMORY: RSS: {mem_info.rss}, VMS: {mem_info.vms}")
                    # Status, cmdline, and CPU usage
                    print(f"    CMDLINE: {proc.cmdline()}")
                    print(f"    STATUS: {proc.status()}")
                    print(f"    CPU_PERCENT: {proc.cpu_percent(interval=0.1)}%")
                    print("-"*25)
                except psutil.NoSuchProcess:
                    pass  # The thread might've terminated between the calls
            print("="*50)

if __name__ == "__main__":
    for process in processes_to_monitor:
        print(f"Fetching registry values for {process}:")
        fetch_registry_values_for_process(process)
    print("="*50)
    fetch_process_details()
