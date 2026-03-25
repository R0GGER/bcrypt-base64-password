# bcrypt-base64 password

A minimal Docker tool to generate bcrypt-hashed, base64-encoded passwords from the command line.

## Why Base64-encode a bcrypt hash?

This does **not** add cryptographic strength - the benefit is in the output format:

- **ASCII-safe:** only printable characters, safe for headers, JSON, URLs, and restricted character sets.
- **Lossless:** no need to re-hash (MD5/SHA) just to get a readable string; Base64 is reversible and fast.
- **Universal:** any system that expects a plain string can store and transport it as-is.

## Build

```bash
docker build -t bcrypt-base64 .
```

## Usage

```bash
docker run --rm bcrypt-base64 <password> [options]
```

### Options

| Option | Short | Description |
|---|---|---|
| `password` | | Password to hash (required) |
| `--rounds` | `-r` | Number of bcrypt rounds (default: 10) |
| `--no-base64` | | Output raw bcrypt hash without base64 encoding |

### Examples

```bash
# Default (10 rounds, base64 output)
docker run --rm bcrypt-base64 MyPassword

# 14 rounds
docker run --rm bcrypt-base64 MyPassword -r 14

# Raw bcrypt hash without base64
docker run --rm bcrypt-base64 MyPassword --no-base64

# Show help
docker run --rm bcrypt-base64 --help
```
