# sandbox/generate_fernet_key.py

"""
Purpose: Generate a secure fernet key for use in Airflow's environment variables.
"""

from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key().decode()
    print(f"\n🔐 Fernet Key:\n{key}\n")

if __name__== "__main__":
    main()