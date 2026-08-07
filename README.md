# Control Flow Flatten (`control-flow-flatten`)

**Category:** reverse engineering · **Difficulty:** hard · **Points:** 400

Obfuscated control-flow flattening hides a comparison against the seed.

## Run it

```bash
docker build -t picoclone/control-flow-flatten .
# `picoclone start control-flow-flatten` (or the web UI) prints the docker run line with your
# PICOCLONE_SERVER + PICOCLONE_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
picoclone submit control-flow-flatten 'picoclone{...}'
```

## Hints

- Rebuild the state machine / dispatcher.
- The compared constant (or decrypted string) is the Fernet seed.
