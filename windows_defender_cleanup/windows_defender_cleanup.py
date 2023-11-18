import subprocess
import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return (True, result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return (False, e.stderr.decode('utf-8'))

def delete_files(files):
    for file in files:
        # Taking ownership
        success, output = run_command(['takeown', '/f', file, '/R', '/D', 'Y'])
        if not success:
            print(f"Failed taking ownership for {file}: {output}")

        # Granting permissions
        success, output = run_command(['icacls', file, '/grant', 'administrators:F', '/T'])
        if not success:
            print(f"Failed setting permissions for {file}: {output}")

        # Deleting
        if os.path.exists(file):
            try:
                if os.path.isdir(file):
                    os.rmdir(file)
                else:
                    os.remove(file)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Failed deleting {file}: {str(e)}")
        else:
            print(f"{file} doesn't exist.")
//The paths are used as examples on what entries look like and are usually implemented
            files_to_delete = [
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasbase.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasbase.vdm",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\11\\117F366E5621BD46281CD6E886897996FA36792C",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\12\\12EE274883507D2552C4C0C9B8CFFE9B1AE7E8A4",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\49\\49BD74AB76CEEFE4C341494B35F4AB1C6CB23B37",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\4A\\4A10D9B4BE9759DB23609CE6C1417B57D67750FB"
]
            delete_files(files_to_delete)
