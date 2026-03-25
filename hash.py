#!/usr/bin/env python3
import argparse
import bcrypt
import base64
import sys


def main():
    parser = argparse.ArgumentParser(description="Generate a bcrypt + base64 encoded password hash")
    parser.add_argument("password", help="The password to hash")
    parser.add_argument("-r", "--rounds", type=int, default=10, help="Number of bcrypt rounds (default: 10)")
    parser.add_argument("--no-base64", action="store_true", help="Output raw bcrypt hash without base64 encoding")
    args = parser.parse_args()

    hashed = bcrypt.hashpw(args.password.encode(), bcrypt.gensalt(args.rounds))

    if args.no_base64:
        print(hashed.decode())
    else:
        print(base64.b64encode(hashed).decode())


if __name__ == "__main__":
    main()
