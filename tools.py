import subprocess
import platform
import socket
import psutil


def check_internet():
    """Check whether internet connectivity is available."""

    try:
        result = subprocess.run(
            ["ping", "-n", "1", "8.8.8.8"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            return "Internet connection is working."

        return "Internet connection appears to be unavailable."

    except Exception as e:
        return f"Internet check failed: {e}"


def check_dns():
    """Check DNS resolution."""

    try:
        ip_address = socket.gethostbyname("google.com")

        return f"DNS is working. google.com resolved to {ip_address}."

    except socket.gaierror:
        return "DNS resolution failed."


def get_system_info():
    """Get basic system information."""

    system = platform.system()
    release = platform.release()
    processor = platform.processor()

    memory = psutil.virtual_memory()

    return {
        "Operating System": f"{system} {release}",
        "Processor": processor,
        "RAM Total": f"{round(memory.total / (1024 ** 3), 2)} GB",
        "RAM Used": f"{memory.percent}%"
    }


# Test the tools
if __name__ == "__main__":

    print("\n===== INTERNET CHECK =====")
    print(check_internet())

    print("\n===== DNS CHECK =====")
    print(check_dns())

    print("\n===== SYSTEM INFORMATION =====")
    print(get_system_info())