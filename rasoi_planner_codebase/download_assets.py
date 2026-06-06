import os
import urllib.request

def download_file(url, filepath):
    print(f"Downloading {url} to {filepath}...")
    try:
        # User-Agent to avoid getting blocked by some CDNs
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully downloaded to {filepath}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        raise

def main():
    # Define directories
    base_dir = os.path.dirname(os.path.abspath(__file__))
    css_dir = os.path.join(base_dir, "frontend", "css")
    js_dir = os.path.join(base_dir, "frontend", "js")

    # Ensure directories exist
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)

    # Assets to download
    # Tailwind CSS v2.2.19 (precompiled full CSS utility bundle)
    tailwind_url = "https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css"
    tailwind_path = os.path.join(css_dir, "tailwind.min.css")

    # Chart.js v4.4.3 (UMD format, self-contained for offline script inclusion)
    chartjs_url = "https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.js"
    chartjs_path = os.path.join(js_dir, "chart.umd.js")

    # Run downloads
    download_file(tailwind_url, tailwind_path)
    download_file(chartjs_url, chartjs_path)
    print("All static assets prepared for offline execution.")

if __name__ == "__main__":
    main()
