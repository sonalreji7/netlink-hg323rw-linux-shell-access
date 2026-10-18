# Offline validation record

These checks were performed on 2026-10-18 against owner-supplied files. They do not represent a new live router session.

## Hexadecimal capture reconstruction

The original conversion script was reviewed and run in a separate working directory. Source files were left unchanged.

```text
Parsed rows: 336308
Missing bytes: 0
Duplicate bytes: 0
Conflicting bytes: 0
Size: 5,380,927 bytes
SHA-256: 0308c4d98b54ba6cc40db90651745e5777f465f2a4b55f5e2b2c7328eab55d57
```

A byte-for-byte comparison against the supplied rootfs.squashfs succeeded. The script's interval is [0xB4500000, 0xB4A21B3F); the last included address is 0xB4A21B3E. The image begins with hsqs. Consistency does not establish capture authenticity or firmware redistribution rights.

## SquashFS and extraction

Tool: unsquashfs 4.7.5 (2026/03/01).

- SquashFS 4.0; little-endian metadata; LZMA compression.
- Used bytes: 5,380,927; block size: 131,072.
- 1,104 inodes; 107 fragments; two IDs.
- Header timestamp: 2021-08-10 09:59:50 UTC. It is a filesystem timestamp, not proof of installation time.
- Extraction reported 676 files, 47 directories, 137 symlinks, one hardlink.
- Character/block device creation failed because extraction ran without superuser privileges. No escalation was used. This is a partial extraction with respect to device nodes, suitable for inspecting the recovered regular files.

The recovered bin/cli matched the supplied extracted_fs/bin/cli byte for byte.

## Executable and screenshot cross-check

bin/cli: ELF32 MSB (big-endian), MIPS, dynamic interpreter /lib/ld-uClibc.so.0; no section-header table.

| String | File offset | ELF mapped address |
| --- | --- | --- |
| Enter linux shell | 0x204b0 | 0x004204b0 |
| enterlinuxshell | 0x204c4 | 0x004204c4 |

These mapped addresses agree with the screenshot labels. The screenshots show command-table data and a matching routine, not a fully traced shell-launch implementation.

The extracted filesystem contains /etc/passwd as a symlink to /var/passwd. Absolute symlinks were inspected as links, not followed into the analysis host. bin/dropbear contains SSH-2.0-dropbear_0.48.

## Runtime limits

The supplied boot log verifies boot-time hardware/software reports. It does not show the enterlinuxshell transition followed by id or a UID-status check, or a successful SSH login. The final PON-related self-check failure remains a logged observation; its cause is not proven by this record.

See firmware-manifest.json for sizes and SHA-256 values. Raw firmware, extracted binaries, and embedded private key material are not part of this documentation commit.
