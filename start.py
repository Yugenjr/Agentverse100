import os
import sys
import subprocess
import time
import urllib.request
import webbrowser
import threading
from dotenv import load_dotenv

def print_sys(msg):
    print(f"[SYSTEM] {msg}", flush=True)

def check_keys():
    print_sys("Verifying Groq API keys...")
    missing = False
    for i in range(1, 11):
        key_name = f"GROQ_API_KEY_{i}"
        val = os.getenv(key_name)
        if not val or val.strip() == "" or "your_groq_api_key" in val:
            print_sys(f"Warning: {key_name} is not properly configured.")
            missing = True
    if not missing:
        print_sys("All 10 Groq API keys verified.")
    else:
        print_sys("Some API keys are missing or use the default placeholder.")

def wait_for_backend():
    print_sys("Waiting for backend to be available at http://localhost:8000/api/agents...")
    # Exponential backoff or just loop with 1s sleep
    for _ in range(30):
        try:
            # use a known endpoint, the root gets 200, /api/agents gets 200 too
            req = urllib.request.Request("http://localhost:8000/")
            with urllib.request.urlopen(req) as response:
                if response.getcode() == 200:
                    print_sys("Backend is ready!")
                    return True
        except Exception:
            pass
        time.sleep(1)
    return False

def stream_output(pipe, prefix):
    try:
        for line in iter(pipe.readline, b''):
            decoded_line = line.decode('utf-8', errors='replace').rstrip()
            if decoded_line:
                print(f"[{prefix}] {decoded_line}", flush=True)
    except Exception:
        pass

def main():
    load_dotenv()
    
    check_keys()
    
    print_sys("Starting services...")
    
    backend_cwd = os.path.join(os.getcwd(), "backend")
    frontend_cwd = os.path.join(os.getcwd(), "frontend")
    
    # If the user runs `python start.py`, sys.executable is the Python interpreter.
    # It might be a global python or a venv python. We just use sys.executable.
    python_exec = sys.executable
        
    backend_cmd = [python_exec, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    frontend_cmd = "npm run dev"
    
    try:
        backend_process = subprocess.Popen(
            backend_cmd,
            cwd=backend_cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        print_sys(f"Failed to start backend process: {e}")
        return

    try:
        frontend_process = subprocess.Popen(
            frontend_cmd,
            cwd=frontend_cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
        )
    except Exception as e:
        print_sys(f"Failed to start frontend process: {e}")
        backend_process.terminate()
        return

    # Start threads to consume output streams
    t_back = threading.Thread(target=stream_output, args=(backend_process.stdout, "BACKEND"), daemon=True)
    t_front = threading.Thread(target=stream_output, args=(frontend_process.stdout, "FRONTEND"), daemon=True)
    t_back.start()
    t_front.start()
    
    if wait_for_backend():
        print_sys("Opening browser...")
        try:
            webbrowser.open("http://localhost:3000")
        except Exception as e:
            print_sys(f"Failed to open browser: {e}")
    else:
        print_sys("Warning: Backend did not become available in time.")
    
    try:
        while True:
            time.sleep(1)
            # Handle crashes
            if backend_process.poll() is not None:
                print_sys("Backend process exited unexpectedly. Restarting once...")
                backend_process = subprocess.Popen(
                    backend_cmd,
                    cwd=backend_cwd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
                )
                t_back = threading.Thread(target=stream_output, args=(backend_process.stdout, "BACKEND"), daemon=True)
                t_back.start()
                
            if frontend_process.poll() is not None:
                print_sys("Frontend process exited unexpectedly. Restarting once...")
                frontend_process = subprocess.Popen(
                    frontend_cmd,
                    cwd=frontend_cwd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    shell=True
                )
                t_front = threading.Thread(target=stream_output, args=(frontend_process.stdout, "FRONTEND"), daemon=True)
                t_front.start()
                
    except KeyboardInterrupt:
        print_sys("Shutting down gracefully on CTRL+C...")
    finally:
        print_sys("Terminating backend...")
        backend_process.terminate()
        print_sys("Terminating frontend...")
        frontend_process.terminate()
        print_sys("All services terminated.")

if __name__ == "__main__":
    main()
