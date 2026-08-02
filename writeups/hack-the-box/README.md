# Hack The Box — CTF Practice Lab

My progress through [Hack The Box CTF](https://ctf.hackthebox.com/) challenges.
Each challenge folder holds the provided files, the exploit scripts and the write-up.

-----

## 📂 Challenges by Category

### 🌐 Web Exploitation

  * **TimeKORP** – [Write-up](./web/timekorp/README.md)
    > *Focus: Command injection through an unsanitised format string.*
  * **Jailbreak** – [Write-up](./web/jailbreak/README.md)
    > *Write-up pending.*
  * **HTBProxy** – [Files](./web/htb-proxy/)
    > *Handout: custom Go HTTP proxy in front of a Node.js backend.*
  * **Guild** – [Files](./web/guild/)
    > *Handout: Flask app with authentication, password reset and file uploads.*

### 🔐 Cryptography

  * **Dynastic** – [Files](./crypto/dynastic/)
    > *Focus: Reversing a positional Caesar-style substitution.*

### 🛡️ Pwn / Binary Exploitation

  * **Regularity** – [Files](./pwn/regularity/)
    > *Focus: Buffer overflows and memory corruption.*

### ⚙️ Reverse Engineering

  * **Flag Casino** – [Files](./rev/flag-casino/)
    > *Focus: Analyzing logic flow and binary disassembly.*

### 🔎 Forensics

  * **An Unusual Sighting** – [Files](./forensics/an-unusual-sighting/)
    > *Handout: a captured `bash_history` to reconstruct attacker activity from.*

### 🧩 Miscellaneous

  * **Character** – [Write-up](./misc/character/README.md)
    > *Focus: Scripting a remote oracle to leak the flag byte by byte.*

-----

## 🛠️ Environment & Tools

  * **Web:** Burp Suite, Ffuf, SQLMap
  * **Reverse:** Ghidra, IDA Pro, `ltrace`
  * **Pwn:** GDB (with Pwndbg), Pwntools

-----

### Quick Tips for Navigation

1.  Navigate to `<category>/<challenge>/`.
2.  Read the `README.md` (write-up) for the step-by-step solution.
3.  `handout/` holds the original challenge files, `solve/` holds the scripts used to capture the flag.
