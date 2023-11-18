import psutil

def list_processes():
    processes = []

    for proc in psutil.process_iter(attrs=['pid', 'name', 'threads', 'num_handles']):
        process_info = {
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'threads': [],
            'handles': proc.info['num_handles']
        }
        
        if proc.info['threads'] is not None:
            for thread in proc.info['threads']:
                process_info['threads'].append({
                    'tid': thread.id,
                    'user_time': thread.user_time,
                    'system_time': thread.system_time
                })
        
        processes.append(process_info)

    return processes

if __name__ == "__main__":
    processes = list_processes()
    for proc in processes:
        print(f"Process: {proc['name']} (PID: {proc['pid']}) - Handles: {proc['handles']}")
        for thread in proc['threads']:
            print(f"   Thread ID: {thread['tid']}, User Time: {thread['user_time']}, System Time: {thread['system_time']}")
