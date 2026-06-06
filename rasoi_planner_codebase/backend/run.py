# Launcher script: 3-Layer Hackathon Architecture
import os
import sys
import subprocess
import webbrowser
import time

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Verify that local assets have been downloaded before running
    tailwind_path = os.path.join(base_dir, "frontend", "css", "tailwind.min.css")
    chartjs_path = os.path.join(base_dir, "frontend", "js", "chart.umd.js")
    
    if not os.path.exists(tailwind_path) or not os.path.exists(chartjs_path):
        print("Error: Offline assets are missing!")
        print("Please run 'python download_assets.py' first to download required assets.")
        sys.exit(1)

    print("=" * 60)
    print("Starting 3-Layer Hackathon Architecture Environment")
    print("=" * 60)
    
    # Command to run uvicorn backend
    # We use sys.executable to ensure we use the same Python environment
    cmd = [
        sys.executable, 
        "-m", 
        "uvicorn", 
        "backend.server:app", 
        "--host", "127.0.0.1", 
        "--port", "8000"
    ]
    
    print("Spinning up Uvicorn server on http://127.0.0.1:8000...")
    server_process = None
    try:
        # Start server subprocess in base_dir
        server_process = subprocess.Popen(cmd, cwd=base_dir)
        
        # Wait a moment for server to bind
        time.sleep(1.5)
        
        # Open web browser automatically
        url = "http://127.0.0.1:8000"
        print(f"Opening default browser to {url}...")
        webbrowser.open(url)
        
        # Keep runner alive while server is running
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received. Shutting down server...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        if server_process and server_process.poll() is None:
            print("Terminating server process...")
            server_process.terminate()
            server_process.wait()
            print("Server terminated successfully.")
        print("Goodbye!")

if __name__ == "__main__":
    main()
