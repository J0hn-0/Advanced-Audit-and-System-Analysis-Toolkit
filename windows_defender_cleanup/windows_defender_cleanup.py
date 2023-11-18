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

            files_to_delete = [
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasbase.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasbase.vdm",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasdlta.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpasdlta.vdm",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpavbase.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpavbase.vdm",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpavdlta.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpavdlta.vdm",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpengine.dll",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Definition Updates\\Backup\\mpengine.lkg",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Service\\Unknown.Log",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Resources\\FC\\FC1F8811DD5CC9C714B057D08ED474E8D7ED1FE5",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Resources\\E2\\E251F5C3A768E90ABBAE9671A8953932AC358DCB",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Resources\\9A\\9ACB6B4ADE2FD1052FED8F1CA97DDD91570C2905",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{00059140-0000-0000-738B-FEB68FE6604B}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8003A269-0000-0000-0416-F33CA1CD2E84}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8003C2AE-0000-0000-E690-BDDF657D03FE}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8003D7CF-0000-0000-6CA4-2F0A1A608F8B}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80044876-0000-0000-42B3-302C2895BF24}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8004A738-0000-0000-C902-EAD188C74F7A}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8004A738-0000-0000-F21B-0BDFCBDBFB67}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{8004F10C-0000-0000-754B-985212E265E1}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80053BBC-0000-0000-BB23-2B41388063F7}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80054329-0000-0000-4403-4A1C7CC9A044}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80054329-0000-0000-5E4F-B8EC2DC0071D}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80059000-0000-0000-5022-981C5661E181}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\Entries\\{80059000-0000-0000-54D6-BEB773EFA5F7}",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\11\\117F366E5621BD46281CD6E886897996FA36792C",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\12\\12EE274883507D2552C4C0C9B8CFFE9B1AE7E8A4",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\49\\49BD74AB76CEEFE4C341494B35F4AB1C6CB23B37",
    "C:\\ProgramData\\Microsoft\\Windows Defender\\Quarantine\\ResourceData\\4A\\4A10D9B4BE9759DB23609CE6C1417B57D67750FB"
]
            delete_files(files_to_delete)
