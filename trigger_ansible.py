import subprocess

def run_ansible_playbook():
    playbook_path = 'restart_nginx.yml'
    inventory_path = 'inventory.ini'
    
    try:
        result = subprocess.run(
            ['ansible-playbook', '-i', inventory_path, playbook_path],
            check=True,
            text=True,
            capture_output=True
        )
        print("Playbook executed successfully:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Playbook failed with error:\n")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)

if __name__ == "__main__":
    run_ansible_playbook()
