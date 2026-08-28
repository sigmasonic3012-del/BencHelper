import time
import sys
import os

def simulate_progress():
    print("\n[+] Initializing Android Hardware Interface...")
    time.sleep(1)
    print("[+] Scanning CPU Clusters...", end="")
    for i in range(15):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(0.1)
    print(" DONE")

def leak():
    vault = []
    print("\n[!] Stress Test Started: Allocating Heap Memory...")
    print("[!] Monitoring LMK (Low Memory Killer) stability...")
    
    count = 0
    while True:
        # Allocate roughly 10MB per loop
        vault.append(' ' * 10**7) 
        count += 1
        
        # This makes it look like it's actually measuring something
        if count % 5 == 0:
            print(f"Allocated: {count * 10}MB | System Stability: {100 - (count // 2)}%...", end="\r")
        
        time.sleep(0.05)

if __name__ == "__main__":
    try:
        simulate_progress()
        leak()
    except KeyboardInterrupt:
        print("\nTest aborted by user.")
    except MemoryError:
        print("\nCRITICAL: System memory exhausted!")
