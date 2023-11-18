import winreg

# A list of suspicious registry keys from the GMER log
suspicious_keys = [
    r"HKLM\SYSTEM\CurrentControlSet\Control\Replace with\actual url\RNG",
]

def fetch_registry_values(path):
    try:
        # Split the path to get main key and subpath
        main_key_str, sub_key = path.split('\\', 1)

        # Map main key string to actual winreg key
        main_key = {
            'HKLM': winreg.HKEY_LOCAL_MACHINE,
            'HKCU': winreg.HKEY_CURRENT_USER,
            # Add other mappings if needed
        }[main_key_str]

        # Open the key
        with winreg.OpenKey(main_key, sub_key) as key:
            # Enumerate values of the key
            i = 0
            while True:
                try:
                    name, value, type_ = winreg.EnumValue(key, i)
                    print(f"Name: {name}, Value: {value}, Type: {type_}")
                    i += 1
                except OSError:
                    break
    except Exception as e:
        print(f"Error reading {path}: {e}")

if __name__ == "__main__":
    for key in suspicious_keys:
        print(f"Fetching values for {key}:")
        fetch_registry_values(key)
        print("="*50)
